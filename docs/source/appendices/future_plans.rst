.. _future-plans:

Future Plans
!!!!!!!!!!!!

Overview
@@@@@@@@

VRS covers a fundamental subset of data types to represent
variation, thus far predominantly related to the replacement of a
subsequence in a reference sequence. Increasing its applicability will
require supporting more complex types of variation, including:

* alternative coordinate types such as nested ranges
* feature-based coordinates such as genes, cytogenetic bands, and exons
* copy number variation
* structural variation
* mosaicism and chimerism
* rule-based variation

.. figure:: ../images/schema-future.png

   An illustration of planned components for the VRS Schema.

   Version 1.0 components are colored green. Components that are
   undergoing testing and evaluation and are candidates for the next
   release cycle are colored yellow. Components that are planned but
   still undergoing requirement gathering and initial development are
   colored red. The VRS Schema requires the use of multiple composite
   objects, which are grouped under four abstract classes:
   :ref:`Variation`, :ref:`Location`, :ref:`State`, and
   :ref:`Interval`. These classes and their relationships to the
   representation of Variation are illustrated here. All classes have
   a string type. Dashed borders denote abstract classes. Abstract
   classes are not instantiated. Thin solid borders denote classes
   that may be instantiated but are not identifiable. Bold borders
   denote identifiable objects (i.e., may be serialized and identified
   by computed identifier). Solid arrow lines denoted
   inheritance. Subclasses inherit all attributes from their
   parent. Inherited attributes are not shown.

The following sections provide a preview of planned concepts under way
to address a broader representation of variation.


.. _planned-locations:

Intervals and Locations
@@@@@@@@@@@@@@@@@@@@@@@

VRS uses :ref:`Interval` and :ref:`Location` subclasses to define
where variation occurs.  The schema is designed to be extensible to
new kinds of Intervals and Locations in order to support, for example,
fuzzy coordinates or feature-based locations.


NestedInterval
##############

**Biological definition**

None

**Computational definition**

An :ref:`Interval` comprised of an *inner* and *outer*
:ref:`SimpleInterval`. The *NestedInterval* allows for the definition
of "fuzzy" range endpoints by designating a potentially included
region (the *outer* SimpleInterval) and required included region (the
*inner* SimpleInterval).

**Information model**

.. list-table::
   :class: reece-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   * - Field
     - Type
     - Limits
     - Description
   * - type
     - string
     - 1..1
     - Interval type; MUST be set to '**NestedInterval**'
   * - inner
     - :ref:`SimpleInterval`
     - 1..1
     - known interval
   * - outer
     - :ref:`SimpleInterval`
     - 1..1
     - potential interval

**Implementation guidance**

* Implementations MUST enforce values `0 ≤ outer.start ≤ inner.start ≤
  inner.end ≤ outer.end`. In the case of double-stranded DNA, this
  constraint holds even when a feature is on the complementary strand.



ComplexInterval
###############

**Biological definition**

Representation of complex coordinates based on relative locations or
offsets from a known location. Examples include "left of" a given
position and intronic positions measured from intron-exon junctions.

**Computational definition**

Under development.

**Information model**

Under development.


GeneLocation
############

**Biological definition**

The symbolic location of a gene.

**Computational definition**

A gene location is made by reference to a gene identifier from NCBI,
Ensembl, HGNC, or other public trusted authority.

**Information model**

.. list-table::
   :class: reece-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   * - Field
     - Type
     - Limits
     - Description
   * - _id
     - :ref:`CURIE`
     - 0..1
     - Location Id; MUST be unique within document
   * - type
     - string
     - 1..1
     - Location type; MUST be set to '**GeneLocation**'
   * - gene_id
     - :ref:`CURIE`
     - 1..1
     - CURIE-formatted gene identifier using NCBI numeric gene id.

**Notes**

* `gene_id` MUST be specified as a CURIE, using a CURIE prefix of
  `"NCBI"` and CURIE reference with the numeric gene id. Other trusted
  authorities MAY be permitted in future releases.

