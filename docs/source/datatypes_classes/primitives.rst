Primitive Types
@@@@@@@@@@@@@@@

Primitive types represent simple values with syntactic or other
constraints. They enable correctness for values stored in VRS.

.. _IRI:

IRI
###

.. include::  ../defs/gks.common/IRI.rst

.. _Residue:

Residue
#######

A residue refers to a specific `monomer`_ within the `polymeric
chain`_ of a `protein`_ or `nucleic acid`_ (Source: `Wikipedia
Residue page`_).

.. include::  ../defs/vrs/Residue.rst

.. _SequenceString:

SequenceString
##############

A *sequence* is a character string representation of a contiguous,
linear polymer of nucleic acid or amino acid :ref:`Residues <Residue>`.
Sequences are the prevalent representation of these polymers,
particularly in the domain of variant representation.

.. include::  ../defs/vrs/SequenceString.rst

**Information Model**

A string constrained to match the regular expression ``^[A-Z*\-]*$``,
derived from the IUPAC one-letter nucleic acid and amino acid codes.

**Implementation Guidance**

* Sequences MAY be empty (zero-length) strings. Empty sequences are used as the
  replacement Sequence for deletion Alleles.
* Sequences MUST consist of only uppercase IUPAC abbreviations, including ambiguity codes.
* A Sequence provides a stable coordinate system by which an :ref:`Allele` MAY be located and
  interpreted.
* A Sequence MAY have several roles. A "reference sequence" is any Sequence used
  to define an :ref:`Allele`. A Sequence that replaces another Sequence is
  called a "replacement sequence".
* In some contexts outside VRS, "reference sequence" may refer
  to a member of set of sequences that comprise a genome assembly. In VRS
  specification, any sequence may be a "reference sequence", including those in
  a genome assembly.
* For the purposes of representing sequence variation, it is not
  necessary that Sequences be explicitly "typed" (i.e., DNA, RNA, or
  AA).

**Examples**

.. parsed-literal::

    "ACGT" (string)
