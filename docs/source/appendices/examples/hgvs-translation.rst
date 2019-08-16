.. _hgvs-translation:

This notebook demonstrates the mechanics of translating an HGVS
expression to a VR representation for educational purposes. Users who
wish to translate HGVS or other expressions routinely should use
ga4gh.vr.extras.translator.

.. code:: ipython3

    # We'll translate this expression to VR:
    hgvs_expr = "NC_000013.11:g.32936732G>C"

.. code:: ipython3

    # 1. Translate the HGVS expression directly
    
    from ga4gh.vr import models
    
    allele = models.Allele(
        location = models.SequenceLocation(
            sequence_id = "refseq:NC_000013.11",
            interval = models.SimpleInterval(
                start = 32936731,
                end = 32936732
            )
        ),
        state = models.SequenceState(
            sequence = "C"
        )
    )
    
    allele.as_dict()




.. parsed-literal::

    {'location': {'interval': {'end': 32936732,
       'start': 32936731,
       'type': 'SimpleInterval'},
      'sequence_id': 'refseq:NC_000013.11',
      'type': 'SequenceLocation'},
     'state': {'sequence': 'C', 'type': 'SequenceState'},
     'type': 'Allele'}



.. code:: ipython3

    # 2. Replace the RefSeq sequence with a GA4GH sequence id
    # Implementations choose how to provide sequence and sequence accession services
    # The following uses the seqrepo REST interface (https://github.com/biocommons/seqrepo-rest-service/)
    
    from ga4gh.vr.extras.dataproxy import SeqRepoRESTDataProxy
    seqrepo_rest_service_url = "http://localhost:5000/seqrepo"
    dp = SeqRepoRESTDataProxy(base_url=seqrepo_rest_service_url)
    
    # In general, one identifier may be related to many others in another namespace
    # Therefore, translate_sequence_identifier() returns a list.
    # Because there will be only 1 ga4gh sequence digest, we choose the first
    # and then replace the sequence id in allele.location.
    
    refseq_ir = str(allele.location.sequence_id)
    ga4gh_ir = dp.translate_sequence_identifier(refseq_ir, "ga4gh")[0]
    allele.location.sequence_id = ga4gh_ir
    allele.as_dict()




.. parsed-literal::

    {'location': {'interval': {'end': 32936732,
       'start': 32936731,
       'type': 'SimpleInterval'},
      'sequence_id': 'ga4gh:SQ._0wi-qoDrvram155UmcSC-zA5ZK4fpLT',
      'type': 'SequenceLocation'},
     'state': {'sequence': 'C', 'type': 'SequenceState'},
     'type': 'Allele'}



.. code:: ipython3

    # 3. Generated the computed identifier
    # ga4gh_identify() serializes the object and computes the identifier
    # (ga4gh_serialize and ga4gh_digest are called internally)
    
    from ga4gh.core import ga4gh_identify
    ga4gh_identify(allele)




.. parsed-literal::

    'ga4gh:VA.n9ax-9x6gOC0OEt73VMYqCBfqfxG1XUH'



.. code:: ipython3

    allele_d = allele.as_dict()
    allele_d["id"] = ga4gh_identify(allele)
    allele_d




.. parsed-literal::

    {'location': {
      'interval': {'end': 32936732, 'start': 32936731, 'type': 'SimpleInterval'},
      'sequence_id': 'ga4gh:SQ._0wi-qoDrvram155UmcSC-zA5ZK4fpLT',
      'type': 'SequenceLocation'},
     'state': {'sequence': 'C', 'type': 'SequenceState'},
     'type': 'Allele',
     'id': 'ga4gh:VA.n9ax-9x6gOC0OEt73VMYqCBfqfxG1XUH'}



Using ga4gh.vr.extras.translator
================================

The VR Translator imports HGVS, SPDI, Beacon, and VCF formats, and
appropriate handles more complex cases than shown above.

.. code:: ipython3

    from ga4gh.vr.extras.translator import Translator
    tlr = Translator(data_proxy=dp)
    allele = tlr.from_hgvs(hgvs_expr)
    allele.as_dict()




.. parsed-literal::

    {'location': {
      'interval': {'end': 32936732, 'start': 32936731, 'type': 'SimpleInterval'},
      'sequence_id': 'ga4gh:SQ._0wi-qoDrvram155UmcSC-zA5ZK4fpLT',
      'type': 'SequenceLocation'},
     'state': {'sequence': 'C', 'type': 'SequenceState'},
     'type': 'Allele'}



