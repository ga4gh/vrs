**Computational Definition**

A set of non-overlapping :ref:`Allele` members that co-occur on the same molecule.

**Information Model**

Some Haplotype attributes are inherited from :ref:`Variation`.

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
      - MUST be "Haplotype"
   *  - members
      - :ref:`Allele` | :ref:`CURIE`
      - 1..m
      - List of Alleles, or references to Alleles, that comprise this Haplotype.
