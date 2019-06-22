Implementations
!!!!!!!!!!!!!!!

Libraries
@@@@@@@@@

Libraries facilitate the use of the VR Spec, but do not implement a
particular use or application.  Although there is only one library
currently, it is expected that others will eventually appear as
VR Spec is adopted.


.. _impl-vr-python:

vr-python: GA4GH VR Reference Implementation
############################################

`vr-python <https://github.com/ga4gh/vr-python/>`__ is the reference
implementation for the GA4GH VR Spec.  It supports all types covered
by the VR Spec, implements Allele normalization and computed
identifier generation, and provides "extra" features such as
translation from HGVS, SPDI, and VCF formats.  The `Overview
<https://github.com/ga4gh/vr-python/blob/master/notebooks/Overview.ipynb>`__
and `Extras
<https://github.com/ga4gh/vr-python/blob/master/notebooks/Extras.ipynb>`__
Jupyter notebooks provide usage examples.


----

Applications and Web Services
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Applications implement VR Spec to support specific use cases.
Projects known to implement VR Spec are listed below. Descriptions are
provided by the application authors.


.. _impl-allele-registry:

ClinGen Allele Registry
#######################

ClinGen Allele Registry provides identifiers for more than 900 million variants. Each identifier (canonical allele identifiers: CAIds) is an abstract concept which represents a group of identical variants based on alignment. Identifiers are retrievable irrespective of the reference sequence and normalization status.

As a Driver Project for GA4GH, `ClinGen Allele Registry <https://reg.clinicalgenome.org>`__ implements two standards: RefGet and VR in the first implementation (**June 27, 2019**).

The API endpoints that support data retrieval in this two key standards are summarized in the following table.

**HOST**: `https//reg.clinicalgenome.org/ <https://reg.clinicalgenome.org>`__

.. csv-table::
   :header: API Path, Parameters, Response Format, Example,
   :align: left

   **RefGet**,,,
   [GET] /sequence/service-info, \-, Refget v1.0.0, `/sequence/service-info <https://reg.clinicalgenome.org/sequence/service-info>`
   [GET] /sequence/{id}, id => TRUNC512 digest for reference sequence, Refget v1.0.0, `/sequence/vYfm5TA_F-_BtIGjfzjGOj8b6IK5hCTx <https://reg.clinicalgenome.org/sequence/vYfm5TA_F-_BtIGjfzjGOj8b6IK5hCTx>`__
   [GET] /sequence/{id}/metadata, id => TRUNC512 digest for reference sequence, Refget v1.0.0, `/sequence/vYfm5TA_F-_BtIGjfzjGOj8b6IK5hCTx/metadata <https://reg.clinicalgenome.org/sequence/vYfm5TA_F-_BtIGjfzjGOj8b6IK5hCTx/metadata>`__
   **VR**,,,
   [GET] /vrAllele?hgvs={hgvs}, hgvs => HGVS expression, VR v1.0, `/vrAllele?hgvs=NC_000007.14:g.55181320A>T <https://reg.clinicalgenome.org/vrAllele?hgvs=NC_000007.14:g.55181320A%3ET>`__  `/vrAllele?hgvs=NC_000007.14:g.55181220del <https://reg.clinicalgenome.org/vrAllele?hgvs=NC_000007.14:g.55181220del>`__

Support for GA4GH refget and VR specs provided in ClinGen Allele Registry through implementation that is independent from VR-Python. Support for this community standards is implemented in ClinGen Allele Registry through extension of code written in C++.


.. _impl-brca-exchange:

BRCA Exchange
#############

BRCA Exchange proposes an API endpoint which will share the variant
list in VR JSON model.  Behind the scenes, all variants will be
represented according to VR specification, in a separate table of the
BRCA Exchange database, and the contents of this table will be served
by the BRCA Exchange API.  A stand-alone executable will leverage
these data to integrate the BRCA Exchange variant set with the ClinGen
allele registry.


.. _impl-vicc:

VICC Meta-knowledgebase
#######################

The Variant Interpretation for Cancer Consortium (VICC;
https://cancervariants.org) has a collection of ~20K clinical
interpretations describing ~3,500 somatic variations and variation
classes in a harmonized meta-knowledgebase [1]_ (see documentation at
http://docs.cancervariants.org). Each interpretation is be linked to
one or more variations or a variation class.

As a Driver Project for GA4GH, the VICC is contributing to and/or
adopting three GA4GH standards: VR, Variant Annotation (VA), and the
Data Use Ontology (DUO). The VICC will support queries on VR computed
identifiers at the searchAssociations endpoint (`vicc-docs`_).

**References:**

.. [1] Wagner, A.H., et al. *A harmonized meta-knowledgebase of clinical interpretations of cancer genomic variants.* bioRxiv 366856 (2018). `doi:10.1101/366856`_


.. _vicc-docs: https://search.cancervariants.org/api/v1/ui/#!/Associations/searchAssociations
.. _doi:10.1101/366856: https://doi.org/10.1101/366856
