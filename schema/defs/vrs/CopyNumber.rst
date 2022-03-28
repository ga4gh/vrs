**Computational Definition**

The absolute count of discrete copies of a :ref:`MolecularVariation`, :ref:`Feature`, :ref:`SequenceExpression`, or a :ref:`CURIE` reference within a system (e.g. genome, cell, etc.).

**Information Model**

Some CopyNumber attributes are inherited from :ref:`Variation`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto
   
   *  - Field
      - Type
      - Limits
      - Description
   *  - _id
      - :ref:`CURIE`
      - 0..1
      - Variation Id. MUST be unique within document.
   *  - type
      - string
      - 1..1
      - MUST be "CopyNumber"
   *  - subject
      - :ref:`MolecularVariation` | :ref:`Feature` | :ref:`SequenceExpression` | :ref:`CURIE` | :ref:`Location`
      - 1..1
      - Subject of the Copy Number object
   *  - copies
      - :ref:`Number` | :ref:`IndefiniteRange` | :ref:`DefiniteRange`
      - 1..1
      - The integral number of copies of the subject in a system
