**Computational Definition**

Write this later.

**Information Model**

Some LabeledEntity attributes are inherited from :ref:`Entity`.

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
      - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is  unique within a given system. The identified entity may have a different 'id' in a different  system.
   *  - type
      - string
      - 1..1
      - MUST be "LabeledEntity".
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
