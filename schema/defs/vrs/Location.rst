**Computational Definition**

A contiguous segment of a biological sequence.

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
   *  - _id
      - :ref:`CURIE`
      - 0..1
      - Location Id. MUST be unique within document.
   *  - type
      - string
      - 1..1
      - The Location class type. MUST match child class type.
