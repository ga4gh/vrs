Classes
@@@@@@@

.. _SequenceLocation:

SequenceLocation
$$$$$$$$$$$$$$$$

A *Sequence Location* is a specified subsequence of a reference :ref:`Sequence`.
The reference is typically a chromosome, transcript, or protein sequence.

.. include::  ../defs/vrs/SequenceLocation.rst

**Implementation Guidance**

* For a :ref:`Sequence` of length *n*:
   * 0 ≤ *interval.start* ≤ *interval.end* ≤ *n*
   * inter-residue coordinate 0 refers to the point before the start of the Sequence
   * inter-residue coordinate n refers to the point after the end of the Sequence.
* Coordinates MUST refer to a valid Sequence. VRS does not support
  referring to intronic positions within a transcript sequence,
  extrapolations beyond the ends of sequences, or other implied
  sequence.

.. important:: HGVS permits variants that refer to non-existent
               sequence. Examples include coordinates extrapolated
               beyond the bounds of a transcript and intronic
               sequence. Such variants are not representable using VRS
               and MUST be projected to a genomic reference in order
               to be represented.

**Examples**

.. parsed-literal::

    {
      "interval": {
        "end": 44908822,
        "start": 44908821,
        "type": "SimpleInterval"
      },
      "sequence_id": "ga4gh:SQ.IIB53T8CNeJJdUqzn9V_JnRtQadwWCbl",
      "type": "SequenceLocation"
    }

.. _Allele:

Allele
$$$$$$

.. note:: The terms *allele* and *variant* are often used interchangeably,
   although this use may mask subtle distinctions made by some users.
   Specifically, while *allele* connotes a specific sequence state,
   *variant* connotes a **change** between states.

   This distinction makes it awkward to use *variant* to represent an
   unchanged (refrence-agreement) state at a Sequence Location. This was
   a primary factor for choosing to use *allele* over *variant*
   when designing VRS. Read more about this design decision: Using
   :ref:`allele-not-variant`.

An allele may refer to a number of alternative forms of the same gene or same
genetic locus. In the genetics community, *allele* may also refer to a
specific haplotype. In the context of biological sequences, "allele" refers
to a distinct state of a molecule at a location.

.. include::  ../defs/vrs/Allele.rst

**Implementation Guidance**

* The :ref:`SequenceExpression` and :ref:`Location`
  subclasses respectively represent diverse kinds of
  sequence changes and mechanisms for describing the locations of
  those changes, including varying levels of precision of sequence
  location and categories of sequence changes.
* Implementations MUST enforce values interval.end ≤ sequence_length
  when the Sequence length is known.
* Alleles are equal only if the component fields are equal: at the
  same location and with the same state.
* Alleles MAY have multiple related representations on the same
  Sequence type due to normalization differences.
* Implementations SHOULD normalize Alleles using :ref:`fully-justified
  normalization <normalization>` whenever possible to facilitate
  comparisons of variation in regions of representational ambiguity.
* Implementations SHOULD preferentially represent Alleles using
  :ref:`LiteralSequenceExpression`, however there are cases where use
  of other :ref:`SequenceExpression` classes is most appropriate; see
  :ref:`using-sequence-expressions` for guidance.
* When the alternate Sequence is the same length as the interval, the
  lengths of the reference Sequence and imputed Sequence are the
  same. (Here, imputed sequence means the sequence derived by applying
  the Allele to the reference sequence.) When the replacement Sequence
  is shorter than the length of the interval, the imputed Sequence is
  shorter than the reference Sequence, and conversely for replacements
  that are larger than the interval.
* When the state is a :ref:`LiteralSequenceExpression` of ``""`` (the empty
  string), the Allele refers to a deletion at this location.
* The Allele entity is based on Sequence and is intended to be used
  for intragenic and extragenic variation. Alleles are not explicitly
  associated with genes or other features.
* Biologically, referring to Alleles is typically meaningful only in
  the context of empirical alternatives. For modelling purposes,
  Alleles MAY exist as a result of biological observation or
  computational simulation, i.e., virtual Alleles.
