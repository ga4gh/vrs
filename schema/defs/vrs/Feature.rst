**Computational Definition**

A named entity that can be mapped to a Location. Genes, protein domains, exons, and chromosomes are some examples of common biological entities that may be Features.

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
      - The Feature class type. MUST match child class type.
