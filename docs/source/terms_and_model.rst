##############################
Teminology & Information Model
##############################

When biologists define terms in order to describe phenomena and observations, they rely on a background of human experience and intelligence for interpretation. Definitions may be abstract, perhaps correctly reflecting uncertainty of our understanding at the time. Unfortunately, such terms are not readily translatable into an unambiguous representation of knowledge.

For example, "allele" might refer to "an alternative form of a gene or locus" [`Wikipedia`_], "one of two or more forms of the DNA sequence of a particular gene" [`ISOGG`_], or one of a set of coexisting sequence alleles of a gene [`Sequence Ontology`_]. Even for human interpretation, these definitions are inconsistent: does the definition describe a precise sequence change or a qualitative one? In addition, all three definitions are inconsistent with the practical need for a way to describe sequence changes outside regions associated with genes.

**The computational representation of biological concepts requires translating precise biological definitions into data structures that can be used by implementers.** This translation should result in a representation of information that is consistent with conventional biological understanding, and, ideally, be able to accommodate future data as well. The resulting *computational representation* of information should also be cognizant of computational performance, the minimization of opportunities for misunderstanding, and ease of manipulating and transforming data.

Accordingly, for each term we define below, we begin by describing the term as used by biologists (**biological definition**) as available. When a term has multiple biological definitions, we explicitly choose one of them for the purposes of this specification. We then provide a computer modeling definition (**computational definition**) that reformulates the biological definition in terms of information content. We then translate each of these computational definitions into precise specifications for representing information (**logical model**). Terms are ordered "bottom-up" so that definitions depend only on previously-defined terms.

.. note:: The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in `RFC 2119`_.

******************
Primitive concepts
******************

