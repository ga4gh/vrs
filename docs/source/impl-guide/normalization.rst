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

VRS uses a "fully-justified" normalization algorithm adapted from
NCBI's Variant Overprecision Correction Algorithm [1]_.
Fully-justified normalization expands such ambiguous representation
over the entire region of ambiguity, resulting in an *unambiguous*
representation that may be readily compared with other alleles.

This algorithm was designed for :ref:`Allele` instances in which the
Reference Allele Sequence and Alternate Allele Sequence are
precisely known and intended to be normalized. In some instances,
this may not be desired, e.g. faithfully maintaining a sequence
represented as a repeating subsequence through a RepeatSequenceExpression
object. We also anticipate that these edge cases will not be common,
and encourage adopters to use the VRS Allele Normalization Algorithm
whenever possible.

Beginning with VRS 2.0, the normalization algorithm was extended to
leverage reference-encoded variant states, providing a mechanism for
compact representation of alleles that can be derived directly from the
reference sequence.

LiteralSequenceExpression Alleles
#################################

When normalizing an Allele with a `LiteralSequenceExpression` state,
the following normalization rules apply:

0. Start with an unnormalized Allele, with corresponding `reference sequence`
   and `alternate sequence`.

   a. The `reference sequence` refers to the subsequence at the
      Allele SequenceLocation.

   #. The `alternate sequence` refers to the Sequence described
      by the Allele `state` attribute.

   #. Let `start` and `end` initially be the start and end of the Allele
      SequenceLocation.

#. Trim common flanking sequence from Allele sequences.

   a. Trim common suffix sequence (if any) from both of the Allele
      Sequences and decrement `end` by the length of the trimmed suffix.

   #. Trim common prefix sequence (if any) from both of the Allele
      Sequences and increment `start` by the length of the trimmed prefix.

#. Compare the two Allele sequences, if:

   a. both are empty, the input Allele is a reference Allele. Return a new
      Allele with:

      i. the `location` from the input Allele.

      #. a `ReferenceLengthExpression` for the `state` with `length` and
         `repeatSubunitLength` both set to the length of the input `location`.

   #. both are non-empty, the input Allele has been normalized to a
      substitution. Return a new Allele with:

      i. a `location` using the modified `start` and `end` for the `location`.

      #. a `LiteralSequenceExpression` for the `state` using the trimmed
         `alternate sequence`.

   #. one is empty, the input Allele is an insertion (empty `Reference Allele
      Sequence`) or a deletion (empty `alternate sequence`). The length
      of the non-empty sequence is the `seed_length`. Continue to step 3.

#. Determine bounds of ambiguity.

   a. Left roll: Set a `left_roll_bound` equal to `start`. While the terminal
      base of the non-empty Allele sequence is equal to the base preceding
      the `left_roll_bound`, decrement `left_roll_bound` and circularly
      permute the Allele sequence by removing the last character of the
      Allele sequence, then prepending the character to the resulting Allele
      sequence.

   #. Right roll: Set a `right_roll_bound` equal to `start`. While the terminal
      base of the non-empty Allele sequence is equal to the base following
      the `right_roll_bound`, increment `right_roll_bound` and circularly permute
      the Allele sequence by removing the first character of the Allele
      sequence, then appending the character to the resulting Allele sequence.

#. Expand the Allele to cover the entire region of ambiguity.

   a. Prepend reference sequence from `left_roll_bound` to `start` to both Allele Sequences.

   #. Append reference sequence from `start` to `right_roll_bound` to both Allele Sequences.

   #. Set `start` to `left_roll_bound` and `end` to `right_roll_bound`.

#. Construct and return a new Allele.

   a. If the `left_roll_bound` and `right_roll_bound` are equal, the Allele is an
      unambiguous insertion. Return a new `Allele` with:

      i. a `location` using the modified `start` and `end`.

      #. a `LiteralSequenceExpression` for the `state` using the modified `alternate sequence`.

   #. If the Allele is a deletion, it is reference derived. Return a new Allele with:

      i. a `location` using the modified `start` and `end`.

      #. a `ReferenceLengthExpression` for the `state` using the `seed length` as the `repeatSubunitLength`
         and the length of the modified `alternate sequence` as the `length`.

   #. If the Allele is an ambiguous insertion, determine if it is reference derived.

      i. Determine the greatest factor `d` of the `seed length` such that `d` is less than or equal to the 
         length of the modified `reference sequence`, and there exists a subsequence of length `d` 
         derived from the modified `reference sequence` that can be circularly expanded to recreate 
         the modified `alternate sequence`.

      #. If a valid factor `d` is found, the insertion is reference-derived.

      #. If a valid factor `d` is not found, the insertion is not reference-derived.

   #. If the Allele is a reference-derived ambiguous insertion, return a new Allele using:

      i. a `location` using the modified `start` and `end`.

      #. a `ReferenceLengthExpression` for the `state` using `d` as the `repeatSubunitLength`
         and the length of the modified `alternate sequence` as the `length`.

   #. If the Allele is not a reference-derived ambiguous insertion, return a new Allele using:

      i. a `location` using the modified `start` and `end`.

      #. a `LiteralSequenceExpression` for the `state` using the modified `alternate sequence`.

.. _normalization-diagram:

.. figure:: ../images/normalize.png

    A demonstration of fully justifying an insertion allele.

    Reproduced from [2]_

**References**

.. [1] Holmes JB, Moyer E, Phan L, Maglott D, Kattman B.
	   **SPDI: Data Model for Variants and Applications at NCBI.
	   Bioinformatics.** 2019. `doi:10.1093/bioinformatics/btz856`_
	   
.. [2] Wagner AH, Babb L, Alterovitz G, Baudis M, Brush M, Cameron DL,
	   ..., Hart RK. **The GA4GH Variation Representation Specification (VRS):
	   a Computational Framework for the Precise Representation and
	   Federated Identification of Molecular Variation.**
	   bioRxiv. 2021. `doi:10.1101/2021.01.15.426843`_

.. _doi:10.1101/2021.01.15.426843: https://doi.org/10.1101/2021.01.15.426843
.. _doi:10.1093/bioinformatics/btz856: https://doi.org/10.1093/bioinformatics/btz856
