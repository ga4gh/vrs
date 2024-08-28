.. _required-data:

Required External Data
!!!!!!!!!!!!!!!!!!!!!!

All VRS implementations will require external data regarding
sequences and sequence metadata. The choices of data sources and
access methods are left to implementations. This section provides
guidance about how to implement required data and helps implementers
estimate effort. This section is descriptive only: it is not intended
to impose requirements on interface to, or sources of, external data.
For clarity and completeness, this section also describes the contexts
in which external data are used.


Contexts
@@@@@@@@

* **Conversion from other variant formats** When converting from other
  variation formats, implementations MUST translate primary database
  accessions or identifiers (|eg| ``NM_000551.3`` or
  ``refseq:NM_000551.3``) to a GA4GH RefGet sequence accession (
  ``SQ.v_QTc1p-MUYdgrRv4LMT6ByXIOsdw3C_``). Implementations MAY
  choose to annotate :ref:`SequenceReference` objects with other public
  accessions for the sequence.

* **Conversion to other variant formats** When converting to other
  variation formats, implementations SHOULD translate GA4GH RefGet
  sequence accessions ( ``SQ.v_QTc1p-MUYdgrRv4LMT6ByXIOsdw3C_``)
  to primary database identifiers (``refseq:NM_000551.3``) that will
  be more readily recognized by users.

* **Normalization** During :ref:`normalization`, implementations will
  need access to sequence length and sequence contexts.


Data Services
@@@@@@@@@@@@@

The following table summarizes data required in the above contexts:

.. list-table:: Data Service Descriptions
   :header-rows: 1
   :class: reece-wrap

   * - Data Service
     - Description
     - Contexts
   * - sequence
     - For a given sequence identifier and range, return the
       corresponding subsequence.
     - normalization
   * - sequence length
     - For a given sequence identifier, return the length of the
       sequence
     - normalization
   * - identifier translation
     - For a given sequence identifier and target namespace, return
       all identifiers in the target namespace that are equivalent to
       the given identifier.
     - Conversion to/from other formats


.. note:: Construction of the GA4GH computed identifier for a sequence
          is described in :ref:`computed-identifiers`.



Suggested Implementation
@@@@@@@@@@@@@@@@@@@@@@@@

In order to maximize portability and to insulate implementations from
decisions about external data sources, implementers should consider
writing an abstract data proxy interface to define a service, and
then implement this interface for each data backend to be
supported. The data proxy interface defines three methods:

* ``get_sequence(identifier, start, end)``: Given a sequence
  identifier and start and end coordinates, return the corresponding
  sequence segment.
* ``get_metadata(identifier)``: Given a sequence identifier, return a
  dictionary of length, alphabet, and known aliases.
* ``translate_sequence_identifier(identifier, namespace)``: Given a
  sequence identifier, return all aliases in the specified
  namespace. Zero or more aliases may be returned.

The :ref:`impl-vrs-python` `DataProxy class
<https://github.com/ga4gh/vrs-python/blob/main/src/ga4gh/vrs/dataproxy.py>`__
provides an example of this design pattern and sample replies.
|vrs-python| implements the DataProxy interface using a local
|seqrepo| instance backend and using a |seqrepo_rs| backend.

Examples
########

The following examples are taken from |notebooks|:

To create the SeqRepoDataProxy:

.. code:: ipython3

    from ga4gh.vrs.dataproxy import create_dataproxy
    seqrepo_rest_service_url = "seqrepo+https://services.genomicmedlab.org/seqrepo"
    seqrepo_dataproxy = create_dataproxy(uri=seqrepo_rest_service_url)

To get the RefGet accession from a public accession identifier:

.. code:: ipython3

    seqrepo_dataproxy.derive_refget_accession("refseq:NM_002439.5")
    'SQ.Pw3Ch0x3XWD6ljsnIfmk_NERcZCI9sNM'

To get sequence length, aliases, and other optional information for a given identifier:

.. code:: ipython3

    seqrepo_dataproxy.get_metadata("refseq:NM_000551.3")
    {'added': '2016-08-24T05:03:11Z',
    'aliases': ['MD5:215137b1973c1a5afcf86be7d999574a',
      'NCBI:NM_000551.3',
      'refseq:NM_000551.3',
      'SEGUID:T12L0p2X5E8DbnL0+SwI4Wc1S6g',
      'SHA1:4f5d8bd29d97e44f036e72f4f92c08e167354ba8',
      'VMC:GS_v_QTc1p-MUYdgrRv4LMT6ByXIOsdw3C_',
      'sha512t24u:v_QTc1p-MUYdgrRv4LMT6ByXIOsdw3C_',
      'ga4gh:SQ.v_QTc1p-MUYdgrRv4LMT6ByXIOsdw3C_'],
    'alphabet': 'ACGT',
    'length': 4560}

To get the specified sequence or subsequence:

.. code:: ipython3

    identifier = "ga4gh:SQ.v_QTc1p-MUYdgrRv4LMT6ByXIOsdw3C_"
    seqrepo_dataproxy.get_sequence(identifier, start=0, end=51)
    'CCTCGCCTCCGTTACAACGGCCTACGGTGCTGGAGGATCCTTCTGCGCACG'

To translate an identifier to a list of identifiers in the ga4gh namespace:

.. code:: ipython3

    seqrepo_dataproxy.translate_sequence_identifier("GRCh38:19", "ga4gh")
    ['ga4gh:SQ.IIB53T8CNeJJdUqzn9V_JnRtQadwWCbl']

To translate an identifier to a list of identifiers in the GRCh38 namespace:

.. code:: ipython3

    seqrepo_dataproxy.translate_sequence_identifier("ga4gh:SQ.IIB53T8CNeJJdUqzn9V_JnRtQadwWCbl", "GRCh38")
    ['GRCh38:19', 'GRCh38:chr19']
