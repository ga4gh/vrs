**Computational Definition**

DEPRECATED: A SimpleInterval represents a span of sequence. Positions are always represented by contiguous spans using interbase coordinates.
This class is deprecated. Use SequenceInterval instead.

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
      - MUST be "SimpleInterval"
   *  - start
      - integer
      - 1..1
      - The start coordinate
   *  - end
      - integer
      - 1..1
      - The end coordinate
