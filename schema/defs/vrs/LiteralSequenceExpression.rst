**Computational Definition**

An explicit expression of a Sequence.

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
      - MUST be "LiteralSequenceExpression"
   *  - sequence
      - :ref:`Sequence`
      - 1..1
      - the literal :ref:`Sequence` expressed
