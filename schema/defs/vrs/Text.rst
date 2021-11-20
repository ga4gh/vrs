**Computational Definition**

A free-text definition of variation.

**Information Model**

Some Text attributes are inherited from :ref:`Variation`.

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
      - MUST be "Text"
   *  - definition
      - string
      - 1..1
      - A textual representation of variation not representable by other subclasses of Variation.
