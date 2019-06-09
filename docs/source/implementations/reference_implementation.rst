.. _vr-python:

VR-python Reference Implementation
======================================

The GA4GH Variation Representation Specification consists of two
components: a JSON schema that describes the structure of data, and
conventions for how to use that structure to improve the consistency of
sequence variation shared in the community. A reference implementation
in Python (vr-python; `GitHub`_) accompanies the specification and is demonstrated in this
notebook.

.. _GitHub: https://github.com/ga4gh/vr-python

Using the Reference Implementation
----------------------------------

All publicly available functionality is accessed by importing from
``ga4gh.vr``, as shown below.

.. code:: ipython3

    from ga4gh.core import ga4gh_digest
    from ga4gh.vr import identify, models, normalize, serialize, __version__

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

    '0.2.1.dev43+g54683c9.d20190604'



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
prescribes how implementations can compute globally-consistent
identifiers from the data.

See the :ref:`vr-schema-diagram` for a schematic representation.

Locations
~~~~~~~~~

A Location is an *abstract* object that refer to contiguous regions of
biological sequences. Concrete types of Locations are shown below.

The most common Location is a SequenceLocation, i.e., a Location based
on a named sequence and an Interval on that sequence. Locations may also
be conceptual or symbolic locations, such as a cytoband region or a
gene. Any of these may be used as the Location for Variation.

.. _simple-interval-example:

SimpleInterval
^^^^^^^^^^^^^^

.. code:: ipython3

    simple_interval = models.SimpleInterval(start=42, end=43)
    simple_interval.as_dict()




.. parsed-literal::

    {'end': 43, 'start': 42, 'type': 'SimpleInterval'}

.. _nested-interval-example:

NestedInterval
^^^^^^^^^^^^^^

Document conversion with ranged format

.. code:: ipython3

    nested_interval = models.NestedInterval(
        inner=models.SimpleInterval(start=29,end=30),
        outer=models.SimpleInterval(start=20,end=39))
    nested_interval.as_dict()




.. parsed-literal::

    {'inner': {'end': 30, 'start': 29, 'type': 'SimpleInterval'},
     'outer': {'end': 39, 'start': 20, 'type': 'SimpleInterval'},
     'type': 'NestedInterval'}



SequenceLocation
^^^^^^^^^^^^^^^^

.. code:: ipython3

    # A SequenceLocation based on a SimpleInterval
    sequence_location_si = models.SequenceLocation(
        sequence_id="NM_0001234.5",
        interval=simple_interval)
    sequence_location_si.id = identify(sequence_location_si)
    sequence_location_si.as_dict()




.. parsed-literal::

    {'id': 'ga4gh:SL/8KJJStVL_dJigtK_AHyVp5AAipy1pMh8',
     'interval': {'end': 43, 'start': 42, 'type': 'SimpleInterval'},
     'sequence_id': 'NM_0001234.5',
     'type': 'SequenceLocation'}



.. code:: ipython3

    # A SequenceLocation based on a NestedInterval
    sequence_location_ni = models.SequenceLocation(sequence_id="NM_0001234.5", 
                                                   interval=nested_interval)
    sequence_location_ni.id = identify(sequence_location_ni)
    sequence_location_ni.as_dict()




