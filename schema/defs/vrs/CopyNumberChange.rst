**Computational Definition**

An assessment of the copy number of a :ref:`Location` or a :ref:`Feature` within a system (e.g. genome, cell, etc.) relative to a baseline ploidy.

**Information Model**

Some CopyNumberChange attributes are inherited from :ref:`Entity`.

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
      - MUST be "CopyNumberChange"
   *  - subject
      - :ref:`Location` | :ref:`CURIE`
      - 1..1
      - A location for which the number of systemic copies is described.
   *  - copy_change
      - string
      - 1..1
      - MUST be one of "EFO:0030069" (complete genomic loss), "EFO:0020073" (high-level loss), "EFO:0030068" (low-level loss), "EFO:0030067" (loss), "EFO:0030064" (regional base ploidy), "EFO:0030070" (gain), "EFO:0030071" (low-level gain), "EFO:0030072" (high-level gain).