**Implementation guidance**

* GeneLocations MAY be converted to :ref:`sequence-location` using
  external data. The source of such data and mechanism for
  implementation is not defined by this specification.


.. _planned-states:

State Classes
@@@@@@@@@@@@@

Additional :ref:`State` concepts that are being planned for future
consideration in the specification.


.. _planned-cnvstate:

CNVState
########

.. note:: This concept is being refined. Please comment at https://github.com/ga4gh/vr-spec/issues/46.

**Biological definition**

Variations in the number of copies of a segment of DNA.  Copy number
variations cover copy losses or gains and at known or unknown
locations (including tandem repeats).  Variations MAY occur at precise
SequenceLocations, within nested intervals, or at GeneLocations.
There is no lower or upper bound on CNV sizes.

**Computational definition**

Under development.

**Information model**

.. list-table::
   :class: reece-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   * - Field
     - Type
     - Limits
     - Description
   * - type
     - string
     - 1..1
     - State type; MUST be set to '**CNVState**'
   * - location
     - :ref:`Location`
     - 1..1
     - the Location of the copy ('**null**' if unknown)
   * - min_copies
     - int
     - 1..1
     - The minimum number of copies
   * - max_copies
     - int
     - 1..1
     - The maximum number of copies


.. _planned-variation:

Variation Classes
@@@@@@@@@@@@@@@@@

Additional :ref:`Variation` concepts that are being planned for future
consideration in the specification. See :ref:`Variation` for more
information.


Translocations
##############

.. note:: This concept is being refined. Please comment at https://github.com/ga4gh/vr-spec/issues/103

**Biological definition**

The aberrant joining of two segments of DNA that are not typically
contiguous.  In the context of joining two distinct coding sequences,
translocations result in a gene fusion, which is also covered by this
VRS definition.

**Computational definition**

A joining of two sequences is defined by two :ref:`Location` objects
and an indication of the join "pattern" (advice needed on conventional
terminology, if any).

**Information model**

Under consideration. See https://github.com/ga4gh/vr-spec/issues/28.

**Examples**

t(9;22)(q34;q11) in BCR-ABL


.. _genotype:

Genotype
########

**Biological definition**

The genetic state of an organism, whether complete (defined over the
whole genome) or incomplete (defined over a subset of the genome).

**Computational definition**

A list of Haplotypes.

**Information model**

.. list-table::
   :class: reece-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   * - Field
     - Type
     - Limits
     - Description
   * - _id
     - :ref:`CURIE`
     - 0..1
     - Variation Id; MUST be unique within document
   * - type
     - string
     - 1..1
     - Variation type; MUST be set to '**Genotype**'
   * - completeness
     - enum
     - 1..1
     - Declaration of completeness of the Haplotype definition.
       Values are:

       * UNKNOWN: Other Haplotypes may exist.
       * PARTIAL: Other Haplotypes exist but are unspecified.
       * COMPLETE: The Genotype declares a complete set of Haplotypes.

   * - members
     - :ref:`Haplotype`\[] or :ref:`CURIE`\[]
     - 0..*
     - List of Haplotypes or Haplotype identifiers; length MUST agree
       with ploidy of genomic region


**Implementation guidance**

* Haplotypes in a Genotype MAY occur at different locations or on
  different reference sequences. For example, an individual may have
  haplotypes on two population-specific references.
* Haplotypes in a Genotype MAY contain differing numbers of Alleles or
  Alleles at different Locations.

**Notes**

* The term "genotype" has two, related definitions in common use. The
  narrower definition is a set of alleles observed at a single
  location and with a ploidy of two, such as a pair of single residue
  variants on an autosome. The broader, generalized definition is a
  set of alleles at multiple locations and/or with ploidy other than
  two.The VR-Spec Genotype entity is based on this broader definition.
