.. _CisPhasedBlock:

Cis-Phased Block
!!!!!!!!!!!!!!!!

The Cis-Phased Block is a set of Alleles that are found *in-cis*: occurring
on the same physical molecule. The `CisPhasedBlock` structure is useful for 
representing genetic *Haplotypes*, which are commonly described with respect
to locations on a gene, a set of nearby genes, or other physically proximal
genetic markers that tend to be transmitted together. Unlike haplotypes, the
`CisPhasedBlock` is not also used to convey information about genetic ancestry.

.. admonition:: New in v2

   In VRS v1, a class with the same computational use as the `CisPhasedBlock`
   was defined and named the `Haplotype` class. This term is not used to describe 
   this concept in v2, as the use of the `Haplotype` name created confusion in the
   community, due to the additional semantics of the term around genetic linkage 
   and ancestry. In practice, implmentations transitioning from v1 to v2 should
   find the `CisPhasedBlock` able to accommodate the same information content
   from v1 `Haplotypes`.

.. include::  ../../def/CisPhasedBlock.rst