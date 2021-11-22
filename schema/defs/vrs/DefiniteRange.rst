**Computational Definition**

A bounded, inclusive range of numbers.

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
      - MUST be "DefiniteRange"
   *  - min
      - number
      - 1..1
      - The minimum value; inclusive
   *  - max
      - number
      - 1..1
      - The maximum value; inclusive
