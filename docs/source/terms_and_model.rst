Terminology & Information Model
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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
translating precise biological definitions into information models and
data structures that may be used in software.** This translation
should result in a representation of information that is consistent
with conventional biological understanding and, ideally, be able to
accommodate future data as well. The resulting *computational
representation* of information should also be cognizant of
computational performance, the minimization of opportunities for
misunderstanding, and ease of manipulating and transforming data.

Accordingly, for each term we define below, we begin by describing the
term as used by the genetics and/or bioinformatics communities as
available. When a term has multiple such definitions, we
explicitly choose one of them for the purposes of computational
modelling. We then define the **computational definition** that
reformulates the community definition in terms of information content.
Finally, we translate each of these computational definitions into precise
specifications for the (**information model**). Terms are ordered
"bottom-up" so that definitions depend only on previously-defined terms.

.. note:: The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
          NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and
          "OPTIONAL" in this document are to be interpreted as
          described in `RFC 2119`_.


Information Model Principles
@@@@@@@@@@@@@@@@@@@@@@@@@@@@

* **VRS objects are minimal** `value objects
  <https://en.wikipedia.org/wiki/Value_object>`_. Two objects are
  considered equal if and only if their respective attributes are
  equal.  As value objects, VRS objects are used as primitive types
  and MUST NOT be used as containers for related data, such as primary
  database accessions, representations in particular formats, or links
  to external data.  Instead, related data should be associated with
  VRS objects through identifiers.  See :ref:`computed-identifiers`.

* **VRS uses polymorphism.** VRS uses polymorphism extensively in
  order to provide a coherent top-down structure for variation while
  enabling precise models for variation data.  For example, Allele is
  a kind of Variation, SequenceLocation is a kind of Location, and
  SequenceState is a kind of State.  See :ref:`future-plans` for the
  roadmap of VRS data classes and relationships.  All VRS objects
  contain a ``type`` attribute, which is used to discriminate
  polymorphic objects.

* **Error handling is intentionally unspecified and delegated to
  implementation.**  VRS provides foundational data types that
  enable significant flexibility.  Except where required by this
  specification, implementations may choose whether and how to
  validate data.  For example, implementations MAY choose to validate
  that particular combinations of objects are compatible, but such
  validation is not required.

* **VRS uses** `snake_case
  <https://simple.wikipedia.org/wiki/Snake_case>`__ **to represent
  compound words.** Although the schema is currently JSON-based (which
  would typically use camelCase), VRS itself is intended to be neutral
  with respect to languages and database.

* **Optional attributes start with an underscore.** Optional
  attributes are not part of the value object.  Such attributes are
  not considered when evaluating equality or creating computed
  identifiers.  The ``_id`` attribute is available to identifiable
  objects, and MAY be used by an implementation to store the
  identifier for a VRS object.  If used, the stored ``_id`` element
  MUST be a `CURIE`_. If used for creating a :ref:`truncated-digest`
  for parent objects, the stored element must be a :ref:`GA4GH
  Computed Identifier <identify>`.  Implementations MUST ignore
  attributes beginning with an underscore and they SHOULD NOT transmit
  objects containing them.


.. _Variation:

Variation
@@@@@@@@@

In the genetics community, variation is often used to mean *sequence*
variation, describing the differences observed in DNA or AA bases among
individuals, and typically with respect to a common reference sequence.

In VRS, the Variation class is the conceptual root of all types of biomolecular
variation, and the *Variation* abstract class is the top-level object in
the :ref:`vr-schema-diagram`. Variation types are broadly categorized as
:ref:`MolecularVariation`, :ref:`SystemicVariation`, or a :ref:`utility
subclass <utilityvariation>`. Types of variation are widely varied, and
there are several :ref:`planned-variation` currently under consideration
to capture this diversity.

.. include:: defs/Variation.rst

.. _MolecularVariation:

Molecular Variation
###################

.. include:: defs/MolecularVariation.rst

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

.. include:: defs/Allele.rst

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

.. include:: defs/Haplotype.rst

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


.. _SystemicVariation:

Systemic Variation
##################

.. include:: defs/SystemicVariation.rst

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

.. include:: defs/CopyNumberCount.rst

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

.. include:: defs/CopyNumberChange.rst

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

