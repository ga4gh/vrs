**Computational Definition**

A break in a molecule with respect to a reference sequence indicating the sequence deviates from the reference sequence after or before this location.

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
          - MUST be "Breakend"
       *  - location
          - Location
          - 1..1
          - The interval over which the break could occur in
       *  - orientation
          - string
          - 1..1
          - MUST be one of "DivergesAfter" or "DivergesBefore" indicating whether the sequences diverges from the reference after or before any position in the interval.
