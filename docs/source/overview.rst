
GA4GH Variation Representation Overview
=======================================

The GA4GH Variation Representation Specification consists of two
components: a JSON schema that describes the structure of data, and
algorithmic conventions for how to use VR data structures to improve the
consistency of sequence variation shared in the community. This overview
of the VR Schema is from the python reference implementation at
https://github.com/ga4gh/vr-python/blob/master/notebooks/Overview.ipynb.
Users may wish to explore
https://github.com/ga4gh/vr-python/blob/master/notebooks/Extras.ipynb,
which provides additional functionality to construct VR objects from
HGVS, SPDI, and VCF.

GA4GH VR was formerly known as the Variation Modelling Collaboration
(VMC).

Using the Reference Implementation
----------------------------------

All publicly available functionality is accessed by importing from
``ga4gh.vr``, as shown below.

.. code:: ipython3

    from ga4gh.core import ga4gh_digest
    from ga4gh.vr import __version__, ga4gh_identify, ga4gh_serialize, models, normalize

.. raw:: html

   <div>
   <div style="border-radius: 10px; width: 80%; margin: 0 auto; padding: 5px; border: 2pt solid #660000; color: #660000; background: #f4cccc;">
   <span style="font-size: 200%">⚠</span> Import only from <code>ga4gh.vr</code>.
           Submodules contain implementation details that are likely to change without notice.
   </div>
   </div>

.. code:: ipython3

    # You can see the version of ga4gh.vr like so:
    __version__




.. parsed-literal::

    '0.2.1.dev56+gfa705ba.d20190620'



Top-Down View of VR Schema Classes
----------------------------------

The top-level VR classes are Location and Variation. A Location
describes *where* an event occurs. Variation describes an event at a
Location. Location and Variation are *abstract* objects — their purpose
is to provide a framework for the way we think about variation, but they
doen’t represent any particular instance themselves.

Currently, there is only one Location class: SequenceLocation, which
defines a precise span on a named sequence. Future Location classes will
include Cytoband Locations, Gene Locations, as well as SequenceLocations
using fuzzy and/or intronic coordinates.

There are two Variation subclasses: \* Text – a blob of text, used when
a textual representation is not (yet) parseable \* Allele – contiguous
state of a sequence or conceptual region Future kinds of Variation will
support haplotypes, genotypes, and translocations/fusions.

The top-level classes in VR are *identifiable*, meaning that VR
proscribes how implementations can compute globally-consistent
identifiers from the data.

See this figure for a schematic representation.

Locations
~~~~~~~~~

A Location is an *abstract* object that refer to contiguous regions of
biological sequences. Concrete types of Locations are shown below.

The most common Location is a SequenceLocation, i.e., a Location based
on a named sequence and an Interval on that sequence. Locations may also
be conceptual or symbolic locations, such as a cytoband region or a
gene. Any of these may be used as the Location for Variation.

SimpleInterval
^^^^^^^^^^^^^^

.. code:: ipython3

    simple_interval = models.SimpleInterval(start=42, end=43)
    simple_interval.as_dict()




.. parsed-literal::

    {'end': 43, 'start': 42, 'type': 'SimpleInterval'}



SequenceLocation
^^^^^^^^^^^^^^^^

.. code:: ipython3

    # A SequenceLocation based on a SimpleInterval
    sequence_location_si = models.SequenceLocation(
        sequence_id="refseq:NM_0001234.5",
        interval=simple_interval)
    ga4gh_identify(sequence_location_si)
    sequence_location_si.as_dict()




.. parsed-literal::

    {'id': 'ga4gh:SL.UqdjWOolIz8Vxd5b14eVND0vw88q0vqr',
     'interval': {'end': 43, 'start': 42, 'type': 'SimpleInterval'},
     'sequence_id': 'refseq:NM_0001234.5',
     'type': 'SequenceLocation'}



Text Variation
~~~~~~~~~~~~~~

In order to support variation descriptions that cannot be parsed, or
cannot be parsed yet, the VR provides a Text schema object. The
intention is to provide ids for *any* variation, particularly human
descriptions of variation.

.. code:: ipython3

    text_variation = models.Text(definition="PTEN loss")
    text_variation.as_dict()




.. parsed-literal::

    {'definition': 'PTEN loss', 'type': 'Text'}



Alleles
~~~~~~~

An Allele is an asserion of a SequenceState at a Location. The many
possible Location and SequenceState classes enable the representation of
many kinds of Variation.

“Simple” sequence replacements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This case covers any “ref-alt” style variation, which includes SNVs,
MNVs, del, ins, and delins.

.. code:: ipython3

    sequence_state = models.SequenceState(sequence="A")
    allele = models.Allele(location=sequence_location_si, state=sequence_state)
    ga4gh_identify(allele)
    allele.as_dict()




.. parsed-literal::

    {'id': 'ga4gh:VA.C0e28xlAfc9LVvCj_2092gF28UbtP3oX',
     'location': {'id': 'ga4gh:SL.UqdjWOolIz8Vxd5b14eVND0vw88q0vqr',
      'interval': {'end': 43, 'start': 42, 'type': 'SimpleInterval'},
      'sequence_id': 'refseq:NM_0001234.5',
      'type': 'SequenceLocation'},
     'state': {'sequence': 'A', 'type': 'SequenceState'},
     'type': 'Allele'}



