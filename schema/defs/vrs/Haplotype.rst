**Computational Definition**

A set of non-overlapping :ref:`Allele` members that co-occur on the same molecule.

**Information Model**

Some Haplotype attributes are inherited from :ref:`Entity`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto
   
   *  - Field
      - Type
      - Limits
      - Description
   *  - id
      - `CURIE <core.json#/$defs/CURIE>`_
      - 0..1
      - The 'logical' identifier of the entity in the system of record, and MUST be represented as a CURIE. This 'id' is unique within a given system, but may also refer to an 'id' for the shared concept in  another system (represented by namespace, accordingly).
   *  - type
      - string
      - 1..1
      - MUST be "Haplotype"
   *  - members
      - :ref:`Allele` | `CURIE <core.json#/$defs/CURIE>`_
      - 2..m
      - List of Alleles, or references to Alleles, that comprise this Haplotype.
