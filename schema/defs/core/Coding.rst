**Computational Definition**

a concept codified by a terminology system.

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
       *  - label
          - string
          - 0..1
          - A primary label for the coding.
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
