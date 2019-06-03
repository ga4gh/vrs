Implementations
!!!!!!!!!!!!!!!

Reference Implementation
@@@@@@@@@@@@@@@@@@@@@@@@

vr-python


ClinGen Allele Registry
@@@@@@@@@@@@@@@@@@@@@@@

.. todo::

   Implementation notes for Allele Registry

VICC
@@@@

.. todo::

   Implementation notes for VICC

BRCA Exchange
@@@@@@@@@@@@@

BRCA Exchange proposes an API endpoint which will share the variant list in VR JSON model.  Behind the scenes, all variants will be represented according to VR specification, in a separate table of the BRCA Exchange database, and the contents of this table will be served by the BRCA Exchange API.  A stand-alone executable will leverage these data to integrate the BRCA Exchange variant set with the ClinGen allele registry.
