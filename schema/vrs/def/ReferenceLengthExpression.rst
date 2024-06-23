**Computational Definition**

An expression of a length of a sequence from a repeating reference.

    **Information Model**
    
Some ReferenceLengthExpression attributes are inherited from :ref:`SequenceExpression`.

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
       *  - mappings
          - `ConceptMapping <../gks-common/common.json#/$defs/ConceptMapping>`_
          - 0..m
          - A list of mappings to concepts in terminologies or code systems. Each mapping should include a coding and a relation.
       *  - extensions
          - `Extension <../gks-common/common.json#/$defs/Extension>`_
          - 0..m
          - A list of extensions to the entity. Extensions are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.
       *  - type
          - string
          - 1..1
          - MUST be "ReferenceLengthExpression"
       *  - length
          - integer | :ref:`Range`
          - 1..1
          - The number of residues in the expressed sequence.
       *  - sequence
          - :ref:`SequenceString`
          - 0..1
          - the :ref:`Sequence` encoded by the Reference Length Expression.
       *  - repeatSubunitLength
          - integer
          - 1..1
          - The number of residues in the repeat subunit.
