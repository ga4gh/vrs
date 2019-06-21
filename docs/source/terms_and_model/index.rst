Terminology & Information Model
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

When biologists define terms in order to describe phenomena and
observations, they rely on a background of human experience and
intelligence for interpretation. Definitions may be abstract, perhaps
correctly reflecting uncertainty of our understanding at the
time. Unfortunately, such terms are not readily translatable into an
unambiguous representation of knowledge.

For example, "allele" might refer to "an alternative form of a gene or
locus" [`Wikipedia`_], "one of two or more forms of the DNA sequence
of a particular gene" [`ISOGG`_], or "one of a set of coexisting
sequence alleles of a gene" [`Sequence Ontology`_]. Even for human
interpretation, these definitions are inconsistent: does the
definition precisely describe a specific change on a specific
sequence, or, rather, a more general change on an undefined sequence?
In addition, all three definitions are inconsistent with the practical
need for a way to describe sequence changes outside regions associated
with genes.

**The computational representation of biological concepts requires
translating precise biological definitions into data structures that
can be used by implementers.** This translation should result in a
representation of information that is consistent with conventional
biological understanding and, ideally, be able to accommodate future
data as well. The resulting *computational representation* of
information should also be cognizant of computational performance, the
minimization of opportunities for misunderstanding, and ease of
manipulating and transforming data.

Accordingly, for each term we define below, we begin by describing the
term as used by biologists (**biological definition**) as
available. When a term has multiple biological definitions, we
explicitly choose one of them for the purposes of this
specification. We then provide a computer modelling definition
(**computational definition**) that reformulates the biological
definition in terms of information content. We then translate each of
these computational definitions into precise specifications for the
(**logical model**). Terms are ordered "bottom-up" so that definitions
depend only on previously-defined terms.

.. note:: The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
          NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and
          "OPTIONAL" in this document are to be interpreted as
          described in `RFC 2119`_.


Primitive Concepts
@@@@@@@@@@@@@@@@@@

.. _id:

Id
==

**Biological definition**

None.

**Computational definition**

A `CURIE-formatted <curie-spec>`_ string that uniquely identifies a
specific instance of an object within a document.

**Implementation guidance**

* This specification RECOMMENDS using :ref:`computed-identifiers` as
  Ids.
* When an appropriate namespace exists at identifiers.org, that
  namespace MUST be used verbatim (case sensitive).


.. _residue:

Residue
=======

**Biological definition**

A residue refers to a specific `monomer`_ within the `polymeric
chain`_ of a `protein`_ or `nucleic acid`_ (Source: `Wikipedia Residue
page`_).

**Computational definition**

A character representing a specific residue (i.e., molecular species)
or groupings of these ("ambiguity codes"), using `one-letter IUPAC
abbreviations <https://www.genome.jp/kegg/catalog/codes1.html>`_ for
nucleic acids and amino acids.


.. _interbase-coordinates:

Interbase Coordinates
=====================

**Biological definition**

None.

**Computational definition**

Interbase coordinates refer to the zero-width points before and after :ref:`residues <Residue>`. An interval of interbase coordinates permits referring to any span, including an empty span, before, within, or after a sequence. See :ref:`interbase-coordinates-design` for more details on this design choice.


.. _sequence:

Sequence
========

**Biological definition**

A contiguous, linear polymer of nucleic acid or amino acid residues.

**Computational definition**

A character string of :ref:`Residues <Residue>` that represents a
biological sequence using the conventional sequence order (5'-to-3'
for nucleic acid sequences, and amino-to-carboxyl for amino acid
sequences). IUPAC ambiguity codes are permitted in Sequences.

**Information model**

A Sequence is a string, constrained to contain only characters representing IUPAC nucleic acid or
amino acid codes.

**Implementation guidance**

* Sequences MAY be empty (zero-length) strings. Empty sequences are used as the replacement Sequence
  for deletion Alleles.
* Sequences MUST consist of only uppercase IUPAC abbreviations, including ambiguity codes.

**Notes**

* A Sequence provides a stable coordinate system by which an :ref:`Allele` may be located and
  interpreted.
* A Sequence may have several roles. A “reference sequence” is any Sequence used to define an
  :ref:`Allele`. A Sequence that replaces another Sequence is called a “replacement sequence”.
* In some contexts outside the VR specification, “reference sequence” may refer to a member of set
  of sequences that comprise a genome assembly. In the VR specification, any sequence may be a
  “reference sequence”, including those in a genome assembly.
* For the purposes of representing sequence variation, it is not
  necessary that Sequences be explicitly “typed” (i.e., DNA, RNA, or
  AA).




.. toctree::
   :maxdepth: 2

   interval
   state
   location
   variation

