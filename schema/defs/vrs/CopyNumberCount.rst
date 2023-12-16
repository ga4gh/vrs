**Computational Definition**

The absolute count of discrete copies of a :ref:`Location` or :ref:`Gene`, within a system (e.g. genome, cell, etc.).

    **Information Model**
    
Some CopyNumberCount attributes are inherited from :ref:`CopyNumber`.

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
          - `Extension <gks.common.json#/$defs/Extension>`_
          - 0..m
          - 
       *  - digest
          - string
          - 0..1
          - A sha512t24u digest created using the VRS Computed Identifier algorithm.
       *  - type
          - string
          - 0..1
          - MUST be "CopyNumberCount"
       *  - expressions
          - :ref:`Expression`
          - 0..m
          - 
       *  - location
          - `IRI <gks.common.json#/$defs/IRI>`_ | :ref:`Location`
          - 1..1
          - A location for which the number of systemic copies is described.
       *  - copies
          - integer | :ref:`Range`
          - 1..1
          - The integral number of copies of the subject in a system
