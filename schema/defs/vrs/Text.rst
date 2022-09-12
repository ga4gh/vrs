**Computational Definition**

A free-text definition of variation.

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
      - MUST be "Text"
   *  - definition
      - string
      - 1..1
      - A textual representation of variation not representable by other subclasses of Variation.
