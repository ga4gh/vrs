
ga4gh.vr.extras
===============

This notebook demonstrates functionality in the vr-python package that
builds on the VR specification but is not formally part of the
specification.

Data Proxy
----------

VR implementations will need access to sequences and sequence
identifiers. Sequences are used during normalization and during
conversions with other formats. Sequence identifiers are necessary in
order to translate identfiers from common forms to a digest-based
identifier.

The VR specification leaves the choice of those data sources to the
implementations. In vr-python, ``ga4gh.vr.extras.dataproxy`` provides an
abstract base class as a basis for data source adapters. One source is
`SeqRepo <https://github.com/biocommons/biocommons.seqrepo/>`__, which
is used below. (An adapter based on the GA4GH refget specification
exists, but is pending necessary changes to the refget interface to
provide accession-based lookups.)

SeqRepo: `github <https://github.com/biocommons/biocommons.seqrepo/>`__
\| `data snapshots <http://dl.biocommons.org/seqrepo/>`__ \|
`seqrepo-rest-service @
github <https://github.com/biocommons/seqrepo-rest-service>`__ \|
`seqrepo-rest-service docker
images <https://cloud.docker.com/u/biocommons/repository/docker/biocommons/seqrepo-rest-service>`__

RefGet: `spec <https://samtools.github.io/hts-specs/refget.html>`__ \|
`perl server <https://github.com/andrewyatz/refget-server-perl>`__

.. code:: ipython3

    from ga4gh.core import ga4gh_digest
    from ga4gh.vr import __version__, ga4gh_identify, ga4gh_serialize, models, normalize
    from ga4gh.vr.extras.dataproxy import SeqRepoRESTDataProxy
    
    seqrepo_rest_service_url = "http://localhost:5000/seqrepo"

.. code:: ipython3

    # Requires seqrepo REST interface is running on this URL (e.g., using docker image)
    dp = SeqRepoRESTDataProxy(base_url=seqrepo_rest_service_url)

.. code:: ipython3

    dp.get_metadata("refseq:NM_000551.3")

.. code:: python

    {'added': '2016-08-24T05:03:11Z',
     'aliases': ['MD5:215137b1973c1a5afcf86be7d999574a',
      'RefSeq:NM_000551.3',
      'SEGUID:T12L0p2X5E8DbnL0+SwI4Wc1S6g',
      'SHA1:4f5d8bd29d97e44f036e72f4f92c08e167354ba8',
      'VMC:GS_v_QTc1p-MUYdgrRv4LMT6ByXIOsdw3C_',
      'ga4gh:SQ.v_QTc1p-MUYdgrRv4LMT6ByXIOsdw3C_',
      'TRUNC512:bff413735a7e31461d82b46fe0b313e81c9720eb1dc370bf',
      'gi:319655736'],
     'alphabet': 'ACGT',
     'length': 4560}



.. code:: ipython3

    dp.get_sequence("ga4gh:SQ.v_QTc1p-MUYdgrRv4LMT6ByXIOsdw3C_", start=0, end=50) + "..."


.. code:: python

    'CCTCGCCTCCGTTACAACGGCCTACGGTGCTGGAGGATCCTTCTGCGCAC...'



Format translator
-----------------

ga4gh.vr.extras.translator translates various formats into VR
representations.

.. raw:: html

   <div>
   <div style="border-radius: 10px; width: 80%; margin: 0 auto; padding: 5px; background: #d9ead3; border: 2pt solid #274e13; color: #274e13">
   <span style="font-size: 200%">🚀</span> The examples below use the same variant in 4 formats: HGVS, beacon, spdi, and VCF/gnomAD. Notice that the resulting Allele objects and computed identifiers are identical.</b>
   </div>
   </div>

.. code:: ipython3

    from ga4gh.vr.extras.translator import Translator
    tlr = Translator(data_proxy=dp)


.. code:: ipython3

    a = tlr.from_hgvs("NC_000013.11:g.32936732G>C")
    a.as_dict()


.. code:: python


    {'id': 'ga4gh:VA.n9ax-9x6gOC0OEt73VMYqCBfqfxG1XUH',
     'location': {'id': 'ga4gh:SL.v9K0mcjQVugxTDIcdi7GBJ_R6fZ1lsYq',
      'interval': {'end': 32936732, 'start': 32936731, 'type': 'SimpleInterval'},
      'sequence_id': 'ga4gh:SQ._0wi-qoDrvram155UmcSC-zA5ZK4fpLT',
      'type': 'SequenceLocation'},
     'state': {'sequence': 'C', 'type': 'SequenceState'},
     'type': 'Allele'}



.. code:: ipython3

    # from_beacon: Translate from beacon's form
    a = tlr.from_beacon("13 : 32936732 G > C")
    a.as_dict()


.. code:: python

    {'id': 'ga4gh:VA.n9ax-9x6gOC0OEt73VMYqCBfqfxG1XUH',
     'location': {'id': 'ga4gh:SL.v9K0mcjQVugxTDIcdi7GBJ_R6fZ1lsYq',
      'interval': {'end': 32936732, 'start': 32936731, 'type': 'SimpleInterval'},
      'sequence_id': 'ga4gh:SQ._0wi-qoDrvram155UmcSC-zA5ZK4fpLT',
      'type': 'SequenceLocation'},
     'state': {'sequence': 'C', 'type': 'SequenceState'},
     'type': 'Allele'}



