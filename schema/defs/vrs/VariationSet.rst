**Computational Definition**

An unconstrained set of Variation members.

**Information Model**

Some VariationSet attributes are inherited from :ref:`Variation`.

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
      - MUST be "VariationSet"
   *  - members
      - :ref:`CURIE` | :ref:`Variation`
      - 0..m
      - List of Variation objects or identifiers. Attribute is required, but MAY be empty.