.. include:: defs/Genotype.rst

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

.. _UtilityVariation:

Utility Variation
#################

.. include:: defs/UtilityVariation.rst

.. _Text:

Text
$$$$

A free-text description of variation that is intended for
interpretation by humans.

.. important:: **Text variation should be used sparingly.** The Text
               type is provided as an option of last resort for
               systems that need to represent human-readable
               descriptions of complex genetic phenomena or variation
               for which VRS does not yet have a data type.
               Structured data types should be preferred over Text.

.. include:: defs/Text.rst

**Implementation Guidance**

* An implementation MUST represent Variation with subclasses other
  than Text if possible.
* Because the Text type can be easily abused, implementations are NOT
  REQUIRED to provide it.  If it is provided, implementations SHOULD
  consider applying access controls.
* Implementations SHOULD upgrade Text variation to structured data
  types when available. A future version of VRS will provide
  additional guidance regarding upgrade mechanisms.
* Additional Variation subclasses are continually under
  consideration. Please open a `GitHub issue`_ if you would like to
  propose a Variation subclass to cover a needed variation
  representation.

.. _GitHub issue: https://github.com/ga4gh/vrs/issues

**Examples**

.. parsed-literal::

    {
      "definition": "MSI High",
      "type": "Text"
    }

.. _VariationSet:

VariationSet
$$$$$$$$$$$$

Sets of variation are used widely, such as sets of variants in dbSNP
or ClinVar that might be related by function.

.. include:: defs/VariationSet.rst

**Implementation Guidance**

* The VariationSet identifier MAY be computed as described in
  :ref:`computed-identifiers`, in which case the identifier
  effectively refers to a static set because a different set of
  members would generate a different identifier.
* `members` may be specified as Variation objects or CURIE
  identifiers.
* CURIEs MAY refer to entities outside the `ga4gh` namespace.
  However, objects that use non-`ga4gh` identifiers MAY NOT use the
  :ref:`computed-identifiers` mechanism.
* VariationSet identifiers computed using the GA4GH
  :ref:`computed-identifiers` process do *not* depend on whether the
  Variation objects are inlined or referenced, and do *not* depend on
  the order of members.
* Elements of `members` must be subclasses of Variation, which permits
  sets to be nested.
* Recursive sets are not meaningful and are not supported.
* VariationSets may be empty.

**Examples**


Example VariationSet with inline Alleles:

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
      "type": "VariationSet"
    }


The same VariationSet with referenced Alleles:

.. parsed-literal::

    {
      "members": [
        "ga4gh:VA.-kUJh47Pu24Y3Wdsk1rXEDKsXWNY-68x",
        "ga4gh:VA.Z_rYRxpUvwqCLsCBO3YLl70o2uf9_Op1"
      ],
      "type": "VariationSet"
    }


The GA4GH computed identifier for these sets is
``ga4gh:VS.QLQXSNSIFlqNYWmQbw-YkfmexPi4NeDE``, regardless of the whether
the Variation objects are inlined or referenced, and regardless of
order. See :ref:`computed-identifiers` for more information.


Locations and Intervals
@@@@@@@@@@@@@@@@@@@@@@@


.. _Location:

Location
########

As used by biologists, the precision of "location" (or "locus") varies
widely, ranging from precise start and end numerical coordinates
defining a Location, to bounded regions of a sequence, to conceptual
references to named genomic features (e.g., chromosomal bands, genes,
exons) as proxies for the Locations on an implied reference sequence.

The most common and concrete Location is a :ref:`SequenceLocation`, i.e.,
a Location based on a named sequence and an Interval on that sequence.
Another common Location is a :ref:`ChromosomeLocation`, specifying a
location from cytogenetic coordinates of stained metaphase chromosomes.
Additional :ref:`planned-locations` may also be conceptual or symbolic locations,
such as a cytoband region or a gene. Any of these may be used as the
Location for Variation.

.. include:: defs/Location.rst

**Implementation Guidance**

* Location refers to a position.  Although it MAY imply a sequence,
  the two concepts are not interchangeable, especially when the
  location is non-specific (e.g., specified by an :ref:`IndefiniteRange`).
  To represent a sequence derived from a Location, see
  :ref:`DerivedSequenceExpression`.


.. _ChromosomeLocation:

