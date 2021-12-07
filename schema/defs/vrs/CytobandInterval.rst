**Computational Definition**

A contiguous region specified by cytobands. The region includes the constituent regions described by the start and end cytobands, as well as any intervening regions.

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
      - MUST be "CytobandInterval"
   *  - start
      - :ref:`HumanCytoband`
      - 1..1
      - The start cytoband region. MUST specify a region nearer the terminal end (telomere) of the chromosome p-arm than `end`.
   *  - end
      - :ref:`HumanCytoband`
      - 1..1
      - The start cytoband region. MUST specify a region nearer the terminal end (telomere) of the chromosome q-arm than `start`.
