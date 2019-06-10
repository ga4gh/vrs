.. _normalization:

Normalization
!!!!!!!!!!!!!

VR Spec implementations MUST normalize Alleles to a fully justified
("expanded") form when generating :ref:`computed-identifiers`. The VR
Spec RECOMMENDS that Alleles at precise locations are also normalized
to a fully justified form.

Conceptually, fully justified variation is expanded to the outer
bounds of left- and right- shuffling. As a result, it describes the
unambiguous state of the resulting sequence.

The process for fully justifying two alleles (reference sequence and
alternate sequence) at an interval is:

* Trim common suffixes, if any, common to both allele sequences. Adjust the
  interval end position to be consistent with the reduced allele
  lengths.
* Trim common prefixes, if any, common to both allele sequences. Adjust the
  interval start position to be consistent with the reduced allele
  lengths.
* If neither allele is empty, the allele pairs represent a alleles
  that do not have common prefixes or suffixes.  Normalization is not
  applicable and the trimmed alleles are returned.
* If exactly one of the alleles is empty, they represent an insertion
  or deletion and are normalized as below. 
* Right extension: The non-empty sequence is iteratively circularly
  permuted rightward n-steps until the next allele residue does not
  match the next reference sequence residue. The interval end is
  adjusted rightward by n residues and the corresponding sequence is
  appeneded to both alleles.
* Left extension: Similar to right extension, but the non-empty
  allele is circularly permuted leftward, the interval start is
  adjusted by the number of steps, and corresponding sequence is
  prepended to both alleles.

This process results in normalization that is similar to NCBI's
Variant Overprecision Correction Algorithm [1]_.


**References**

.. [1] Bradley Holmes, J., Moyer, E., Phan, L., Maglott, D. & Kattman, B. L. *SPDI: Data Model for Variants and Applications at NCBI.* bioRxiv 537449 (2019). `doi:10.1101/537449`_

.. _doi:10.1101/537449: https://doi.org/10.1101/537449
