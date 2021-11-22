**Computational Definition**

A half-bounded range of numbers represented as a number bound and associated comparator. The bound operator is interpreted as follows: '>=' are all numbers greater than and including `value`, '<=' are all numbers less than and including `value`.

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
      - 1..1
      - MUST be "IndefiniteRange"
   *  - value
      - number
      - 1..1
      - The bounded value; inclusive
   *  - comparator
      - string
      - 1..1
      - MUST be one of "<=" or ">=", indicating which direction the range is indefinite
