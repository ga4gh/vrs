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
          - A primary label for the entity.
       *  - description
          - string
          - 0..1
          - A free-text description of the entity.
       *  - extensions
          - :ref:`Extension`
          - 0..m
          - 
       *  - coding
          - :ref:`Coding`
          - 1..1
          - 
       *  - relation
          - string
          - 1..1
          - A mapping relation between concepts as defined by the Simple Knowledge Organization System (SKOS).