ChromosomeLocation
$$$$$$$$$$$$$$$$$$

Chromosomal locations based on named features, including named landmarks,
cytobands, and regions observed from chromosomal staining techniques.

.. include:: defs/ChromosomeLocation.rst

**Implementation Guidance**

* ChromosomeLocation is intended to enable the representation of
  cytogenetic results from karyotyping or low-resolution molecular
  methods, particularly those found in older scientific literature.
  Precise :ref:`SequenceLocation` should be preferred when
  nucleotide-scale location is known.
* `species` is specified using the NCBI taxonomy.  The CURIE prefix
  MUST be "taxonomy", corresponding to the `NCBI taxonomy prefix at
  identifiers.org
  <https://registry.identifiers.org/registry/taxonomy>`__, and the
  CURIE reference MUST be an NCBI taxonomy identifier (e.g., 9606 for
  Homo sapiens).
* ChromosomeLocation is intended primarily for human chromosomes.
  Support for other species is possible and will be considered based
  on community feedback.
* `chromosome` is an archetypal chromosome name. Valid values for, and
  the syntactic structure of, `chromosome` depends on the species.
  `chromosome` MUST be an official sequence name from `NCBI Assembly
  <https://www.ncbi.nlm.nih.gov/assembly>`__.  For humans, valid
  chromosome names are 1..22, X, Y (case-sensitive).  **NOTE: A `chr`
  prefix is NOT part of the chromosome and MUST NOT be included.**
* `interval` refers to a contiguous region specified named markers,
  which are presumed to exist on the specified chromosome.  See
  :ref:`CytobandInterval` for additional information.
* The conversion of ChromosomeLocation instances to SequenceLocation
  instances is out-of-scope for VRS.  When converting `start` and
  `end` to SequenceLocations, the positions MUST be interpreted as
  inclusive ranges that cover the maximal extent of the region.
* Data for converting cytogenetic bands to precise sequence
  coordinates are available at `NCBI GDP
  <https://ftp.ncbi.nlm.nih.gov/pub/gdp/>`__, `UCSC GRCh37 (hg19)
  <http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/cytoBand.txt.gz>`__,
  `UCSC GRCh38 (hg38)
  <http://hgdownload.cse.ucsc.edu/goldenPath/hg38/database/cytoBand.txt.gz>`__,
  and `bioutils (Python)
  <https://bioutils.readthedocs.io/en/stable/reference/bioutils.cytobands.html>`__.
* See also the rationale
  for :ref:`dd-not-using-external-chromosome-declarations`.


**Examples**

.. parsed-literal::

    {
      "chr": "19",
      "interval": {
        "end": "q13.32",
        "start": "q13.32",
        "type": "CytobandInterval"
      },
      "species_id": "taxonomy:9606",
      "type": "ChromosomeLocation"
    }


.. _SequenceLocation:

SequenceLocation
$$$$$$$$$$$$$$$$

A *Sequence Location* is a specified subsequence of a reference :ref:`Sequence`.
The reference is typically a chromosome, transcript, or protein sequence.

.. include:: defs/SequenceLocation.rst

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

.. _Interval:
.. _SequenceInterval:

SequenceInterval
################

SequenceInterval is intended to be compatible with a "region" in Sequence Ontology
(`SO:0000001 <http://www.sequenceontology.org/browser/current_svn/term/SO:0000001>`_),
with the exception that the GA4GH VRS SequenceInterval may be zero-width. The SO
definition of region has an "extent greater than zero".

.. include:: defs/SequenceInterval.rst

.. sidebar:: VRS Uses Inter-residue Coordinates

   **GA4GH VRS uses inter-residue coordinates when referring to spans of
   sequence.**

   Inter-residue coordinates refer to the zero-width points before and
   after :ref:`residues <Residue>`. An interval of inter-residue
   coordinates permits referring to any span, including an empty span,
   before, within, or after a sequence. See
   :ref:`inter-residue-coordinates-design` for more details on this design
   choice.  Inter-residue coordinates are always zero-based.


**Sources**

