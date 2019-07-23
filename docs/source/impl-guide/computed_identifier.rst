.. _computed-identifiers:

Computed Identifiers
!!!!!!!!!!!!!!!!!!!!

The VR-Spec provides an algorithmic solution to deterministically
generate a globally unique identifier from a VR object itself. All
valid implementations of the VR Computed Identifier will generate the
same identifier when the objects are identical, and will generate
different identifiers when they are not. The VR Computed Digest
algorithm obviates centralized registration services, allows
computational pipelines to generate "private" ids efficiently, and
makes it easier for distributed groups to share data.

A VR Computed Identifier is computed as follows:

* :ref:`Serialize <serialization>` the object into binary data.
* :ref:`Generate a digest <digest>` from the binary data.
* :ref:`Construct an identifier` based on the digest and object type.

The following diagram depicts the operations necessary to generate a
computed identifier.  These operations are described in detail in the
subsequent sections.

.. _ser-dig-id:

.. figure:: ../images/id-dig-ser.png
   :align: left

   **Serialization, Digest, and Computed Identifier Operations**

   Entities are shown in gray boxes. Functions are denoted by bold
   italics.  The yellow, green, and blue boxes, corresponding to the
   ``ga4gh_digest``, ``vr_digest``, and ``vr_identify`` functions
   respectively, depict the dependencies among functions.
   ``SHA512t192`` is :ref:`SHA-512` truncated at 192 bits using the
   systematic name recommended by SHA-512.  base64url_ is the
   official name of the :ref:`Base64` encoding variant that uses a URL-safe
   character set.

   [`figure source <https://www.draw.io/?page-id=M8V1EMsVyfZQDDbK8gNL&title=VR%20diagrams.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fa%2Fharts.net%2Fuc%3Fid%3D1Qimkvi-Fnd1hhuixbd6aU4Se6zr5Nc1h%26export%3Ddownload>`__]



.. _serialization:

VR Serialization
@@@@@@@@@@@@@@@@

.. important:: Do not confuse VR serialization with other
   serialization formats, including JSON serialization used to
   transmit VR messages.  Although VR and JSON serializations appear
   similar, they are NOT interchangeable. A VR object might have many
   valid JSON serializations, but it will have only one valid VR
   serialization.

VR serialization converts a VR object into a binary representation in
preparation for computing a digest of the object.  The VR
serialization specification ensures that all implementations serialize
variation objects identically, and therefore that the digests will
also be identical.  |vr-spec| provides validation tests to ensure
compliance.

Although several proposals exist for serializing arbitrary data in a
consistent manner ([Gibson]_, [OLPC]_, [JCS]_), none have been
ratified. As a result, |vr-spec| defines a custom serialization format
that is consistent with these proposals but does not rely on them for
definition; it is hoped that a future ratified standard will be
forward compatible with the process described here.

The first step in serialization is to generate message content. To do
so, implementations MUST:

    * replace nested identifiable objects (i.e., objects that have id
      properties) with their corresponding *digests*
    * order arrays of digests and ids by Unicode Character Set values
    * filter out id fields
    * filter out fields with null values

The second step is to JSON serialize the message
content subject to the following REQUIREMENTS:

    * encode the serialization in UTF-8
    * exclude insignificant whitespace, as defined in `RFC8259§2
      <https://tools.ietf.org/html/rfc8259#section-2>`__
    * order all keys by Unicode Character Set values
    * use two-char escape codes when available, as defined in
      `RFC8259§7 <https://tools.ietf.org/html/rfc8259#section-7>`__

The criteria for the VR serialization method was that it must be
relatively easy and reliable to implement in any common computer
language.



.. _ga4gh-digest:

Digest
@@@@@@

Computing digests for identifiable VR objects consists of three steps:

1. Compute the `SHA-512`_ digest of a binary object.
2. Truncate the digest to the left-most 24 bytes (192 bits).  See
   :ref:`truncated-digest-collision-analysis` for the rationale for 24
   bytes.
3. Encode the truncated digest as a base64url_ ASCII string.


.. code-block:: python

   >>> import base64, hashlib
   >>> blob = b"ACGT"
   >>> digest = hashlib.sha512(blob).digest()
   >>> digest
   b'h\xa1x\xf7\xc7@\xc5\xc2@\xaag\xbaA\x84;\x11\x9d;\xf9\xf8 ...
   >>> base64.urlsafe_b64encode(digest[:24]).decode("ASCII")
   'aKF498dAxcJAqme6QYQ7EZ07-fiw8Kw2'



.. _ga4gh-identifier:

Identifier Construction
@@@@@@@@@@@@@@@@@@@@@@@

A `W3C CURIE <curie-spec>`_ format has the form::

    prefix ":" reference

The GA4GH VR Spec constructs computed identifiers as follows::

    "ga4gh" ":" <type_prefix> "." <digest>

Type prefixes used by VR are:

.. csv-table::
   :header: type_prefix, VR Spec class name
   :align: left

   SQ, Sequence
   VA, Allele
   VL, Location
   VT, Text
   VH, (reserved) Haplotype
   VG, (reserved) Genotype
   VX, (reserved) Translocation

For example::

    ga4gh:SQ.v_QTc1p-MUYdgrRv4LMT6ByXIOsdw3C_


.. note:: Do not confuse the W3C CURIE `prefix` ("ga4gh" in this case)
          with a prefix used to indicate type.










----

**References**

.. [Gibson] `Gibson Canonical JSON <http://gibson042.github.io/canonicaljson-spec/>`__
.. [OLPC] `OLPC Canonical JSON <http://wiki.laptop.org/go/Canonical_JSON>`__
.. [JCS] `JSON Canonicalization Scheme <https://tools.ietf.org/html/draft-rundgren-json-canonicalization-scheme-05>`__

----

scraps

* if the object is an Allele, normalize as described in
  :ref:`normalization`

The VR Computed Identifier algorithm applies only to *identifiable*
objects, that is, objects with an `id` property.  In addition, the
algorithm is defined only when nested objects use `ga4gh` identifiers.
For example, generating a Computed Identifier for an Allele requires a
Computed Identifier for the embedded location, which requires that the
reference sequence is defined using a Computed Identifier.


In addition, the VR Computed Identifier is explicitly NOT defined
(that is, invalid) if used with any other normalization,
serialization, or digest mechanism to generate a GA4GH Computed
Identifier.



.. note:: **Proposal for GA4GH-wide use**

   The Variation Representation team created the computed
   identifier scheme for VR objects.  However, this scheme is
   applicable and useful to the entire GA4GH ecosystem.  As a
   result, we are proposing that the computed identifier scheme
   described here be considered for adoption as a GA4GH-wide
   standard.  For this reason, we have adopted the use of the
   `ga4gh` prefix above. 

   If the Computed Identifier scheme is adopted as a GA4GH-wide
   standard, documentation and type prefixes would moved from the VR
   specification to a separate repository for GA4GH-wide use.



The VR Computed Identifier algorithm uses two well-established
standard algorithms, the SHA-512 hash function, which generates a
binary digest from binary data, and Base64 URL encoding, which encodes
binary data using printable characters.



