**Computational Definition**

A mapping to a concept in a terminology system.

**Information Model**

Some Mapping attributes are inherited from :ref:`Entity`.

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
      - string
      - 0..1
      - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is  unique within a given system. The identified entity may have a different 'id' in a different  system, or may refer to an 'id' for the shared concept in another system (e.g. a CURIE).
   *  - label
      - string
      - 0..1
      - 
   *  - extensions
      - :ref:`Extension`
      - 0..m
      - 
   *  - system
      - string
      - 1..1
      - Identity of the terminology system.
   *  - version
      - string
      - 0..1
      - Version of the terminology system.
   *  - code
      - :ref:`Code`
      - 1..1
      - Symbol in syntax defined by the terminology system.
   *  - mapping
      - string
      - 1..1
      - A mapping between concepts as defined by the Simple Knowledge Organization System (SKOS).