.. code:: ipython3

    # SPDI uses 0-based coordinates
    a = tlr.from_spdi("NC_000013.11:32936731:1:C")
    a.as_dict()




.. code:: python

    {'id': 'ga4gh:VA.n9ax-9x6gOC0OEt73VMYqCBfqfxG1XUH',
     'location': {'id': 'ga4gh:SL.v9K0mcjQVugxTDIcdi7GBJ_R6fZ1lsYq',
      'interval': {'end': 32936732, 'start': 32936731, 'type': 'SimpleInterval'},
      'sequence_id': 'ga4gh:SQ._0wi-qoDrvram155UmcSC-zA5ZK4fpLT',
      'type': 'SequenceLocation'},
     'state': {'sequence': 'C', 'type': 'SequenceState'},
     'type': 'Allele'}



.. code:: ipython3

    a = tlr.from_vcf("13-32936732-G-C")   # gnomAD-style expression
    a.as_dict()


.. code:: python

    {'id': 'ga4gh:VA.n9ax-9x6gOC0OEt73VMYqCBfqfxG1XUH',
     'location': {'id': 'ga4gh:SL.v9K0mcjQVugxTDIcdi7GBJ_R6fZ1lsYq',
      'interval': {'end': 32936732, 'start': 32936731, 'type': 'SimpleInterval'},
      'sequence_id': 'ga4gh:SQ._0wi-qoDrvram155UmcSC-zA5ZK4fpLT',
      'type': 'SequenceLocation'},
     'state': {'sequence': 'C', 'type': 'SequenceState'},
     'type': 'Allele'}



Detailed HGVS Examples
----------------------

These examples were contributed by Ronak Patel to assess the `ClinGen
Allele Registry <https://reg.clinicalgenome.org/>`__ implementation of
VR.

.. code:: ipython3

    hgvs_exprs = [
        "NC_000013.11:g.32936732C=",
        "NC_000007.14:g.55181320A>T",
        "NC_000007.14:g.55181220del",
        "NC_000007.14:g.55181230_55181231insGGCT"
    ]

.. code:: ipython3

    import pprint
    from IPython.display import HTML, display
    import tabulate
    
    def pre(o):
        return f"<pre>{o}</pre>"
    def hrow(h):
        return f"<tr style='background:#ffc'> <th colspan=2 style='text-align:left'>{h}</th> </tr>"
    def row(h, d):
        return f"<tr> <th>{h}</th> <td style='text-align:left'>{pre(d)}</td> </tr>"
    
    table_blocks = []
    for hgvs_expr in hgvs_exprs:
        a = tlr.from_hgvs(hgvs_expr)
        table_blocks = (
            hrow(pre(hgvs_expr)),
            row("json", pprint.pformat(a.as_dict())),
            row("ga4gh identifier", ga4gh_identify(a)),
            row("ga4gh serialization (allele)", ga4gh_serialize(a)),
            row("ga4gh serialization (location)", ga4gh_serialize(a.location)),
        )
        display(HTML("<table>" + "".join(table_blocks) + "</table>"))


.. raw:: html

    <table><tr style='background:#ffc'> <th colspan=2 style='text-align:left'><pre>NC_000013.11:g.32936732C=</pre></th> </tr><tr> <th>json</th> <td style='text-align:left'><pre>{'id': 'ga4gh:VA.n9ax-9x6gOC0OEt73VMYqCBfqfxG1XUH',
     'location': {'id': 'ga4gh:SL.v9K0mcjQVugxTDIcdi7GBJ_R6fZ1lsYq',
                  'interval': {'end': 32936732,
                               'start': 32936731,
                               'type': 'SimpleInterval'},
                  'sequence_id': 'ga4gh:SQ._0wi-qoDrvram155UmcSC-zA5ZK4fpLT',
                  'type': 'SequenceLocation'},
     'state': {'sequence': 'C', 'type': 'SequenceState'},
     'type': 'Allele'}</pre></td> </tr><tr> <th>ga4gh identifier</th> <td style='text-align:left'><pre>ga4gh:VA.n9ax-9x6gOC0OEt73VMYqCBfqfxG1XUH</pre></td> </tr><tr> <th>ga4gh serialization (allele)</th> <td style='text-align:left'><pre>b'{"location":"v9K0mcjQVugxTDIcdi7GBJ_R6fZ1lsYq","state":{"sequence":"C","type":"SequenceState"},"type":"Allele"}'</pre></td> </tr><tr> <th>ga4gh serialization (location)</th> <td style='text-align:left'><pre>b'{"interval":{"end":32936732,"start":32936731,"type":"SimpleInterval"},"sequence_id":"_0wi-qoDrvram155UmcSC-zA5ZK4fpLT","type":"SequenceLocation"}'</pre></td> </tr></table>


