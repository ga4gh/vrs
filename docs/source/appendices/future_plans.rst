Future Plans
!!!!!!!!!!!!

As part of publishing this specification, we now describe our next steps, which include expanding the specification for important additional use cases even while we begin the equally crucial work of encouraging stakeholders to embrace the VR-Spec and work toward standardizing the exchange of variation data.

Below is an illustration of planned components for the VR Schema.


.. figure:: ../images/planned_extensions_graph.png
   :align: left

   **An illustration of planned components for the VR Schema.** Version 1.0 components are colored green. Components that are undergoing testing and evaluation and are candidates for the next release cycle are colored yellow. Components that are planned but still undergoing requirement gathering and initial development are colored red. The VR Schema requires the use of multiple composite objects, which are grouped under four abstract classes: :ref:`Variation`, :ref:`Location`, :ref:`State`, and :ref:`Interval`. These classes and their relationships to the representation of Variation are illustrated here. All classes have a string type. Dashed borders denote abstract classes. Abstract classes are not instantiated. Thin solid borders denote classes that may be instantiated but are not identifiable. Bold borders denote identifiable objects (i.e., may be serialized and identified by computed identifier). Solid arrow lines denoted inheritance. Subclasses inherit all attributes from their parent. Inherited attributes are not shown.


.. _planned-intervals:

Planned Interval Concepts
@@@@@@@@@@@@@@@@@@@@@@@@@

.. _NestedInterval:

NestedInterval
@@@@@@@@@@@@@@

**Biological definition**

None

**Computational definition**

An :ref:`Interval` comprised of an *inner* and *outer* :ref:`SimpleInterval`. The *NestedInterval* allows for the definition of "fuzzy" range endpoints by designating a potentially included region (the *outer* SimpleInterval) and required included region (the *inner* SimpleInterval).

**Information model**

.. csv-table::
   :header: Field, Type, Label, Description
   :align: left

   type, :ref:`string`, required, Interval type; must be set to 'NestedInterval'
   inner, :ref:`SimpleInterval`, required, known interval
   outer, :ref:`SimpleInterval`, required, potential interval

**Implementation guidance**

* Implementations MUST require that 0 ≤ outer.start ≤ inner.start ≤ inner.end ≤ outer.end. In the case of double-stranded DNA, this constraint holds even when a feature is on the complementary strand.


**Examples**

* See :ref:`example <nested-interval-example>` in the reference implementation documentation.

.. _will need to convert: https://www.biostars.org/p/84686/

ComplexInterval
###############

.. _planned-states:

Planned State Concepts
@@@@@@@@@@@@@@@@@@@@@@

CNVState
########

StateRule
#########

.. _planned-locations:

Planned Location Concepts
@@@@@@@@@@@@@@@@@@@@@@@@@

CytobandLocation
################

GeneLocation
############

LocationRule
############

.. _planned-variation:

Planned Variation Concepts
@@@@@@@@@@@@@@@@@@@@@@@@@@


Haplotypes
##########

**Biological definition**

A specific combination of Alleles that occur together on single sequence in one or more individuals.

**Computational definition**

A specific combination of non-overlapping Alleles that co-occur on the same reference sequence.

**Information model**

.. csv-table::
   :header: Field, Type, Label, Description
   :align: left
   :widths: auto

   id, :ref:`Id`, optional, Variation Id; must be unique within document
   type, :ref:`string`, required, Variation type; must be set to 'Haplotype'
   location, :ref:`Location`, required, Where Haplotype is located
   completeness, :ref:`enum`, required, Declaration of completeness of the Haplotype definition. Values are: **UNKNOWN**: Other in-phase Alleles may exist. **PARTIAL**: Other in-phase Alleles exist but are unspecified. **COMPLETE**: The Haplotype declares a complete set of Alleles.
   allele_ids, :ref:`Id[]`, required, List of Alleles that comprise this Haplotype

**Implementation guidance**

* The Haplotype location (as specified by the location_id) may refer to a subsequence of the reference sequence, such as a subsequence of an entire chromosome.
* All Alleles in a Haplotype MUST be defined on the same reference sequence as specified by location_id.
* Alleles within a Haplotype MUST not overlap ("overlap" is defined in Interval).
* All Location Intervals are to be interpreted in the context of the underlying reference sequence, irrespective of insertions or deletions by other “upstream” Alleles within the Haplotype.
* When reporting an Haplotype, completeness MUST be set according to these criteria:
   * "COMPLETE" only if the entire reference sequence was assayed and all in-phase Alleles are reported in this Haplotype.
   * "PARTIAL" only if the entire reference sequence was assayed, other in-phase Alleles exist, and are NOT reported in this Haplotype. This is an assertion of unreported variation.
   * "UNKNOWN" otherwise. This value is the default and should be used if neither "COMPLETE" nor "PARTIAL" applies. These cases include, but are not limited to, assays that do not fully cover the reference sequence and an unwillingness by the reporter to declare the existence or absence of other in-phase Alleles.
* A Haplotype with an empty list of Alleles and completeness set to "COMPLETE" is an assertion of an unchanged reference sequence.
* When projecting a Haplotype from one sequence to a larger sequence, a "complete" Haplotype becomes an "unknown" Haplotype on the target sequence. Furthermore, this change is not reversible.

** Notes **
* Alleles within a Haplotype are, by definition, “cis” or “in-phase”. (“In phase” and “cis” refer to features that exist on instances of covalently bonded sequences.)
* Haplotypes are often given names, such as ApoE3 or A*33:01 for convenience.
   * Examples: A*33:01:01 (IMGT/HLA) 
* When used to report Haplotypes, the completeness property enables data providers (e.g, diagnostic labs) to indicate that other Alleles exist, may exist, or do not exist. Data providers may not assay the full reference sequence or may withhold other in-phase Alleles in order to protect patient privacy.
* When used to define Haplotypes, the completeness property enables implementations to permit (PARTIAL) or preclude (COMPLETE) the existence of other variation when matching a Haplotype to a set of observed Alleles.
* Data consumers may wish to use the completeness property in order to provide accurate context for Allele interpretation or to select data used in association studies.

** Sources **
* ISOGG: Haplotype — A haplotype is a combination of alleles (DNA sequences) at different places (loci) on the chromosome that are transmitted together. A haplotype may be one locus, several loci, or an entire chromosome depending on the number of recombination events that have occurred between a given set of loci.
* SO: haplotype (SO:0001024) — A haplotype is one of a set of coexisting sequence variants of a haplotype block.
* GENO: Haplotype (GENO:0000871) - A set of two or more sequence alterations on the same chromosomal strand that tend to be transmitted together.

Genotypes
#########

Translocations
##############

.. _var-sets:

Variation Sets
@@@@@@@@@@@@@@

StaticVariationSets
####################

.. _non-sequence-variation:

Non-sequence Variation
######################

.. warning::
   Not sure what this is.



