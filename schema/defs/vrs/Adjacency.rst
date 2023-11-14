**Computational Definition**

The `Adjacency` class represents the termination of a sequence and (when present) the beginning of an adjacent sequence, potentially with an intervening linker sequence.

    **Information Model**
    
Some Adjacency attributes are inherited from :ref:`Ga4ghIdentifiableObject`.

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
          - `Extension <core.json#/$defs/Extension>`_
          - 0..m
          - 
       *  - digest
          - string
          - 0..1
          - A sha512t24u digest created using the VRS Computed Identifier algorithm.
       *  - type
          - string
          - 1..1
          - MUST be "Adjacency".
       *  - sequenceTerminals
          - `IRI <core.json#/$defs/IRI>`_ | :ref:`Location`
          - 1..2
          - Sequence terminals involved in the adjacency.
       *  - linker
          - :ref:`SequenceExpression`
          - 0..1
          - A linker sequence found between the sequence terminals.