--------------

Functions
---------

Conventions in the VR specification are implemented through several
algorithmic functions. They are:

-  ``normalize``: Implements sequence normalization for ins and del
   variation.
-  ``ga4gh_digest``: Implements a convention constructing and formatting
   digests for an object.
-  ``serialize``: Implements object serialization based on a canonical
   form of JSON.
-  ``identify``: Generates a computed identifier for an identifiable
   object.

normalize()
~~~~~~~~~~~

VR Spec RECOMMENDS that variation is reported as “expanded” alleles.
Expanded alleles capture the entire region of insertion/deletion
amiguity, thereby facilitating comparisons that would otherwise require
on-the-fly computations.

.. code:: ipython3

    # Define a dinucleotide insertion on the following sequence at interbase (13, 13)
    sequence = "CCCCCCCCACACACACACTAGCAGCAGCA"
    #    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9
    #     C C C C C C C C A C A C A C A C A C T A G C A G C A G C A
    #                              ^ insert CA here
    interval = (13, 13)
    alleles = (None, "CA")
    args = dict(sequence=sequence, interval=interval, alleles=alleles, bounds=(0,len(sequence)))

.. code:: ipython3

    # The expanded allele sequences
    normalize(**args, mode="EXPAND")




.. parsed-literal::

    ((7, 18), ('CACACACACAC', 'CACACACACACAC'))



.. code:: ipython3

    # For comparison, the left and right shuffled alleles
    normalize(**args, mode="LEFTSHUFFLE")




.. parsed-literal::

    ((7, 7), ('', 'CA'))



.. code:: ipython3

    normalize(**args, mode="RIGHTSHUFFLE")




.. parsed-literal::

    ((18, 18), ('', 'AC'))



ga4gh_digest()
~~~~~~~~~~~~~~

The ``ga4gh_digest`` is a convention for constructing unique identifiers
from binary objects (as from serialization) using well-known SHA512
hashing and Base64 (i.e., base64url) encoding.

.. code:: ipython3

    ga4gh_digest(b"")




.. parsed-literal::

    'z4PhNX7vuL3xVChQ1m2AB9Yg5AULVxXc'



.. code:: ipython3

    ga4gh_digest(b"ACGT")




.. parsed-literal::

    'aKF498dAxcJAqme6QYQ7EZ07-fiw8Kw2'



ga4gh_serialize()
~~~~~~~~~~~~~~~~~

Serialization is the process of converting an object to a *binary*
representation for transmission or communication. In the context of
generating GA4GH identifiers, serialization is a process to generate a
*canonical* JSON form in order to generate a digest. The VR
serialization is based on a JSON canonincialization scheme consistent
with several existing proposals. See the spec for details.

Because the serialization and digest methods are well-defined, groups
with the same data will generate the same digests and computed
identifiers.

GA4GH serialization replaces inline identifiable objects with their
digests in order to create a well-defined ordering. See the ``location``
property in the ``Allele`` example below.

.. raw:: html

   <div>
   <div style="border-radius: 10px; width: 80%; margin: 0 auto; padding: 5px; border: 2pt solid #660000; color: #660000; background: #f4cccc;">
       <span style="font-size: 200%">⚠</span> Although JSON serialization and GA4GH canonical JSON serialization appear similar, they are NOT interchangeable and will generated different digests. GA4GH identifiers are defined <i>only</i> when used with GA4GH serialization process.
   </div>
   </div>

.. code:: ipython3

    # This is the "simple" allele defined above, repeated here for readability
    # Note that the location data is inlined
    allele.as_dict()




.. parsed-literal::

    {'id': 'ga4gh:VA.C0e28xlAfc9LVvCj_2092gF28UbtP3oX',
     'location': {'id': 'ga4gh:SL.UqdjWOolIz8Vxd5b14eVND0vw88q0vqr',
      'interval': {'end': 43, 'start': 42, 'type': 'SimpleInterval'},
      'sequence_id': 'refseq:NM_0001234.5',
      'type': 'SequenceLocation'},
     'state': {'sequence': 'A', 'type': 'SequenceState'},
     'type': 'Allele'}



.. code:: ipython3

    # This is the serialized form. Notice that the inline `Location` instance was replaced with
    # its identifier and that the Allele id is not included. 
    ga4gh_serialize(allele)




.. parsed-literal::

    b'{"location":"UqdjWOolIz8Vxd5b14eVND0vw88q0vqr","state":{"sequence":"A","type":"SequenceState"},"type":"Allele"}'



ga4gh_identify()
~~~~~~~~~~~~~~~~

VR computed identifiers are constructed from digests on serialized
objects by prefixing a VR digest with a type-specific code.

.. code:: ipython3

    # applying ga4gh_digest to the serialized allele returns a base64url-encoded digest
    ga4gh_digest( ga4gh_serialize(allele) )




.. parsed-literal::

    'C0e28xlAfc9LVvCj_2092gF28UbtP3oX'



.. code:: ipython3

    # identify() uses this digest to construct a CURIE-formatted identifier.
    # The VA prefix identifies this object as a Variation Allele.
    ga4gh_identify(allele)




.. parsed-literal::

    'ga4gh:VA.C0e28xlAfc9LVvCj_2092gF28UbtP3oX'


