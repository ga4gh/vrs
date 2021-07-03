.. _faq:

Frequently (Asked and) Answered Questions
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. glossary::

   How can I learn more about VRS? How can I get involved?
     See :ref:`getting-involved`.

   Why does VRS ...?  Why did you use interresidue coordinates?  Are they they same as 0-based coordinates?  Why aren't sequences typed?

      The first stop for these questions is :ref:`design-decisions`. 

   How does VRS handle strandedness?

     It doesn't. VRS presumes that all locations are with respect to
     the positive/forward/Watson strand.
   
   How do you deal with variation that need to hold large amounts of data?

     VRS models are minimal, meaning that they contain only the
     minimum information required to represent the instance.  They do
     not contain related information or annotations of any sort.  If
     an instance entails the insertion of a large arbitrary sequence,
     then the object will be large. Computed identifiers are fixed
     length and independent of the size of an object.

   How do you handle variant representations and annotation across multiple transcripts and reference builds?

     VRS does not currently structure any of the many notions of
     variant equivalence, although prototypes have been written.  As
     of VRS mid-2021, readers are advised to consult `VRSATILE
     <https://github.com/ga4gh/vrsatile>`__.
   
   How do you represent genotypes, especially for mosaicism and somatic variants (multi-ploidy)?  What existing tools can help bridge single-location variants and genotypes with VRS?

     VRS does not currently represent genotypes or mosaicism.
     Genotypes are expected in version 1.3 and will include support
     for moscaicim and chimerism.  VRS may currently be used to
     represent somatic variation; no specialized support is required.

   How do you represent different types of variation in a unified way (e.g. gene fusions)?

     VRS does not currently represent structural variation such as
     fusions or translocations.  Both are expected in version 1.3.

   How do you communicate the uncertainty about variants meaningfully to other providers?

     VRS represents variation only.  All annotations *about* variation
     are left to other systems.

   What makes it special/different/better than SPDI, VCF, and others?

     See :ref:`relationships`.