.. parsed-literal::

    {'id': 'ga4gh:SL/FdTUSDxD1Ja0jNLCTUHlzONhozgEuEvq',
     'interval': {'inner': {'end': 30, 'start': 29, 'type': 'SimpleInterval'},
      'outer': {'end': 39, 'start': 20, 'type': 'SimpleInterval'},
      'type': 'NestedInterval'},
     'sequence_id': 'NM_0001234.5',
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

An Allele is an assertion of a SequenceState at a Location. The many
possible Location and SequenceState classes enable the representation of
many kinds of Variation.

.. _simple-sequence-replacements:

"Simple" sequence replacements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This case covers any “ref-alt” style variation, which includes SNVs,
MNVs, del, ins, and delins.

.. code:: ipython3

    sequence_state = models.SequenceState(sequence="A")
    allele = models.Allele(location=sequence_location_si, state=sequence_state)
    allele.id = identify(allele)
    allele.as_dict()




.. parsed-literal::

    {'id': 'ga4gh:VA/Zp8e9tUGfwiTRfIIij7INFQKa_Hc4ep9',
     'location': {'id': 'ga4gh:SL/8KJJStVL_dJigtK_AHyVp5AAipy1pMh8',
      'interval': {'end': 43, 'start': 42, 'type': 'SimpleInterval'},
      'sequence_id': 'NM_0001234.5',
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

VR-Spec RECOMMENDS that variation is reported as “expanded” alleles.
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

.. code:: ipython3

    # The expanded allele sequences
    normalize(sequence=sequence, interval=interval, alleles=alleles, bounds=(0,len(sequence)),
              mode="EXPAND")




.. parsed-literal::

    ((7, 18), ('CACACACACAC', 'CACACACACACAC'))



.. code:: ipython3

    # For comparison, the left and right shuffled alleles
    normalize(sequence=sequence, interval=interval, alleles=alleles, bounds=(0,len(sequence)),
              mode="LEFTSHUFFLE")




.. parsed-literal::

    ((7, 7), ('', 'CA'))



.. code:: ipython3

    normalize(sequence=sequence, interval=interval, alleles=alleles, bounds=(0,len(sequence)),
              mode="RIGHTSHUFFLE")




.. parsed-literal::

    ((18, 18), ('', 'AC'))

.. _digest-example:

digest()
~~~~~~~~~~~~~~

The ``digest`` is a convention for constructing unique identifiers from binary objects (as from serialization) using well-known SHA512 hashing and base64url encoding.

.. code:: ipython3

    digest(b"")




.. parsed-literal::

    'z4PhNX7vuL3xVChQ1m2AB9Yg5AULVxXc'



.. code:: ipython3

    digest(b"ACGT")




.. parsed-literal::

    'aKF498dAxcJAqme6QYQ7EZ07-fiw8Kw2'



serialize()
~~~~~~~~~~~

Serialization is the process of converting an object to a *binary*
representation for transmission or communication. In VR, the serialized
form is used to generate a digest. Because the serialization and digest
methods are well-defined, groups with the same data will generate the
same identifier for any variation.

Importantly, serialization replaces inline identifiable objects with
their identifiers. See the ``location`` property in the ``Allele``
example below.

The VR serialization is based on a JSON canonincialization scheme
consistent with several existing proposals. See the spec for details.

.. raw:: html

   <div>
   <div style="border-radius: 10px; width: 80%; margin: 0 auto; padding: 5px; border: 2pt solid #660000; color: #660000; background: #f4cccc;">
       <span style="font-size: 200%">⚠</span> Although the <code>serialize()</code> result appears similar to JSON, implementations must be careful to use only the canonical JSON form to generate digests and identifiers.
   </div>
   </div>

.. code:: ipython3

    # This is the allele defined above. Notice that `location` is defined inline
    allele.as_dict()




.. parsed-literal::

    {'id': 'ga4gh:VA/Zp8e9tUGfwiTRfIIij7INFQKa_Hc4ep9',
     'location': {'id': 'ga4gh:SL/8KJJStVL_dJigtK_AHyVp5AAipy1pMh8',
      'interval': {'end': 43, 'start': 42, 'type': 'SimpleInterval'},
      'sequence_id': 'NM_0001234.5',
      'type': 'SequenceLocation'},
     'state': {'sequence': 'A', 'type': 'SequenceState'},
     'type': 'Allele'}



.. code:: ipython3

    # This is the serialized form. Notice that the inline `Location` instance was replaced with
    # its identifier and that the Allele id is not included. 
    serialize(allele)




.. parsed-literal::

    b'{"location":"ga4gh:SL/8KJJStVL_dJigtK_AHyVp5AAipy1pMh8","state":{"sequence":"A","type":"SequenceState"},"type":"Allele"}'



identify()
~~~~~~~~~~

VR computed identifiers are constructed from digests on serialized
objects by prefixing a VR digest with a type-specific code.

.. code:: ipython3

    # applying ga4gh_digest to the serialized allele returns a base64url-encoded digest
    ga4gh_digest( serialize(allele) )




.. parsed-literal::

    'Zp8e9tUGfwiTRfIIij7INFQKa_Hc4ep9'



.. code:: ipython3

    # identify() uses this digest to construct a CURIE-formatted identifier.
    # The VA prefix identifies this object as a Variation Allele.
    identify(allele)




.. parsed-literal::

    'ga4gh:VA/Zp8e9tUGfwiTRfIIij7INFQKa_Hc4ep9'



--------------

ga4gh.vr.extras
---------------

Data Proxy
~~~~~~~~~~

VR implementations will need access to sequences and sequence
identifiers. Sequences are used during normalization and, as shown
below, during conversions with other formats. Sequence identifiers are
necessary in order to translate identfiers from common forms to a
digest-based form. The VR specification leaves the choice of those data
sources to the implementations. One source is
`SeqRepo <https://github.com/biocommons/biocommons.seqrepo/>`__, which
is shown below. ga4gh.vr.extras.dataproxy provides an abstract base
class that facilitates using other data sources.

.. code:: ipython3

    # This will only work if a seqrepo REST interface is running on this URL:
    seqrepo_rest_service_url = "http://localhost:5000/seqrepo"
    
    from ga4gh.vr.extras.dataproxy import SeqRepoRESTDataProxy
    dp = SeqRepoRESTDataProxy(base_url=seqrepo_rest_service_url)

.. code:: ipython3

    dp.get_metadata("refseq:NM_000551.3")


.. parsed-literal::

    2019-06-04 12:23:21 snafu ga4gh.vr.extras.dataproxy[23085] INFO Fetching http://localhost:5000/seqrepo/1/metadata/RefSeq:NM_000551.3




.. parsed-literal::

    {'added': '2016-08-24T05:03:11Z',
     'aliases': ['MD5:215137b1973c1a5afcf86be7d999574a',
      'RefSeq:NM_000551.3',
      'SEGUID:T12L0p2X5E8DbnL0+SwI4Wc1S6g',
      'SHA1:4f5d8bd29d97e44f036e72f4f92c08e167354ba8',
      'VMC:GS_v_QTc1p-MUYdgrRv4LMT6ByXIOsdw3C\_',
      'ga4gh:SQ/v_QTc1p-MUYdgrRv4LMT6ByXIOsdw3C\_',
      'TRUNC512:bff413735a7e31461d82b46fe0b313e81c9720eb1dc370bf',
      'gi:319655736'],
     'alphabet': 'ACGT',
     'length': 4560}



.. code:: ipython3

    dp.get_sequence("ga4gh:SQ/v_QTc1p-MUYdgrRv4LMT6ByXIOsdw3C_", start=0, end=50) + "..."


.. parsed-literal::

    2019-06-04 12:23:21 snafu ga4gh.vr.extras.dataproxy[23085] INFO Fetching http://localhost:5000/seqrepo/1/sequence/VMC:GS_v_QTc1p-MUYdgrRv4LMT6ByXIOsdw3C\_




.. parsed-literal::

    'CCTCGCCTCCGTTACAACGGCCTACGGTGCTGGAGGATCCTTCTGCGCAC...'



Format translator
~~~~~~~~~~~~~~~~~

ga4gh.vr.extras.translator translates various formats into VR
representations.

.. raw:: html

   <div>

::

   <div style="border-radius: 10px; width: 80%; margin: 0 auto; padding: 5px; background: #d9ead3; border: 2pt solid #274e13; color: #274e13">
   <span style="font-size: 200%">🚀</span> The examples below use the same variant in 4 formats: HGVS, beacon, spdi, and VCF/gnomAD. Notice that the resulting Allele objects and computed identifiers are identical.</b>
   </div>

.. raw:: html

   </div>

.. code:: ipython3

    from ga4gh.vr.extras.translator import Translator
    tlr = Translator(data_proxy=dp)


.. parsed-literal::

    2019-06-04 12:23:21 snafu hgvs[23085] INFO hgvs 1.3.0.post0; released: False


.. code:: ipython3

    a = tlr.from_hgvs("NC_000013.11:g.32936732G>C")
    a.as_dict()


.. parsed-literal::

    2019-06-04 12:23:21 snafu ga4gh.vr.extras.translator[23085] INFO Creating  parser
    2019-06-04 12:23:23 snafu ga4gh.vr.extras.dataproxy[23085] INFO Fetching http://localhost:5000/seqrepo/1/metadata/RefSeq:NC_000013.11




.. parsed-literal::

    {'id': 'ga4gh:VA/xlv08oyqHKbmkP7mW38FwIf9scOrogMW',
     'location': {'id': 'ga4gh:SL/0FXQTd1CoM6ElQtD7qK1Ge6XGYhH6OZt',
      'interval': {'end': 32936732, 'start': 32936731, 'type': 'SimpleInterval'},
      'sequence_id': 'ga4gh:SQ_0wi-qoDrvram155UmcSC-zA5ZK4fpLT',
      'type': 'SequenceLocation'},
     'state': {'sequence': 'C', 'type': 'SequenceState'},
     'type': 'Allele'}



.. code:: ipython3

    # from_beacon: Translate from beacon's form
    a = tlr.from_beacon("13 : 32936732 G > C")
    a.as_dict()


.. parsed-literal::

    2019-06-04 12:23:23 snafu ga4gh.vr.extras.dataproxy[23085] INFO Fetching http://localhost:5000/seqrepo/1/metadata/GRCh38:13




.. parsed-literal::

    {'id': 'ga4gh:VA/xlv08oyqHKbmkP7mW38FwIf9scOrogMW',
     'location': {'id': 'ga4gh:SL/0FXQTd1CoM6ElQtD7qK1Ge6XGYhH6OZt',
      'interval': {'end': 32936732, 'start': 32936731, 'type': 'SimpleInterval'},
      'sequence_id': 'ga4gh:SQ_0wi-qoDrvram155UmcSC-zA5ZK4fpLT',
      'type': 'SequenceLocation'},
     'state': {'sequence': 'C', 'type': 'SequenceState'},
     'type': 'Allele'}



.. code:: ipython3

    # SPDI uses 0-based coordinates
    a = tlr.from_spdi("NC_000013.11:32936731:1:C")
    a.as_dict()




.. parsed-literal::

    {'id': 'ga4gh:VA/xlv08oyqHKbmkP7mW38FwIf9scOrogMW',
     'location': {'id': 'ga4gh:SL/0FXQTd1CoM6ElQtD7qK1Ge6XGYhH6OZt',
      'interval': {'end': 32936732, 'start': 32936731, 'type': 'SimpleInterval'},
      'sequence_id': 'ga4gh:SQ_0wi-qoDrvram155UmcSC-zA5ZK4fpLT',
      'type': 'SequenceLocation'},
     'state': {'sequence': 'C', 'type': 'SequenceState'},
     'type': 'Allele'}



.. code:: ipython3

    a = tlr.from_vcf("13-32936732-G-C")   # gnomAD-style expression
    a.as_dict()




.. parsed-literal::

    {'id': 'ga4gh:VA/xlv08oyqHKbmkP7mW38FwIf9scOrogMW',
     'location': {'id': 'ga4gh:SL/0FXQTd1CoM6ElQtD7qK1Ge6XGYhH6OZt',
      'interval': {'end': 32936732, 'start': 32936731, 'type': 'SimpleInterval'},
      'sequence_id': 'ga4gh:SQ_0wi-qoDrvram155UmcSC-zA5ZK4fpLT',
      'type': 'SequenceLocation'},
     'state': {'sequence': 'C', 'type': 'SequenceState'},
     'type': 'Allele'}



