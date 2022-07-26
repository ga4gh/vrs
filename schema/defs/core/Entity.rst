**Computational Definition**

Entity is the root class of ‘core’ classes model - those that have identifiers and other general  metadata like labels, xrefs, urls, descriptions, etc. All core classes descend from and inherit  its attributes.

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
   *  - id
      - :ref:`CURIE`
      - 0..1
      - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is  unique within a given system. The identified entity may have a different 'id' in a different  system.
   *  - type
      - string
      - 1..1
      - The schema class that is instantiated by the data object. Must be the name of a class from  the VA schema.
