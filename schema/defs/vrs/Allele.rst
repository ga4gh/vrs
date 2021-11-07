**Computational Definition**

The state of a molecule at a :ref:`Location`.

**Information Model**

Some Allele attributes are inherited from :ref:`Variation`.

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
      - MUST be "Allele"
   *  - location
      - :ref:`CURIE` | :ref:`Location`
      - 1..1
      - Where Allele is located
   *  - state
      - :ref:`SequenceExpression` | :ref:`SequenceState` (deprecated)
      - 1..1
      - An expression of the sequence state