.. raw:: html

    <table><tr style='background:#ffc'> <th colspan=2 style='text-align:left'><pre>NC_000007.14:g.55181320A>T</pre></th> </tr><tr> <th>json</th> <td style='text-align:left'><pre>{'id': 'ga4gh:VA.vU0meY5wGjpyRLCjSxCfb2Jlruyn2adL',
     'location': {'id': 'ga4gh:SL.5D9eG-ev4fA7mYIpOpDEe-4Am1lzPZlQ',
                  'interval': {'end': 55181320,
                               'start': 55181319,
                               'type': 'SimpleInterval'},
                  'sequence_id': 'ga4gh:SQ.F-LrLMe1SRpfUZHkQmvkVKFEGaoDeHul',
                  'type': 'SequenceLocation'},
     'state': {'sequence': 'T', 'type': 'SequenceState'},
     'type': 'Allele'}</pre></td> </tr><tr> <th>ga4gh identifier</th> <td style='text-align:left'><pre>ga4gh:VA.vU0meY5wGjpyRLCjSxCfb2Jlruyn2adL</pre></td> </tr><tr> <th>ga4gh serialization (allele)</th> <td style='text-align:left'><pre>b'{"location":"5D9eG-ev4fA7mYIpOpDEe-4Am1lzPZlQ","state":{"sequence":"T","type":"SequenceState"},"type":"Allele"}'</pre></td> </tr><tr> <th>ga4gh serialization (location)</th> <td style='text-align:left'><pre>b'{"interval":{"end":55181320,"start":55181319,"type":"SimpleInterval"},"sequence_id":"F-LrLMe1SRpfUZHkQmvkVKFEGaoDeHul","type":"SequenceLocation"}'</pre></td> </tr></table>



.. raw:: html

    <table><tr style='background:#ffc'> <th colspan=2 style='text-align:left'><pre>NC_000007.14:g.55181220del</pre></th> </tr><tr> <th>json</th> <td style='text-align:left'><pre>{'id': 'ga4gh:VA.csOXic4ezsVVEPJjM7jdcx4cCYuWNvFx',
     'location': {'id': 'ga4gh:SL.eDAO6enI-Mok9nCCJotVmsKzi0vwBF9t',
                  'interval': {'end': 55181220,
                               'start': 55181219,
                               'type': 'SimpleInterval'},
                  'sequence_id': 'ga4gh:SQ.F-LrLMe1SRpfUZHkQmvkVKFEGaoDeHul',
                  'type': 'SequenceLocation'},
     'state': {'sequence': '', 'type': 'SequenceState'},
     'type': 'Allele'}</pre></td> </tr><tr> <th>ga4gh identifier</th> <td style='text-align:left'><pre>ga4gh:VA.csOXic4ezsVVEPJjM7jdcx4cCYuWNvFx</pre></td> </tr><tr> <th>ga4gh serialization (allele)</th> <td style='text-align:left'><pre>b'{"location":"eDAO6enI-Mok9nCCJotVmsKzi0vwBF9t","state":{"sequence":"","type":"SequenceState"},"type":"Allele"}'</pre></td> </tr><tr> <th>ga4gh serialization (location)</th> <td style='text-align:left'><pre>b'{"interval":{"end":55181220,"start":55181219,"type":"SimpleInterval"},"sequence_id":"F-LrLMe1SRpfUZHkQmvkVKFEGaoDeHul","type":"SequenceLocation"}'</pre></td> </tr></table>



.. raw:: html

    <table><tr style='background:#ffc'> <th colspan=2 style='text-align:left'><pre>NC_000007.14:g.55181230_55181231insGGCT</pre></th> </tr><tr> <th>json</th> <td style='text-align:left'><pre>{'id': 'ga4gh:VA.mL71zVuJ7BKsB6U825nJuGv31S84puyd',
     'location': {'id': 'ga4gh:SL.YRGVXC7g1ScsKl_z594KbS8FLflV3sLV',
                  'interval': {'end': 55181230,
                               'start': 55181230,
                               'type': 'SimpleInterval'},
                  'sequence_id': 'ga4gh:SQ.F-LrLMe1SRpfUZHkQmvkVKFEGaoDeHul',
                  'type': 'SequenceLocation'},
     'state': {'sequence': 'GGCT', 'type': 'SequenceState'},
     'type': 'Allele'}</pre></td> </tr><tr> <th>ga4gh identifier</th> <td style='text-align:left'><pre>ga4gh:VA.mL71zVuJ7BKsB6U825nJuGv31S84puyd</pre></td> </tr><tr> <th>ga4gh serialization (allele)</th> <td style='text-align:left'><pre>b'{"location":"YRGVXC7g1ScsKl_z594KbS8FLflV3sLV","state":{"sequence":"GGCT","type":"SequenceState"},"type":"Allele"}'</pre></td> </tr><tr> <th>ga4gh serialization (location)</th> <td style='text-align:left'><pre>b'{"interval":{"end":55181230,"start":55181230,"type":"SimpleInterval"},"sequence_id":"F-LrLMe1SRpfUZHkQmvkVKFEGaoDeHul","type":"SequenceLocation"}'</pre></td> </tr></table>


