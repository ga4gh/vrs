**Computational Definition**

A SequenceInterval represents a span on a :ref:`Sequence`. Positions are always represented by contiguous spans using interbase coordinates or coordinate ranges.

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
      - MUST be "SequenceInterval"
   *  - start
      - :ref:`Number` | :ref:`IndefiniteRange` | :ref:`DefiniteRange`
      - 1..1
      - The start coordinate or range of the interval. The minimum value of this coordinate or range is 0. MUST represent a coordinate or range less than the value of `end`.
   *  - end
      - :ref:`Number` | :ref:`IndefiniteRange` | :ref:`DefiniteRange`
      - 1..1
      - The end coordinate or range of the interval. The minimum value of this coordinate or range is 0. MUST represent a coordinate or range greater than the value of `start`.
