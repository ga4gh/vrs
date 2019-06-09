Future Plans
!!!!!!!!!!!!

.. figure:: ../images/planned_extensions_graph.png
   :align: left

   **An illustration of planned components for the VR Schema.** Version 1.0 components are colored green. Components that are undergoing testing and evaluation and are candidates for the next release cycle are colored yellow. Components that are planned but still undergoing requirement gathering and initial development are colored red. The VR Schema requires the use of multiple composite objects, which are grouped under four abstract classes: :ref:`Variation`, :ref:`Location`, :ref:`State`, and :ref:`Interval`. These classes and their relationships to the representation of Variation are illustrated here. All classes have a string type. Dashed borders denote abstract classes. Abstract classes are not instantiated. Thin solid borders denote classes that may be instantiated but are not identifiable. Bold borders denote identifiable objects (i.e., may be serialized and identified by computed identifier). Solid arrow lines denoted inheritance. Subclasses inherit all attributes from their parent. Inherited attributes are not shown.



.. _var-sets:

Variation Sets
@@@@@@@@@@@@@@

.. _planned-variation:

Planned Variation Concepts
@@@@@@@@@@@@@@@@@@@@@@@@@@


Haplotypes
##########

Genotypes
#########

Translocations
##############

.. _planned-locations:


Planned Location Concepts
@@@@@@@@@@@@@@@@@@@@@@@@@

CytobandLocation
################

GeneLocation
############

LocationRule
############

.. _planned-states:


Planned State Concepts
@@@@@@@@@@@@@@@@@@@@@@

CNVState
########

StateRule
#########

.. _planned-intervals:


Planned Interval Concepts
@@@@@@@@@@@@@@@@@@@@@@@@@

.. _NestedInterval:

NestedInterval
@@@@@@@@@@@@@@

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

.. _non-sequence-variation:

Non-sequence Variation
######################
