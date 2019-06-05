ClinGen Allele Registry
!!!!!!!!!!!!!!!!!!!!!!!

ClinGen Allele Registry provides identifiers for more than 900 million variants. Each identifier (canonical allele identifiers: CAIds) is an abstract concept which represents a group of identical variants based on alignment. Identifiers are retrievable irrespective of the reference sequence and normalization status.

As a driver project for GA4GH, allele registry implements two standards: RefGet and VR. The API endpoints that support data retrieval in this two key standards are summarized in the following table.

**HOST**: https//reg.clinicalgenome.org/

.. csv-table::
   :header: API Path, Parameters, Response Format, Example
   :align: left

   **RefGet**,,,
   [GET] /sequence/service-info, \-, Refget v1.0.0, /sequence/service-info
   [GET] /sequence/{id}, id => TRUNC512 digest for reference sequence, Refget v1.0.0, /sequence/vYfm5TA_F-_BtIGjfzjGOj8b6IK5hCTx
   **VR**,,,
   [GET] /vrAllele?hgvs={hgvs}, hgvs => HGVS expression, VR v1.0, /vrAllele?hgvs=NM_002496.3:c.64C>T

The GA4GH identifiers for allele (ga4gh/allele:vYfm5TA_F-_BtIGjfzjGOj8b6IK5hCTx) and sequence (e.g. ga4gh/refget:vYfm5TA_F-_BtIGjfzjGOj8b6IK5hCTx) are retrievable from the human readable variant centric pages following GA4GH icon next to sequence and HGVS expressions.

Documentation of service is provided in the link available through registry landing page (https://reg.clinicalgenome.org).