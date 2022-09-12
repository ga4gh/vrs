**Computational Definition**

A set of non-overlapping :ref:`Allele` members that co-occur on the same molecule.

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
      - MUST be "Haplotype"
   *  - members
      - :ref:`Allele` | :ref:`CURIE`
      - 2..m
      - List of Alleles, or references to Alleles, that comprise this Haplotype.
