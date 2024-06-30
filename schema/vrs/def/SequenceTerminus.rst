**Computational Definition**

The `SequenceTerminus` data class provides a structure for describing the end (terminus) of a sequence. Structurally similar to Adjacency but the linker sequence is not allowed and it removes the unnecessary array structure.

    **Information Model**
    
Some SequenceTerminus attributes are inherited from :ref:`Variation`.

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
          - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system, or may refer to an 'id' for the shared concept in another system (e.g. a CURIE).
       *  - label
          - string
          - 0..1
          - A primary name for the entity.
       *  - description
          - string
          - 0..1
          - A free-text description of the entity.
       *  - alternativeLabels
          - string
          - 0..m
          - Alternative name(s) for the Entity.
       *  - extensions
          - `Extension <../gks-core-im/core.json#/$defs/Extension>`_
          - 0..m
          - A list of extensions to the entity. Extensions are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.
       *  - type
          - string
          - 0..1
          - MUST be "SequenceTerminus".
       *  - digest
          - string
          - 0..1
          - A sha512t24u digest created using the VRS Computed Identifier algorithm.
       *  - expressions
          - `Expression <../gks-core-im/core-im.json#/$defs/Expression>`_
          - 0..m
          - 
       *  - location
          - `IRI <../gks-core-im/core-im.json#/$defs/IRI>`_ | :ref:`Location`
          - 1..1
          - The location of the terminus.
