.. _computed-identifiers:

Computed Identifiers
!!!!!!!!!!!!!!!!!!!!

VRS provides an algorithmic solution to deterministically generate a
globally unique identifier from a VRS object itself. All valid
implementations of the VRS Computed Identifier will generate the same
identifier when the objects are identical, and will generate different
identifiers when they are not. The VRS Computed Digest algorithm
obviates centralized registration services, allows computational
pipelines to generate "private" ids efficiently, and makes it easier
for distributed groups to share data.

A VRS Computed Identifier for a VRS concept is computed as follows:

* The object SHOULD be :ref:`normalized <normalization>`.
  Normalization formally applies to all VRS classes.

* Generate binary data to digest through :ref:`digest-serialization`.

* Generate a :ref:`truncated-digest` from the binary data.

* :ref:`Construct an identifier <identify>` based on the digest and object type.

.. important:: Normalizing objects is STRONGLY RECOMMENDED for
               interoperability. While normalization is not strictly
               required, automated validation mechanisms are
               anticipated that will likely disqualify Variation that
               is not normalized. See :ref:`should-normalize` for
               a rationale.

The following diagram depicts the operations necessary to generate a
computed identifier.  These operations are described in detail in the
subsequent sections.


.. _ser-dig-id:
.. figure:: ../images/id-dig-ser.png

   Serialization, Digest, and Computed Identifier Operations

   Entities are shown in gray boxes. Functions are denoted by bold
   italics.  The yellow, green, and blue boxes, corresponding to the
   ``sha512t24u``, ``ga4gh_digest``, and ``ga4gh_identify`` functions
   respectively, depict the dependencies among functions.  ``SHA512``
   is `SHA-512`_ truncated to 24 bytes (192 bits), using the SHA-512
   initialization vector.  base64url_ is the official name of the
   variant of `Base64`_ encoding that uses a URL-safe character
   set. [`figure source
   <https://www.draw.io/?page-id=M8V1EMsVyfZQDDbK8gNL&title=VR%20diagrams.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fa%2Fharts.net%2Fuc%3Fid%3D1Qimkvi-Fnd1hhuixbd6aU4Se6zr5Nc1h%26export%3Ddownload>`__]

.. note:: Most implementation users will need only the
	  ``ga4gh_identify`` function.  We describe the
	  ``ga4gh_serialize``, ``ga4gh_digest``, and ``sha512t24u``
	  functions here primarily for implementers.


Requirements
@@@@@@@@@@@@

Implementations MUST adhere to the following requirements:

* Implementations MUST use the normalization, serialization, and
  digest mechanisms described in this section when generating GA4GH
  Computed Identifiers.  Implementations MUST NOT use any other
  normalization, serialization, or digest mechanism to generate a
  GA4GH Computed Identifier.

* When computing identifiers, implementations MUST ensure that each 
  nested :ref:`Ga4ghIdentifiableObject` is referenced with a GA4GH 
  Computed Identifier.

.. note:: The GA4GH schema MAY be used with identifiers from any
          namespace. For example, a SequenceLocation may be defined
          using a `sequence_id` = ``refseq:NC_000019.10``.  However,
          an implementation of the Computed Identifier algorithm MUST
          first translate sequence accessions to GA4GH RefGet ``SQ``
          accessions to be compliant with this specification.

.. admonition:: New in v2
  
    In VRS v2, all objects now inherit from :ref:`Entity`, providing a
    means by which common expressions and accessions for VRS objects can 
    be provided in other fields as decorative metadata, alongside object 
    IDs. Implementations may freely implement such fields without impacting
    computed identifiers. Implementations are therefore encouraged (but not
    required) to use the ``ID`` field strictly for computed identifiers and 
    use decorative fields for alternate accessions, to reduce computational
    complexity.

.. _digest-serialization:

Digest Serialization
@@@@@@@@@@@@@@@@@@@@

.. TODO:: update digest serialization section to discuss ga4gh.keys

Digest serialization converts a VRS object into a binary representation
in preparation for computing a digest of the object.  The Digest
Serialization specification ensures that all implementations serialize
variation objects identically, and therefore that the digests will
also be identical.  |VRS| provides validation tests to ensure
compliance.

VRS uses the JSON Canonicalization Scheme (`RFC 8785`_) to
serialize JSON data, and includes additional preprocessing steps to
ensure computed digests are not impacted by decorative metadata.

.. admonition:: New in V2
    
    Beginning in VRS v2, object value data and descriptive metadata may be
    passed in the same object, providing a means for sharing commonly
    expected annotations (e.g. a "Ref Allele") on VRS objects. Read
    :ref:`ga4gh-digest-keys` for more.

The first step in serialization is to generate message content.

If the object is an instance of a VRS class, implementations MUST:

    * ensure that objects are referenced with identifiers in the
      ``ga4gh`` namespace
    * replace each nested :term:`identifiable object` with their
      corresponding *digests*
    * order arrays of digests and ids by Unicode Character Set values
    * filter out fields not included in the class :ref:`ga4gh-digest-keys`
      (if defined)
    * filter out fields with null values

