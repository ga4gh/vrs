**Computational Definition**

The Extension class provides VODs with a means to extend descriptions with other attributes unique to a content provider. These extensions are not expected to be natively understood under VRSATILE, but may be used for pre-negotiated exchange of message attributes when needed.

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
          - 0..1
          - MUST be "Extension".
       *  - name
          - string
          - 1..1
          - A name for the Extension
       *  - value
          - ['number', 'string', 'boolean', 'object', 'array', 'null']
          - 0..1
          - Any primitive or structured object
