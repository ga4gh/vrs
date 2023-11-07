**Computational Definition**

A rearrangement resulting in sequences flanking the two breakends becoming adjacent sequences on the same molecule.

    **Information Model**
    
Some Breakpoint attributes are inherited from :ref:`ValueObject`.

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
          - MUST be "Breakpoint"
       *  - breakends
          - `IRI <core.json#/$defs/IRI>`_ | :ref:`Breakend`
          - 1..2
          - Breakends involved in the sequence
       *  - insertion
          - :ref:`Range`
          - 0..1
          - Approximate length of unknown sequence between the breaks.
       *  - homology
          - boolean
          - 0..1
          - A flag indicating whether the location interval of the breakend is due to the sequences at the breakends being homologous or whether the interval is due to uncertainty regarding the actual locations of the breakends.
       *  - sequence
          - `IRI <core.json#/$defs/IRI>`_ | :ref:`SequenceExpression`
          - 0..1
          - Sequence occurring after the break.
       *  - terminal
          - boolean
          - 0..1
          - Indicates the end of the molecule
