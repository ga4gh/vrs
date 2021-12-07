**Computational Definition**

The count of discrete copies of a subject :ref:`MolecularVariation`, :ref:`Feature`, :ref:`SequenceExpression`, or a :ref:`CURIE` reference to any of these.

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
      - :ref:`MolecularVariation` | :ref:`Feature` | :ref:`SequenceExpression` | :ref:`CURIE`
      - 1..1
      - Subject of the Copy Number object
   *  - copies
      - :ref:`Number` | :ref:`IndefiniteRange` | :ref:`DefiniteRange`
      - 1..1
      - The integral number of copies of the subject in a genome
