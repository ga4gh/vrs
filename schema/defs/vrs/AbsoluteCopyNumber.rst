**Computational Definition**

The absolute count of discrete copies of a :ref:`MolecularVariation`, :ref:`Feature`, :ref:`SequenceExpression`, or a :ref:`CURIE` reference within a system (e.g. genome, cell, etc.).

**Information Model**

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto
   
   *  - Field
      - Type
      - Limits
      - Description
   *  - type
      - string
      - 0..1
      - MUST be "AbsoluteCopyNumber"
   *  - subject
      - :ref:`MolecularVariation` | :ref:`Feature` | :ref:`SequenceExpression` | `CURIE <core.json#/$defs/CURIE>`_
      - 1..1
      - Subject of the Copy Number object
   *  - copies
      - :ref:`Number` | :ref:`IndefiniteRange` | :ref:`DefiniteRange`
      - 1..1
      - The integral number of copies of the subject in a system