.. glossary::

   Id
      **Biological definition:** None.

      **Computational definition:** A string that uniquely identifies a specific instance of an object within a document.

      **Implementation guidance**

      * Ids are opaque byte-strings: there are no formatting, content, or character set constraints.
      * A `FHIR Id`_, which is limited to 64 characters from a restricted character set, may be used as a VR Id.
      * Ids must correspond 1:1 to object instances: An id refers to exactly one object, and an object has only one id. Therefore, equivalence of objects implies equivalence of ids, and vice versa.
      * Implementations MAY change internal identifiers at any time. Therefore, receiving systems SHOULD NOT persist Ids from remote sources. Instead, Identifiers (below) should be used for communication between systems.
      * Ids are not locatable references. An Id may not be used to retrieve objects from remote databases. Instead, Identifiers should be used for retrieval.
      * The VR specification requires a canonical ordering (sorting) of Ids. Sorting a list of Ids MUST be performed using the C locale or, equivalently, by first encoding Ids as ASCII.


   Identifier
      **Biological definition:** An identifier for an object, such as a :term:`Sequence` or :ref:`Allele`, that is assigned by an organization or algorithm. The identifier may be used to name data in order to reference it, or to locate data in order to retrieve it from its source.

      **Computational definition:** A VR Identifier is represented using a `Compact URI (CURIE)`_, a W3C standard, with a *prefix* and *reference* that correspond to a namespace and local identifier within that namespace.

      **Information model**

      .. csv-table::
         :header: Field, Type, Label, Description
         :align: left
         :widths: 12, 9, 10, 30

         prefix, string, required, Namespace for the identifier
         reference, string, required, Unique key within prefix namespace

      **Implementation guidance**

      * CURIEs may be represented as structured data objects or as strings. The two forms are deterministically convertible as defined in the CURIE specification.
      * Within VR models, CURIEs MUST be represented as objects.
      * Implementations MAY display to users, and accept from users, CURIEs represented as strings.
      * The CURIE specification requires the use of a map from each prefix value to a URI template, shown below. URIs are generated from the CURIE map by substituting {reference} in the URI, if it exists, with the CURIE reference. This mapping provides URIs to descriptive information for a prefix rather than to structured data.

      .. csv-table::
         :header: prefix, mapped URI template
         :align: left
         :widths: 15, 85

         Ensembl, https://www.ensembl.org/Multi/Search/Results?q={reference}
         GRCh37,  https://www.ncbi.nlm.nih.gov/grc/human
         GRCh38,  https://www.ncbi.nlm.nih.gov/grc/human
         LRG,     http://ftp.ebi.ac.uk/pub/databases/lrgex/{reference}.xml
         NCBI,    https://www.ncbi.nlm.nih.gov/gquery/?term={reference}
         VR,      https://github.com/ga4gh/vr-schema

      * Implementations MAY provide additional mappings in the VR Bundle.
      * Implementations SHALL use prefix and reference, and the Identifiers derived from them, verbatim. These entities MAY NOT be modified in any way; for example, they may not be case folded or modified by the addition of prefixes or suffixes.
      * CURIEs and `FHIR Business Identifiers`_ are convertible:  For the purposes of interoperability with FHIR, the Identifier namespace and accession SHALL map, using the CURIE prefix map, to the system and value components of a FHIR Identifier.
      * It is essential for the durability of information that an Identifier refer to exactly one object for all time. (For example a Sequence reference should refer to only one Sequence.) Implementations may assume this uniqueness, but adherence is the responsibility of source databases. For this reason, databases (or versions of databases) that do not provide this guarantee SHALL NOT be used with the VR data model.


   Residue
   Base
      **Biological definition:** A residue refers to a specific `monomer`_ within the `polymeric chain`_ of a `protein`_ or `nucleic acid`_ (Source: `Wikipedia Residue page`_).

      **Computational definition:** Specific residues (i.e., molecular species) as well as categories or groupings of these ("ambiguity codes") are represented using one-letter IUPAC abbreviations.

   Interbase Coordinates
      **Biological definition:** None

      **Computational definition:** Interbase coordinates refer to the zero-width points before and after :term:`residues <Residue>`. An interval of interbase coordinates permits referring to any span, including an empty span, before, within, or after a sequence. See :ref:`interbase-coords` for more details on this design choice.

   Interval
      **TODO:** Update to include simple interval and nested interval

      **Biological definition:** None.

      **Computational definition:** Two integers that define the start and end positions of a range of residues, possibly with length zero, and specified using interbase coordinates.

      **Information model**

      .. csv-table::
         :header: Field, Type, Label, Description
         :align: left

         start, uint64, required, start position
         end, uint64, required, end position

      **Implementation guidance**

      * Implementations MUST require that 0 ≤ start ≤ end. In the case of double-stranded DNA, this constraint holds even when a feature is on the complementary strand.

      **Notes**

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

      **Examples**

      * <start, end>=<*0,0*> refers to the point with width zero before the first residue.
      * <start, end>=<*i,i+1*> refers to the *i+1th* (1-based) residue.
      * <start, end>=<*N,N*> refers to the position after the last residue for Sequence of length *N*.
      * See `Interbase Interval tests`_ in the VR-python repo for a diagram and examples.

   Sequence
      **Biological definition:** A contiguous, linear polymer of nucleic acid or amino acid residues.

      **Computational definition:** A character string of :term:`Residues <Residue>` that represents a biological sequence using the conventional sequence order (5'-to-3' for nucleic acid sequences, and amino-to-carboxyl for amino acid sequences). IUPAC ambiguity codes are permitted in Sequences.

      **Information model**

      A Sequence is a string, constrained by characters representing IUPAC nucleic acid or amino acid codes.

      **Implementation guidance**

      * Sequences MAY be empty (zero-length) strings. Empty sequences are used as the replacement Sequence for deletion Alleles.
      * Sequences MUST consist of only uppercase IUPAC abbreviations, including ambiguity codes.

      **Notes**

      * A Sequence provides a stable coordinate system by which an :ref:`Allele` may be located and interpreted.
      * A Sequence may have several roles. A “reference sequence” is any Sequence used to define an :ref:`Allele`. A Sequence that replaces another Sequence is called a “replacement sequence”.
      * In some contexts outside the VR specification, “reference sequence” may refer to a member of set of sequences that comprise a genome assembly. In the VR specification, any sequence may be a “reference sequence”, including those in a genome assembly.
      * For the purposes of representing sequence variation, it is not necessary that Sequences be “typed” (i.e., DNA, RNA, or AA).

