**Computational Definition**

An assessment of the copy number of a :ref:`Location` or a :ref:`Feature` within a system (e.g. genome, cell,  etc.) relative to a baseline ploidy.

**Information Model**

Some CopyNumberChange attributes are inherited from :ref:`Variation`.

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
      - MUST be "CopyNumberChange"
   *  - subject
      - :ref:`Location` | :ref:`CURIE` | :ref:`Feature`
      - 1..1
      - A location for which the number of systemic copies is described.
   *  - copy_change
      - string
      - 1..1
      - MUST be one of "efo:0030069" (complete genomic loss), "efo:0020073" (high-level loss),  "efo:0030068" (low-level loss), "efo:0030067" (loss), "efo:0030064" (regional base ploidy),  "efo:0030070" (gain), "efo:0030071" (low-level gain), "efo:0030072" (high-level gain).