* "Single, contiguous" refers the representation of the Allele, not
  the biological mechanism by which it was created. For instance, two
  non-adjacent single residue Alleles could be represented by a single
  contiguous multi-residue Allele.
* When a trait has a known genetic basis, it is typically represented
  computationally as an association with an Allele.
* This specification's definition of Allele applies to any
  :ref:`Location`, including locations on RNA or protein
  :ref:`Sequence`.

**Examples**

An Allele correponding to rs7412 C>T on GRCh38:

.. parsed-literal::

    {
      "location": {
        "interval": {
          "end": {
            "type": "Number",
            "value": 44908822
          },
          "start": {
            "type": "Number",
            "value": 44908821
          },
          "type": "SequenceInterval"
        },
        "sequence_id": "ga4gh:SQ.IIB53T8CNeJJdUqzn9V_JnRtQadwWCbl",
        "type": "SequenceLocation"
      },
      "state": {
        "sequence": "T",
        "type": "SequenceState"
      },
      "type": "Allele"
    }


**Sources**

* `ISOGG: Allele <http://isogg.org/wiki/Allele>`__ — An allele is one
  of two or more forms of the DNA sequence of a particular gene.
* `SequenceOntology: allele (SO:0001023)
  <http://www.sequenceontology.org/browser/current_svn/term/SO:0001023>`__
  — An allele is one of a set of coexisting sequence variants of a
  gene.
* `SequenceOntology: sequence_alteration (SO:0001059)
  <http://www.sequenceontology.org/browser/current_svn/term/SO:0001059>`__
  — A sequence_alteration is a sequence_feature whose extent is the
  deviation from another sequence.
* `SequenceOntology: sequence_variant (SO:0001060)
  <http://www.sequenceontology.org/browser/current_svn/term/SO:0001060>`__
  — A sequence_variant is a non exact copy of a sequence_feature or
  genome exhibiting one or more sequence_alteration.
* `Wikipedia: Allele <https://en.wikipedia.org/wiki/Allele>`__ — One
  of a number of alternative forms of the same gene or same genetic
  locus.
* `GenotypeOntology: Allele (GENO:0000512)
  <http://purl.obolibrary.org/obo/GENO_0000512>`__ - A sequence
  feature representing one of a set of coexisting sequences at a
  particular genomic locus. An allele can represent a 'reference' or
  'variant' sequence at a locus.


.. _Haplotype:

Haplotype
$$$$$$$$$

Haplotypes are a specific combination of Alleles that are *in-cis*: occurring
on the same physical molecule. Haplotypes are commonly described with respect
to locations on a gene, a set of nearby genes, or other physically proximal
genetic markers that tend to be transmitted together.

.. include::  ../defs/vrs/Haplotype.rst

**Implementation Guidance**

* Haplotypes are an assertion of Alleles known to occur "in cis" or
  "in phase" with each other.
* All Alleles in a Haplotype MUST be defined on the same reference
  sequence or chromosome.
* Alleles within a Haplotype MUST not overlap ("overlap" is defined in
  Interval).
* The locations of Alleles within the Haplotype MUST be interpreted
  independently.  Alleles that create a net insertion or deletion of
  sequence MUST NOT change the location of "downstream" Alleles.
* The `members` attribute is required and MUST contain at least two
  Alleles.

**Sources**

* `ISOGG: Haplotype <https://isogg.org/wiki/Haplotype>`__ — A haplotype
  is a combination of alleles (DNA sequences) at different places
  (loci) on the chromosome that are transmitted together. A haplotype
  may be one locus, several loci, or an entire chromosome depending on
  the number of recombination events that have occurred between a
  given set of loci.
* `SequenceOntology: haplotype (SO:0001024)
  <http://www.sequenceontology.org/browser/current_release/term/SO:0001024>`__
  — A haplotype is one of a set of coexisting sequence variants of a
  haplotype block.
* `GENO: Haplotype (GENO:0000871)
  <http://www.ontobee.org/ontology/GENO?iri=http://purl.obolibrary.org/obo/GENO_0000871>`__ -
  A set of two or more sequence alterations on the same chromosomal
  strand that tend to be transmitted together.

**Examples**

An APOE ε2 Haplotype with inline Alleles:

