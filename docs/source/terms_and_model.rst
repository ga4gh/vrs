Teminology & Information Model
==============================

When biologists define terms in order to describe phenomena and observations, they rely on a background of human experience and intelligence for interpretation. Definitions may be abstract, perhaps correctly reflecting uncertainty of our understanding at the time. Unfortunately, such terms are not readily translatable into an unambiguous representation of knowledge.

For example, "allele" might refer to "an alternative form of a gene or locus" [`Wikipedia`_], "one of two or more forms of the DNA sequence of a particular gene" [`ISOGG`_], or one of a set of coexisting sequence alleles of a gene [`Sequence Ontology`_]. Even for human interpretation, these definitions are inconsistent: does the definition describe a precise sequence change or a qualitative one? In addition, all three definitions are inconsistent with the practical need for a way to describe sequence changes outside regions associated with genes.

**The computational representation of biological concepts requires translating precise biological definitions into data structures that can be used by implementers.** This translation should result in a representation of information that is consistent with conventional biological understanding, and, ideally, be able to accommodate future data as well. The resulting *computational representation* of information should also be cognizant of computational performance, the minimization of opportunities for misunderstanding, and ease of manipulating and transforming data.

Accordingly, for each term we define below, we begin by describing the term as used by biologists (**biological definition**) as available. When a term has multiple biological definitions, we explicitly choose one of them for the purposes of this specification. We then provide a computer modeling definition (**computational definition**) that reformulates the biological definition in terms of information content. We then translate each of these computational definitions into precise specifications for representing information (**logical model**). Terms are ordered "bottom-up" so that definitions depend only on previously-defined terms.

.. note:: The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in `RFC 2119`_.

.. glossary::

    Residue
    Base
      **Biological definition:** A residue refers to a specific monomer within the polymeric chain of a protein or nucleic acid (Source: Wikipedia Residue page).

      **Computational definition:** Specific residues (i.e., molecular species) as well as categories or groupings of these ("ambiguity codes") are represented using one-letter IUPAC abbreviations.

    Interbase Coordinates
      **Biological definition:** None

      **Computational definition:** Interbase coordinates refer to the zero-width points before and after :term:`residues <Residue>`. An interval of interbase coordinates permits referring to any span, including an empty span, before, within, or after a sequence. See :ref:`interbase-coords` for more details on this design choice.

    Interval
      **Biological definition:** None.

      **Computational definition:** Two integers that define the start and end positions of a range of residues, possibly with length zero, and specified using interbase coordinates.

      .. csv-table:: **Information model**
         :header: Field, Type, Label, Description
         :align: left

         start, uint64, required, start position
         end, uint64, required, end position

      **Implementation guidance:**

      * Implementations MUST require that 0 ≤ start ≤ end. In the case of double-stranded DNA, this constraint holds even when a feature is on the complementary strand.

      **Notes:**

      * VR uses Interbase coordinates because they provide conceptual consistency that is not possible with residue-based systems (see :ref:`rationale <interbase-coords>`). Implementations `will need to convert`_ between interbase and 1-based inclusive residue coordinates familiar to most human users.
      * Interbase coordinates start at 0 (zero).
      * The length of an interval is *end - start*.
      * An interval in which start == end is a zero width point between two residues.
      * An interval of length == 1 may be colloquially referred to as a position.
      * Two intervals are *equal* if the their start and end coordinates are equal.
      * Two intervals *intersect* if the start or end coordinate of one is strictly between the start and end coordinates of the other. That is, if:

         * b.start < a.start < b.end OR
         * b.start < a.end < b.end OR
         * a.start < b.start < a.end OR
         * a.start < b.end < a.end
      * Two intervals a and b *coincide* if they intersect or if they are equal (the equality condition is required to handle the case of two identical zero-width Intervals).

      **Examples:**

      * <start, end>=<*0,0*> refers to the point with width zero before the first residue.
      * <start, end>=<*i,i+1*> refers to the *i+1th* (1-based) residue.
      * <start, end>=<*N,N*> refers to the position after the last residue for Sequence of length *N*.
      * See `Interbase Interval tests`_ in the VR-python repo for a diagram and examples.

    Sequence
      Lorem Ipsum

    Location
      Lorem Ipsum

    Allele
      A single contiguous :term:`Sequence` at a :term:`Location`.



.. _Wikipedia: https://en.wikipedia.org/wiki/Allele
.. _ISOGG: https://isogg.org/wiki/Allele
.. _Sequence Ontology: http://www.sequenceontology.org/browser/current_svn/term/SO:0001023
.. _RFC 2119: https://www.ietf.org/rfc/rfc2119.txt
.. _will need to convert: https://www.biostars.org/p/84686/
.. _Interbase Interval tests: https://github.com/ga4gh/vr-python/blob/master/notebooks/appendices/Interbase%20Interval%20tests.ipynb