**Computational Definition**

A rearrangement resulting in sequences flanking the two breakends becoming adjacent sequences on the same molecule.

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
       *  - type
          - string
          - 1..1
          - MUST be "Breakpoint"
       *  - breakends
          - Breakend
          - 1..2
          - Breakends involed in the sequence
       *  - insertion
          - DefiniteRange
          - 0..1
          - Approximate length of unknown sequence between the breaks.
       *  - homology
          - boolean
          - 0..1
          - A flag indicating whether the location interval of the breakend is due to the sequences at the breakends being homologous or whether the interval is due to uncertainty regarding the actual locations of the breakends.
       *  - sequence
          - LiteralSequenceExpression
          - 0..1
          - Sequence occuring after the break.
       *  - terminal
          - boolean
          - 0..1
          - Indicates the end of the molecule
