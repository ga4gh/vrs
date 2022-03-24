**Computational Definition**

The state of a molecule at a :ref:`Location`.

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
      - MUST be "Allele"
   *  - location
      - :ref:`CURIE` | :ref:`SequenceLocation.v2`
      - 1..1
      - Where Allele is located
   *  - state
      - :ref:`SequenceExpression`
      - 1..1
      - An expression of the sequence state