.. parsed-literal::

    {
      "members": [
        {
          "location": {
            "interval": {
              "end": {
                "type": "Number",
                "value": 44908822
              },
              "start": {
                "type": "Number",
                "value": 44908821
              },
              "type": "SequenceInterval"
            },
            "sequence_id": "ga4gh:SQ.IIB53T8CNeJJdUqzn9V_JnRtQadwWCbl",
            "type": "SequenceLocation"
          },
          "state": {
            "sequence": "C",
            "type": "LiteralSequenceExpression"
          },
          "type": "Allele"
        },
        {
          "location": {
            "interval": {
              "end": {
                "type": "Number",
                "value": 44908684
              },
              "start": {
                "type": "Number",
                "value": 44908683
              },
              "type": "SequenceInterval"
            },
            "sequence_id": "ga4gh:SQ.IIB53T8CNeJJdUqzn9V_JnRtQadwWCbl",
            "type": "SequenceLocation"
          },
          "state": {
            "sequence": "C",
            "type": "LiteralSequenceExpression"
          },
          "type": "Allele"
        }
      ],
      "type": "Haplotype"
    }

The same APOE ε2 Haplotype with referenced Alleles:
  
.. parsed-literal::

    {
      "members": [
        "ga4gh:VA.-kUJh47Pu24Y3Wdsk1rXEDKsXWNY-68x",
        "ga4gh:VA.Z_rYRxpUvwqCLsCBO3YLl70o2uf9_Op1"
      ],
      "type": "Haplotype"
    }

The GA4GH computed identifier for these Haplotypes is
``ga4gh:VH.i8owCOBHIlRCPtcw_WzRFNTunwJRy99-``, regardless of whether the
Variation objects are inlined or referenced, and regardless of
order. See :ref:`computed-identifiers` for more information.


.. _CopyNumber:
.. _CopyNumberCount:

CopyNumberCount
$$$$$$$$$$$$$$$

*Copy Number Count* captures the integral copies of a molecule within a
genome. Copy Number Count has conflated meanings in the
genomics community, and can mean either (or both) the notion of copy
number *in a genome* or copy number *on a molecule*. VRS separates
the concerns of these two types of statements; this concept is a type
of :ref:`SystemicVariation` and so describes the number of copies in a
genome. The related :ref:`MolecularVariation` concept can be expressed
as an :ref:`Allele` with a :ref:`RepeatedSequenceExpression`.

.. include::  ../defs/vrs/CopyNumberCount.rst

**Examples**

Two, three, or four total copies of BRCA1:

.. parsed-literal::

    {
      "copies": {
        "comparator": ">=",
        "type": "IndefiniteRange",
        "value": 3
      },
      "subject": {
        "gene_id": "ncbigene:348",
        "type": "Gene"
      },
      "type": "CopyNumberCount"
    }

.. _CopyNumberChange:

CopyNumberChange
$$$$$$$$$$$$$$$$

*Copy Number Change* captures a categorization of copies
of a molecule within a system, relative to a baseline. These types
of Variation are common outputs from CNV callers, particularly in the
somatic domain where integral :ref:`CopyNumberCount` are difficult to
estimate and less useful in practice than relative statements. Somatic CNV
callers typically express changes as relative statements, and many HGVS
expressions submitted to express copy number variation are interpreted to be
relative copy changes.

.. include::  ../defs/vrs/CopyNumberChange.rst

**Examples**

Low-level copy gain of BRCA1:

.. parsed-literal::

    {
      "copy_change": "efo:0030071", # low-level gain
      "subject": {
        "gene_id": "ncbigene:348",          # BRCA1 gene
        "type": "Gene"
      },
      "type": "CopyNumberChange"
    }

.. _genotype:

Genotype
$$$$$$$$

A *genotype* is a representation of the variants present at a given genomic locus, and may be referred
to either by individual nucleotide representations (e.g. GT representation in VCF files) or symbolically
(e.g. A/B/O blood type reporting). To support these use cases, VRS genotypes enable representation of
genotypes using either :ref:`Allele` objects (as commonly done in VCF records) or larger :ref:`Haplotype`
objects (which would otherwise be represented using symbolic shorthand).

