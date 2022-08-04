**Computational Definition**

A `coding` is an extensible entity for labeling or otherwise annotating globally  namespaced identifiers known as "codes".

**Information Model**

Some Coding attributes are inherited from :ref:`Entity`.

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
      - :ref:`CURIE`
      - 0..1
      - The `coding.id` field is used to capture the code as a CURIE.
   *  - type
      - string
      - 1..1
      - MUST be "Coding".
   *  - label
      - string
      - 0..1
      - 
   *  - extensions
      - :ref:`Extension`
      - 0..m
      - 
   *  - record_metadata
      - :ref:`RecordMetadata`
      - 0..1
      - 