* `Interbase Coordinates (Chado documentation) <http://gmod.org/wiki/Introduction_to_Chado#Interbase_Coordinates>`__
* `SequenceOntology: sequence_feature (SO:0000110) <http://www.sequenceontology.org/miso/current_svn/term/SO:0000110>`__ — Any extent of continuous biological sequence.
* `SequenceOntology: region (SO:0000001) <http://www.sequenceontology.org/miso/current_svn/term/SO:0000001>`__ — A sequence_feature with an extent greater than zero. A nucleotide region is composed of bases and a polypeptide region is composed of amino acids.

**Examples**

.. parsed-literal::

    {
      "end": {
        "type": "Number",
        "value": 44908822
      },
      "start": {
        "type": "Number",
        "value": 44908821
      },
      "type": "SequenceInterval"
    }

.. _CytobandInterval:

CytobandInterval
################

.. important::

   VRS currently supports only human cytobands and
   cytoband intervals. Implementers wishing to use VRS for other
   cytogenetic systems are encouraged to open a `GitHub issue`_.

Cytobands refer to regions of chromosomes that are identified by
visible patterns on stained metaphase chromosomes.  They provide a
convenient, memorable, and low-resolution shorthand for chromosomal
segments.

.. include:: defs/CytobandInterval.rst

**Implementation Guidance**

* When using :ref:`CytobandInterval` to refer to human cytogentic
  bands, the following conventions MUST be used. Bands are denoted by
  the arm ("p" or "q") and position (e.g., "22", "22.3", or the symbolic
  values "cen" or "ter") per ISCN conventions [1]_. These conventions
  identify cytobands in order from the centromere towards the telomeres.
  In VRS, we order cytoband coordinates in the p-ter → cen → q-ter
  orientation, analogous to sequence coordinates. This has the
  consequence that bands on the p-arm are represented in descending
  numerical order when selecting cytobands for `start` and `end`.

**Examples**

.. parsed-literal::

    {
      "end": "q13.32",
      "start": "q13.32",
      "type": "CytobandInterval"
    }


.. _SequenceExpression:

Sequence Expression
@@@@@@@@@@@@@@@@@@@

VRS provides several syntaxes for expressing a sequence,
collectively referred to as *Sequence Expressions*. They are:

* :ref:`LiteralSequenceExpression`: An explicit :ref:`Sequence`.
* :ref:`DerivedSequenceExpression`: A sequence that is derived from a
  :ref:`Sequencelocation`.
* :ref:`RepeatedSequenceExpression`: A description of a repeating :ref:`Sequence`.

Some SequenceExpression instances may appear to resolve to the same
sequence, but are intended to be semantically distinct. There MAY be
reasons to select or enforce one form over another that SHOULD be
managed by implementations. See discussion on :ref:`equivalence`.

.. include:: defs/SequenceExpression.rst

.. _LiteralSequenceExpression:

LiteralSequenceExpression
#########################

A LiteralSequenceExpression "wraps" a string representation of a
sequence for parallelism with other SequenceExpressions.

.. include:: defs/LiteralSequenceExpression.rst

**Examples**

.. parsed-literal::

    {
      "sequence": "ACGT",
      "type": "LiteralSequenceExpression"
    }


.. _DerivedSequenceExpression:

DerivedSequenceExpression
#########################

Certain mechanisms of variation result from relocating and
transforming sequence from another location in the genome.
A *derived sequence* is a mechanism for expressing (typically
large) reference subsequences specified by a :ref:`SequenceLocation`.

.. include:: defs/DerivedSequenceExpression.rst

**Examples**

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
      "reverse_complement": false,
      "type": "DerivedSequenceExpression"
    }

    
.. _RepeatedSequenceExpression:

RepeatedSequenceExpression
##########################

*Repeated Sequence* is a class of sequence expression where a specified
subsequence is repeated multiple times in tandem. Microsatellites are an
example of a common class of repeated sequence, but repeated sequence can
also be used to describe larger subsequence repeats, up to and including
large-scale tandem duplications.

.. include:: defs/RepeatedSequenceExpression.rst

**Examples**

.. parsed-literal::

    {
      "count": {
        "comparator": ">=",
        "type": "IndefiniteRange",
        "value": 6
      },
      "seq_expr": {
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
        "reverse_complement": false,
        "type": "DerivedSequenceExpression"
      },
      "type": "RepeatedSequenceExpression"
    }

.. _ComposedSequenceExpression:

ComposedSequenceExpression
##########################