.. include::  ../defs/vrs/Genotype.rst

**Implementation guidance**

* Haplotypes or Alleles in :ref:`GenotypeMember` objects MAY occur at different locations or on
  different reference sequences. For example, an individual may have haplotypes on two
  population-specific references.

**Notes**

* The term "genotype" has two, related definitions in common use. The
  narrower definition is a set of alleles observed at a single
  location and often with a ploidy of two, such as a pair of single residue
  variants on an autosome. The broader, generalized definition is a
  set of alleles at multiple locations and/or with ploidy other than
  two. VRS Genotype entity is based on this broader definition.
* The term "diplotype" is often used to refer to two in-trans haplotypes at a locus.
  VRS Genotype entity subsumes the conventional definition of diplotype, though
  it describes no explicit in-trans phase relationship. Therefore,
  VRS does not include an explicit entity for diplotypes. See :ref:`this note
  <genotypes-represent-haplotypes-with-arbitrary-ploidy>` for a discussion.
* VRS makes no assumptions about ploidy of an organism or individual nor any
  polysomy affecting a locus. The `genotype.count` attribute explicitly captures the total
  count of molecules associated with a genomic locus represented by the Genotype.
* In diploid organisms, there are typically two instances of each autosomal chromosome,
  and therefore two instances of sequence at a particular locus. Thus, Genotypes will
  often list two GenotypeMembers each based on a distinct Haplotype or Allele. In the case
  of haploid chromosomes or haploinsufficiency, the Genotype consists of a single GenotypeMember.
* A specific (heterozygous) diplotype SHOULD be represented as a Genotype of two GenotypeMember
  instances each containing a constituent :ref:`Haplotype`. A homozygous diplotype SHOULD be
  represented as a Genotype of one constituent GenotypeMember (with `GenotypeMember.count=2`).
* A consequence of the computational definition is that in-cis Haplotypes at overlapping or
  adjacent intervals MUST be merged into a single Haplotype for the same Genotype.
* A `GenotypeMember.variation` value MUST be unique among Genotype Members within a Genotype.
  When more than one Genotype Member would have the same `variation` value (e.g. in the case
  of a homozygous variant), this would be represented as a Genotype Value with a corresponding
  `count` (i.e. for a diploid homozygous variant, `GenotypeMember.count = 2`).
* The rationale for permitting Genotypes with Haplotypes defined on different reference
  sequences is to enable the accurate representation of segments of DNA with the most
  appropriate population-specific reference sequence.
* Deletion of sequence at locus would be represented by the presence of Alleles of deleted
  sequence, not absence of Alleles; therefore Genotypes MAY NOT have count < 1.

**Sources**

SO: `Genotype (SO:0001027)
<http://www.sequenceontology.org/browser/current_svn/term/SO:0001027>`__
— A genotype is a variant genome, complete or incomplete.

.. _genotypes-represent-haplotypes-with-arbitrary-ploidy:

.. note::
     VRS defines Genotypes using a list of GenotypeMembers defined by
     Haplotypes or Alleles. In essence, Haplotypes and Genotypes represent
     two distinct dimensions of containment: Haplotypes represent the "in
     phase" relationship of Alleles while Genotypes represents sets of
     Haplotypes of arbitrary ploidy.

     There are two important consequences of these definitions: There is no
     single-location Genotype. Users of SNP data will be familiar with
     representations like rs7412 C/C, which indicates the diploid state at
     a position. In VRS, this is merely a special case of a
     Genotype with one GenotypeMember, defined by a single Allele with
     two copies.  VRS does not define a diplotype class. A diplotype
     is a special case of a VRS Genotype with count = 2. In practice, software
     data types that assume a ploidy of 2 make it very difficult to represent haploid
     states, copy number loss, and copy number gain, all of which occur
     when representing human data. In addition, inferred ploidy = 2 makes
     software incompatible with organisms with other ploidy. VRS
     requires explicit definition of the count of molecules associated with
     a genomic locus using the `count` attribute, though this count may be inexact
     (e.g. a :ref:`DefiniteRange` or :ref:`IndefiniteRange`).