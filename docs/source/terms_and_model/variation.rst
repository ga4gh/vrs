.. _variation:

Variation
#########

This is the variation definition.

.. todo::
   Describe Variation

.. _allele:

Allele
******
**Biological definition:** One of a number of alternative forms of the same gene or same genetic locus. In the context of biological sequences, “allele” refers to a set of specific changes within a :ref:`Sequence`, including sets with zero (no change), one change (a simple allele), or multiple changes (:ref:`var-sets`). In the context of VR, Allele refers to a Sequence or Sequence change with respect to a reference sequence.

**Computational definition:** An Allele is a specific, single, and contiguous :ref:`Sequence` at a :ref:`Location`. Each alternative Sequence may be empty, shorter, longer, or the same length as the interval (e.g., due to one or more indels).

**Information model**

.. csv-table::
   :header: Field, Type, Label, Description
   :align: left
   :widths: 12, 9, 10, 30

   id, :ref:`Id`, optional, Location Id; must be unique within document
   location_id, :ref:`Id`, required, An id mapping to the Identifier of the external database Sequence
   interval, :ref:`Interval`, required, Position of feature on reference sequence specified by sequence_id.

.. todo::

   Finish Allele

************
Text Variant
************
.. todo::

   Finish Text Variant