* The term "diplotype" is often used to refer to two haplotypes. The
  VR-Spec Genotype entity subsumes the conventional definition of
  diplotype. Therefore, the VR-Spec model does not include an explicit
  entity for diplotypes. See :ref:`this note
  <genotypes-represent-haplotypes-with-arbitrary-ploidy>` for a
  discussion.
* The VR-SPec model makes no assumptions about ploidy of an organism
  or individual. The number of Haplotypes in a Genotype is the
  observed ploidy of the individual.
* In diploid organisms, there are typically two instances of each
  autosomal chromosome, and therefore two instances of sequence at a
  particular location. Thus, Genotypes will often list two
  Haplotypes. In the case of haploid chromosomes or
  haploinsufficiency, the Genotype consists of a single Haplotype.
* A consequence of the computational definition is that Haplotypes at
  overlapping or adjacent intervals MUST NOT be included in the same
  Genotype. However, two or more Alleles MAY always be rewritten as an
  equivalent Allele with a common sequence and interval context.
* The rationale for permitting Genotypes with Haplotypes defined on
  different reference sequences is to enable the accurate
  representation of segments of DNA with the most appropriate
  population-specific reference sequence.

**Sources**

SO: `Genotype (SO:0001027)
<http://www.sequenceontology.org/browser/current_svn/term/SO:0001027>`__
— A genotype is a variant genome, complete or incomplete.

.. _genotypes-represent-haplotypes-with-arbitrary-ploidy:

.. note:: Genotypes represent Haplotypes with arbitrary ploidy
     The VR-Spec defines Haplotypes as a list of Alleles, and Genotypes as
     a list of Haplotypes. In essence, Haplotypes and Genotypes represent
     two distinct dimensions of containment: Haplotypes represent the "in
     phase" relationship of Alleles while Genotypes represents sets of
     Haplotypes of arbitrary ploidy.

     There are two important consequences of these definitions: There is no
     single-location Genotype. Users of SNP data will be familiar with
     representations like rs7412 C/C, which indicates the diploid state at
     a position. In the VR-Spec, this is merely a special case of a
     Genotype with two Haplotypes, each of which is defined with only one
     Allele (the same Allele in this case).  The VR-Spec does not define a
     diplotype type. A diplotype is a special case of a VR-Spec Genotype
     with exactly two Haplotypes. In practice, software data types that
     assume a ploidy of 2 make it very difficult to represent haploid
     states, copy number loss, and copy number gain, all of which occur
     when representing human data. In addition, assuming ploidy=2 makes
     software incompatible with organisms with other ploidy. The VR-Spec
     makes no assumptions about "normal" ploidy.

     In other words, the VR-Spec does not represent single-position
     Genotypes or diplotypes because both concepts are subsumed by the
     Allele, Haplotype, and Genotypes entities.



.. _GitHub issue: https://github.com/ga4gh/vr-spec/issues
.. _genetic variation: https://en.wikipedia.org/wiki/Genetic_variation


.. _planned-variation-sets:

Rule-based Variation
@@@@@@@@@@@@@@@@@@@@

Some variations are defined by categorical concepts, rather than specific
locations and states. These variations go by many terms, including
*categorical variants*, *bucket variants*, *container variants*, or
*variant classes*. These forms of variation are not described by any
broadly-recognized variation format, but modeling them is a key requirement
for the representation of aggregate variation descriptions as commonly
found in biomedical literature. Our future work will focus on the formal
specification for representing these variations with sets of rules, which
we currently call *Rule-based Variation*.

RuleLocation
############

RuleLocation is a subclass of :ref:`location` intended to capture locations
defined by rules instead of specific contiguous sequences. This includes
locations defined by sequence characteristics, e.g. *microsatellite
regions*.

RuleState
#########

RuleState is a subclass of :ref:`state` intended to capture states defined
by categorical rules instead of sequence states. This includes *gain- /
loss-of-function*, *oncogenic*, and *truncating* variation.