*Composed Sequence* is a class of sequence expression composed of other sequence expression
types. It is useful, for example, when representing multiple repeating subunits that occur
in tandem, such as in the description of *PABPN1* alleles in the diagnosis of
oculopharyngeal muscular dystrophy (OPMD).

.. include:: defs/ComposedSequenceExpression.rst

**Examples**

.. parsed-literal::

    {
      "type": "Allele",
      "location": {
        "type": "SequenceLocation",
        "sequence_id": "ga4gh:SQ.sH4gymNtL5nxNdTE3evfxzZa4dg3fqDz",
        "interval": {
          "type": "SequenceInterval",
          "start": { "type": "Number", "value": 3  },
          "end":   { "type": "Number", "value": 33 }
        }
      },
      "state": {
        "type": "ComposedSequenceExpression",
        "components": [
          {
            "type": "RepeatedSequenceExpression",
            "seq_expr": { "type": "LiteralSequenceExpression", "sequence": "GCG" },
            "count": { "type": "Number", "value": 11 }
          },
          {
            "type": "RepeatedSequenceExpression",
            "seq_expr": { "type": "LiteralSequenceExpression", "sequence": "GCA" },
            "count": { "type": "Number", "value": 3 }
          },
          {
            "type": "RepeatedSequenceExpression",
            "seq_expr": { "type": "LiteralSequenceExpression", "sequence": "GCG" },
            "count": { "type": "Number", "value": 1 }
          }
        ]
      }
    }

.. _Feature:

Feature
@@@@@@@

.. include:: defs/Feature.rst

.. _Gene:

Gene
####

A gene is a basic and fundamental unit of heritability. Genes are
functional regions of heritable DNA or RNA that include transcript
coding regions, regulatory elements, and other functional sequence
domains. Because of the complex nature of these many components
comprising a gene, the interpretation of a gene depends on context.

.. include:: defs/Gene.rst

**Implementation guidance**

* Gene symbols (e.g., "BRCA1") are unreliable keys.  Implementations
  MUST NOT use a gene symbol to define a Gene.
* A gene is specific to a species.  Gene orthologs have distinct
  records in the recommended databases.  For example, the BRCA1 gene
  in humans and the Brca1 gene in mouse are orthologs and have
  distinct records in the recommended gene databases.
* Implementations MUST use authoritative gene namespaces available from
  identifiers.org whenever possible.  Examples include:

    * `hgnc <https://registry.identifiers.org/registry/hgnc>`__
    * `ncbigene <https://registry.identifiers.org/registry/ncbigene>`__
    * `ensembl <https://registry.identifiers.org/registry/ensembl>`__
    * `vgnc <https://registry.identifiers.org/registry/vgnc>`__
    * `mgi <https://registry.identifiers.org/registry/mgi>`__
* The `hgnc` namespace is RECOMMENDED for human variation in order to
  improve interoperability.  When using the ``hgnc`` namespace, the
  optional "HGNC:" prefix MUST NOT be used.
* Gene MAY be converted to one or more :ref:`Locations <Location>`
  using external data. The source of such data and mechanism for
  implementation is not defined by this specification.
* See discussion on :ref:`equivalence`.

**Examples**

The following examples all refer to the human APOE gene:

.. parsed-literal::

   {
     'gene_id': 'ncbigene:613',
     'type': 'Gene'
   }


**Sources**

* `SequenceOntology: gene (SO:0000704)
  <http://www.sequenceontology.org/browser/current_release/term/SO:0000704>`__
  — A region (or regions) that includes all of the sequence elements
  necessary to encode a functional transcript. A gene may include
  regulatory regions, transcribed regions and/or other functional
  sequence regions.


Basic Types
@@@@@@@@@@@

Basic types are data structures that represent general concepts and
that may be applicable in multiple parts of VRS.

.. _Number:

Number
######

.. include:: defs/Number.rst

**Examples**

.. parsed-literal::

    {
      "type": "Number",
      "value": 55
    }

.. _DefiniteRange:

DefiniteRange
###############

.. include:: defs/DefiniteRange.rst

**Examples**

.. parsed-literal::

    {
      "max": 33,
      "min": 22,
      "type": "DefiniteRange"
    }


.. _IndefiniteRange:

IndefiniteRange
################