********************
Identifiable objects
********************

**TODO:** Insert model diagram and create subdocs for Variation / Location / State / Interval


Variation
---------
**TODO:** Describe Variation

State
-----
   **TODO:** Describe State

.. _location:

Location
--------
   **Biological definition:** As used by biologists, the precision of “location” (or “locus”) varies widely; examples include chromosomal bands, named genomic features (e.g., genes, exons, or markers), or specific positions on a reference sequence.

   **Computational definition:** An identifiable position or region on a :term:`Sequence`, defined by a Sequence :term:`Id` and related positional information, which varies by location subtype.

   **Information model**

   The *SequenceLocation* subtype is described by an

   .. csv-table::
      :header: Field, Type, Label, Description
      :align: left
      :widths: 12, 9, 10, 30

      id, :term:`Id`, optional, Location Id; must be unique within document
      sequence_id, :term:`Id`, required, An id mapping to the Identifier of the external database Sequence
      interval, :term:`Interval`, required, Position of feature on reference sequence specified by sequence_id.

   **Implementation guidance**

   * For a :term:`Sequence` of length *n*:
      * 0 ≤ *interval.start* ≤ *interval.end* ≤ *n*
      * interbase coordinate 0 refers to the point before the start of the Sequence
      * interbase coordinate n refers to the point after the end of the Sequence.
   * VR requires that coordinates refer to valid Sequence. VR does not support referring to intronic positions within a transcript sequence, extrapolations beyond the ends of sequences, or other implied sequence.

   .. important:: HGVS permits variants that refer to non-existent sequence. Examples include coordinates extrapolated beyond the bounds of a transcript and intronic sequence. Such variants are not representable using VR and must be projected to a genomic reference in order to be represented.

.. _allele:

Allele
------
   **Biological definition:** One of a number of alternative forms of the same gene or same genetic locus. In the context of biological sequences, “allele” refers to a set of specific changes within a :term:`Sequence`, including sets with zero (no change), one change (a simple allele), or multiple changes (:ref:`var-sets`). In the context of VMC, allele refers to a Sequence or Sequence change with respect to a reference sequence.

   **Computational definition:** An Allele is a specific, single, and contiguous :term:`Sequence` at a :ref:`Location`. Each alternative Sequence may be empty, shorter, longer, or the same length as the interval (e.g., due to one or more indels).

   **Information model**

   .. csv-table::
      :header: Field, Type, Label, Description
      :align: left
      :widths: 12, 9, 10, 30

      id, :term:`Id`, optional, Location Id; must be unique within document
      location_id, :term:`Id`, required, An id mapping to the Identifier of the external database Sequence
      interval, :term:`Interval`, required, Position of feature on reference sequence specified by sequence_id.

   **TODO: Finish Allele**

Text Variant
------------
   **TODO: Finish Text Variant**

.. _Wikipedia: https://en.wikipedia.org/wiki/Allele
.. _ISOGG: https://isogg.org/wiki/Allele
.. _Sequence Ontology: http://www.sequenceontology.org/browser/current_svn/term/SO:0001023
.. _RFC 2119: https://www.ietf.org/rfc/rfc2119.txt
.. _FHIR Id: http://build.fhir.org/datatypes.html#id
.. _Compact URI (CURIE): https://www.w3.org/TR/curie/
.. _FHIR Business Identifiers: https://www.hl7.org/fhir/datatypes.html#identifier
.. _monomer: https://en.wikipedia.org/wiki/Monomer
.. _polymeric chain: https://en.wikipedia.org/wiki/Polymer
.. _protein: https://en.wikipedia.org/wiki/Protein
.. _nucleic acid: https://en.wikipedia.org/wiki/Nucleic_acid
.. _Wikipedia Residue page: https://en.wikipedia.org/wiki/Residue_%28chemistry%29
.. _will need to convert: https://www.biostars.org/p/84686/
.. _Interbase Interval tests: https://github.com/ga4gh/vr-python/blob/master/notebooks/appendices/Interbase%20Interval%20tests.ipynb