The second step is to JSON serialize the message content following the
`RFC 8785`_ specification, which includes these REQUIRED constraints:

    * encode the serialization in UTF-8
    * exclude insignificant whitespace, as defined in `RFC8785§3.2.1
      <https://datatracker.ietf.org/doc/html/rfc8785#section-3.2.1>`__
    * order all keys by Unicode Character Set values
    * use predefined JSON control character codes when available, 
      as defined in `RFC8785§3.2.2.1 <https://datatracker.ietf.org/doc/html/rfc8785#section-3.2.2.2>`__

The criteria for the digest serialization method was that it must be
relatively easy and reliable to implement in any common computer
language.

.. _digest-serialization-example:

**Example**

.. code:: ipython3

    allele = models.Allele(location=models.SequenceLocation(
        sequence_id="ga4gh:SQ.IIB53T8CNeJJdUqzn9V_JnRtQadwWCbl",
        interval=simple_interval),
        state=models.SequenceState(sequence="T"))
    ga4gh_serialize(allele)

Gives the following *binary* (UTF-8 encoded) data:

.. parsed-literal::

    {"location":"u5fspwVbQ79QkX6GHLF8tXPCAXFJqRPx","state":{"sequence":"T","type":"SequenceState"},"type":"Allele"}

For comparison, here is one of many possible JSON serializations of the same object:

.. code:: ipython3

    allele.for_json()

.. parsed-literal::

    {
      "location": {
        "interval": {
          "end": 44908822,
          "start": 44908821,
          "type": "SimpleInterval"
        },
        "sequence_id": "ga4gh:SQ.IIB53T8CNeJJdUqzn9V_JnRtQadwWCbl",
        "type": "SequenceLocation"
      },
      "state": {
        "sequence": "T",
        "type": "SequenceState"
      },
      "type": "Allele"
    }



.. _truncated-digest:

Truncated Digest (sha512t24u)
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

The sha512t24u truncated digest algorithm [Hart2020]_ computes an ASCII digest
from binary data.  The method uses two well-established standard
algorithms, the `SHA-512`_ hash function, which generates a binary
digest from binary data, and a URL-safe variant of `Base64`_ encoding, which encodes
binary data using printable characters.

Computing the sha512t24u truncated digest for binary data consists of
three steps:

1. Compute the `SHA-512`_ digest of a binary data.
2. Truncate the digest to the left-most 24 bytes (192 bits).  See
   :ref:`truncated-digest-collision-analysis` for the rationale for 24
   bytes.
3. Encode the truncated digest as a base64url_ ASCII string.



.. code-block:: python

   >>> import base64, hashlib
   >>> def sha512t24u(blob):
           digest = hashlib.sha512(blob).digest()
           tdigest = digest[:24]
           tdigest_b64u = base64.urlsafe_b64encode(tdigest).decode("ASCII")
           return tdigest_b64u
   >>> sha512t24u(b"ACGT")
   'aKF498dAxcJAqme6QYQ7EZ07-fiw8Kw2'


.. _identify:
.. _identifier-construction:

Identifier Construction
@@@@@@@@@@@@@@@@@@@@@@@

The final step of generating a computed identifier for a VRS object is
to generate a `W3C CURIE <https://www.w3.org/TR/curie/>`__ formatted identifier, which
has the form::

    prefix ":" reference

The GA4GH VRS constructs computed identifiers as follows::

    "ga4gh" ":" type_prefix "." <digest>

.. warning:: Do not confuse the W3C CURIE ``prefix`` ("ga4gh") with the
          type prefix.

Type prefixes used by VRS are:

.. _type_prefixes:
.. csv-table::
   :header: type_prefix, VRS class name
   :align: left

   VA, Allele
   CPB, CisPhasedBlock
   CN, CopyNumberCount
   CX, CopyNumberChange
   AJ, Adjacency
   TM, Terminus
   DM, DerivativeMolecule
   SL, SequenceLocation
   SQ, Sequence (`RefGet <https://samtools.github.io/hts-specs/refget.html#refget-checksum-algorithm:~:text=The%20addition%20of%20SQ.%20to%20the%20string>`_)

For example, the identifer for the allele example under :ref:`digest-serialization` gives:

.. parsed-literal::

   ga4gh\:VA.EgHPXXhULTwoP4-ACfs-YCXaeUQJBjH\_


References
@@@@@@@@@@

.. [Hart2020] Hart RK, Prlić A. **SeqRepo: A system for managing local
			  collections of biological sequences.** PLoS
			  One. 2020;15:
			  e0239883. `doi:10.1371/journal.pone.0239883
			  <https://journals.plos.org/plosone/article/comments?id=10.1371/journal.pone.0239883>`__

.. _RFC 8785: https://datatracker.ietf.org/doc/html/rfc8785