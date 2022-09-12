**Computational Definition**

An unconstrained set of Variation members.

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
      - MUST be "VariationSet"
   *  - members
      - :ref:`CURIE` | :ref:`Variation`
      - 0..m
      - List of Variation objects or identifiers. Attribute is required, but MAY be empty.
