Primitive Types
@@@@@@@@@@@@@@@

Primitive types represent simple values with syntactic or other
constraints. They enable correctness for values stored in VRS.

.. _CURIE:

CURIE
#####

.. include:: ../defs/CURIE.rst

**Implementation Guidance**

* All identifiers in VRS MUST be a valid CURIE, regardless of
  whether the identifier refers to GA4GH VRS objects or external data.
* For GA4GH VRS objects, this specification RECOMMENDS using globally
  unique :ref:`computed-identifiers` for use within *and* between
  systems.
* For external data, CURIE-formatted identifiers MUST be used.  When
  an appropriate namespace exists at `identifiers.org
  <http://identifiers.org/>`__, that namespace MUST be used.  When an
  appropriate namespace does not exist at `identifiers.org
  <http://identifiers.org/>`__, support is implementation-dependent.
  That is, implementations MAY choose whether and how to support
  informal or local namespaces.
* Implementations MUST use CURIE identifiers verbatim. Implementations
  MAY NOT modify CURIEs in any way (e.g., case-folding).

**Examples**

Identifiers for GRCh38 chromosome 19:

.. parsed-literal::

    ga4gh:SQ.IIB53T8CNeJJdUqzn9V_JnRtQadwWCbl
    refseq:NC_000019.10
    grch38:19

See :ref:`identify` for examples of CURIE-based identifiers for VRS
objects.


**Information Model**

A string constrained to match the regular expression
``^cen|[pq](ter|([1-9][0-9]*(\.[1-9][0-9]*)?))$``, derived from the
ISCN guidelines [1]_.

.. [1] McGowan-Jordan J (Ed.). *ISCN 2016: An international system
       for human cytogenomic nomenclature (2016).* Karger (2016).

**Examples**

.. parsed-literal::

   "q13.32" (string)

.. _Residue:

Residue
#######

A residue refers to a specific `monomer`_ within the `polymeric
chain`_ of a `protein`_ or `nucleic acid`_ (Source: `Wikipedia
Residue page`_).

.. include:: ../defs/Residue.rst

.. _Sequence:

Sequence
########

A *sequence* is a character string representation of a contiguous,
linear polymer of nucleic acid or amino acid :ref:`Residues <Residue>`.
Sequences are the prevalent representation of these polymers,
particularly in the domain of variant representation.

.. include:: ../defs/Sequence.rst

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