.. include:: defs/IndefiniteRange.rst

**Examples**

This value is equivalent to the concept of "equal to or greater than
22":

.. parsed-literal::

    {
      "comparator": ">=",
      "type": "IndefiniteRange",
      "value": 22
    }

.. _genotypemember:

GenotypeMember
##############

.. include:: defs/GenotypeMember.rst

Primitives
@@@@@@@@@@

Primitives represent simple values with syntactic or other
constraints. They enable correctness for values stored in VRS.

.. _CURIE:

CURIE
#####

.. include:: defs/CURIE.rst

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

.. _HumanCytoband:

HumanCytoband
#############

Cytobands are any of a pattern of stained bands, formed on chromosomes of
cells undergoing metaphase, that serve to identify particular chromosomes.
Human cytobands are predominantly specified by the *International System
for Human Cytogenomic Nomenclature* (ISCN) [1]_.

.. include:: defs/HumanCytoband.rst

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

.. include:: defs/Residue.rst

.. _Sequence:

Sequence
########

A *sequence* is a character string representation of a contiguous,
linear polymer of nucleic acid or amino acid :ref:`Residues <Residue>`.
Sequences are the prevalent representation of these polymers,
particularly in the domain of variant representation.

.. include:: defs/Sequence.rst

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



.. _deprecations:

Deprecated and Obsolete Classes
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. _SimpleInterval:

SimpleInterval
##############

.. warning::

   DEPRECATED. Use :ref:`SequenceInterval` instead.
   SimpleInterval will be removed in VRS 2.0.

.. include:: defs/SimpleInterval.rst

**Implementation Guidance**

* Implementations MUST enforce values 0 ≤ start ≤ end. In the case of
  double-stranded DNA, this constraint holds even when a feature is on
  the complementary strand.
* VRS uses Inter-residue coordinates because they provide conceptual
  consistency that is not possible with residue-based systems (see
  :ref:`rationale <inter-residue-coordinates-design>`). Implementations
  will need to convert between inter-residue and 1-based inclusive
  residue coordinates familiar to most human users.
* Inter-residue coordinates start at 0 (zero).
* The length of an interval is *end - start*.
* An interval in which start == end is a zero width point between two residues.
* An interval of length == 1 MAY be colloquially referred to as a position.
* Two intervals are *equal* if the their start and end coordinates are equal.
* Two intervals *intersect* if the start or end coordinate of one is
  strictly between the start and end coordinates of the other. That
  is, if:

   * b.start < a.start < b.end OR
   * b.start < a.end < b.end OR
   * a.start < b.start < a.end OR
   * a.start < b.end < a.end
* Two intervals a and b *coincide* if they intersect or if they are
  equal (the equality condition is REQUIRED to handle the case of two
  identical zero-width SimpleIntervals).
* <start, end>=<*0,0*> refers to the point with width zero before the first residue.
* <start, end>=<*i,i+1*> refers to the *i+1th* (1-based) residue.
* <start, end>=<*N,N*> refers to the position after the last residue for Sequence of length *N*.
* See example notebooks in |vrs-python|.

**Examples**

.. parsed-literal::

    {
      "end": 44908822,
      "start": 44908821,
      "type": "SimpleInterval"
    }

.. _SequenceState:

SequenceState
#############

.. warning::

   DEPRECATED. Use :ref:`LiteralSequenceExpression` instead.
   SequenceState will be removed in VRS 2.0.

.. deprecated:: 1.2

.. include:: defs/SequenceState.rst

**Examples**

.. parsed-literal::

    {
      "sequence": "T",
      "type": "SequenceState"
    }


.. _State:

State
#####

.. warning::

   OBSOLETE. State was an abstract class that was intended for future
   growth. It was replaced by SequenceExpressions, which subsumes the
   functionality envisioned for State.  Because State was abstract,
   and therefore purely an internal concept, it was made obsolete at
   the same time that SequenceState was deprecated.

.. deprecated:: 1.2

**Computational Definition**

*State* objects are one of two primary components specifying a VRS
:ref:`Allele` (in addition to :ref:`Location`), and the designated
components for representing change (or non-change) of the features
indicated by the Allele Location. As an abstract class, State
currently encompasses single and contiguous :ref:`sequence` changes
(see :ref:`SequenceState`).
