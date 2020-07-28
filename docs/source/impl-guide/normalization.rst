.. _normalization:

Normalization
!!!!!!!!!!!!!

In VRS, "normalization" refers to the process of rewriting an
ambiguous variation representation of variation into a canonical form.
Normalization eliminates a class of ambiguity that impedes comparison
of variation across systems.

In the sequencing community, "normalization" refers to the process of
converting a given sequence variant into a canonical form, typically
by left- or right-shuffling insertion/deletion variants.  VRS
normalization extends this concept to all classes of VRS Variation
objects.

Implementations MUST provide a normalize function that accepts *any*
Variation object and returns a normalized Variation.  Guidelines for
these functions are below.


General Normalization Rules
@@@@@@@@@@@@@@@@@@@@@@@@@@@

* Object types that do not have explicit VRS normalization rules below
  are returned as-is.  That is, all types of Variation MUST be
  supported, even if such objects are unchanged.
* VRS normalization functions are idempotent: Normalizing a
  previously-normalized object returns an equivalent object.
* VRS normalization functions are not necessarily homomorphic: That
  is, the input and output objects may be of different types.



Allele Normalization
@@@@@@@@@@@@@@@@@@@@

Certain insertion or deletion alleles may have ambiguous
representations when using conventional sequence normalization,
resulting in significant challenges when comparing such alleles.

VRS uses a "fully-justified" normalization algorithm inspired by
NCBI's Variant Overprecision Correction Algorithm [1]_.
Fully-justified normalization expands such ambiguous representation
over the entire region of ambiguity, resulting in an *unambiguous*
representation that may be readily compared with other alleles.

VRS RECOMMENDS that Alleles at precise locations are normalized to a
fully justified form unless there is a compelling reason to do
otherwise.  Alleles SHOULD be normalized in order to generate
:ref:`computed-identifiers`.

The process for fully justifying an Allele is outlined below.

0. Given an Allele:

   a. Let `reference allele sequence` refer to the subsequence at the
      Allele's SequenceLocation.
   #. Let `alternate allele sequence` be the sequence in the Allele's
      State object.
   #. Let `start` and `end` initially be the `start` and `end` of the
      Allele's SequenceLocation.

#. Trim sequences:

   a. Remove suffixes common to the `reference allele sequence` and
      `alternate allele sequence`, if any. Decrement `end` by the
      length of the trimmed suffix.
   #. Remove prefixes common to the `reference allele sequence` and
      `alternate allele sequence`, if any. Increment `start` by the
      length of the trimmed prefix.

#. If `reference allele sequence` and `alternate allele sequence`
   are empty, the input Allele is a reference Allele.  Return the
   input Allele unmodified.

#. If `reference allele sequence` and `alternate allele sequence` are
   non-empty, the input Allele has been reduced to a substitution
   Allele.  Construct and return a new Allele with the current
   `start`, `end`, and `alternate allele sequence`.

   NOTE: The remaining cases are that exactly one of `reference allele
   sequence` or `alternate allele sequence` is empty.  If `reference
   allele sequence` is empty, the Allele represents an insertion in
   the reference.  If `alternate allele sequence` is empty, the Allele
   represents a deletion in the reference.

#. Determine bounds of ambiguity:

   a. Left roll: While the terminal base of all non-empty alleles is
      equal to the base *prior* to the current position, circularly
      permute all alleles *rightward* and move the current position
      *leftward*. When terminating, return `left_roll`, the number of
      steps rolled leftward.
   #. Right roll: Symmetric case of left roll, returning `right_roll`,
      the number of steps rolled rightward.

#. Fully justify the trimmed allele sequences:

   a. To the `reference allele sequence` and `alternate allele
      sequence`, prepend the `left_roll` bases prior to the trimmed
      allele position and append the `right_roll` bases after the
      trimmed allele position.
   b. Decrement `start` by `left_roll` and increment `end` by
      `right_roll`.

#. Construct and return a new Allele with the current `start`, `end`,
   and `alternate allele sequence`.



.. _normalization-diagram:

.. list-table::
     **VRS Justified Normalization** A demonstration of fully justifying an insertion allele.
   :class: reece-wrap
   :header-rows: 1
   :widths: 40 15 20
   :align: left

   *  -  | Steps
      -  | `start` and `end` (interbase)
	 | and allele sequences
      -  | Equivalent representations
   *  -  0. Given allele ``S:g.5_6delinsCAGCA`` defined on reference sequence S=TCAGCAGCT
      -  | (4,6)
         | (“CA”, “CAGCA”)
      -  .. math:: TCAG \Bigl[ \frac{CA}{CAGCA} \Bigr] GCT

   *  -  1. Trimming

            a. Remove suffix common to all alleles, if any, and update end position.
            b. Remove prefix common to all alleles, if any, and update start position. 

            **Note:**  This example shows removing C prefix and A suffix.
            Equivalently in this case, CA prefix or CA suffix could be removed.
      -  | (5,5)
         | (“”, “AGC”)
      -  .. math:: TCAGC \Bigl[ \frac{}{AGC} \Bigr] AGCT

   *  -  2. & 3. These conditions are False.
      -
      -

   *  -  4a. Roll Left

            Begin with trimmed alleles from (1).

            While the terminal base of all non-empty alleles equals the base
            prior to the current position, circularly permute all alleles right
            one step and move the start left one position.

            Shown: The 4 incremental steps of rolling left.
      -  | (1,1)
         | (“”, “CAG”)
      -  .. math::
            TCAGC \Bigl[ \frac{}{AGC} \Bigr] AGCT \\
            TCAG \Bigl[ \frac{}{CAG} \Bigr] CAGCT \\
            TCA \Bigl[ \frac{}{GCA} \Bigr] GCAGCT \\
            TC \Bigl[ \frac{}{AGC} \Bigr] AGCAGCT \\
            T \Bigl[ \frac{}{CAG} \Bigr] CAGCAGCT \\
            \Rightarrow left\_roll = 4

   *  -  4b. Roll Right

            Symmetric case of step 4a.
      -  | (8,8)
         | (“”, “AGC”)
      -  .. math::
            TCAGC \Bigl[ \frac{}{AGC} \Bigr] AGCT \\
            TCAGCA \Bigl[ \frac{}{GCA} \Bigr] GCT \\
            TCAGCAG \Bigl[ \frac{}{CAG} \Bigr] CT \\
            TCAGCAGC \Bigl[ \frac{}{AGC} \Bigr] T \\
            \Rightarrow right\_roll = 3

   *  -  5. Update position and alleles to fully justify within region of ambiguity.

            To each trimmed allele from (1), prepend the *left_roll*
            preceding reference bases and append the *right_roll*
            following reference bases (corresponding to the interbase
            reference spans (1,5) and (5,8) respectively).

            Decrement the start position by *left_roll*, and increment the end
            position by *right_roll*.
      -  | (1,8)
         | (“CAGCAGC”,
         | “CAGCAGCAGC”)
      -  .. math::
            T \Bigl[ \frac{CAGCAGC}{CAGCAGCAGC} \Bigr] T

**References**

.. [1] Holmes, J. B., Moyer, E., Phan, L., Maglott, D. &
       Kattman, B. L. *SPDI: Data Model for Variants and Applications
       at NCBI.* Bioinformatics (2020 March 15). `doi:10.1093/bioinformatics/btz856`_

.. _doi:10.1093/bioinformatics/btz856: https://doi.org/10.1093/bioinformatics/btz856
