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
          - `Extension </ga4gh/schema/gks-common/1.x/data-types/json/Extension>`_
          - 0..m
          - A list of extensions to the entity. Extensions are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.
       *  - digest
          - string
          - 0..1
          - A sha512t24u digest created using the VRS Computed Identifier algorithm.
       *  - expressions
          - `Expression </ga4gh/schema/gks-common/1.x/data-types/json/Expression>`_
          - 0..m
          - 
       *  - location
          - `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_ | :ref:`Location`
          - 1..1
          - A location for which the number of systemic copies is described.
       *  - type
          - string
          - 1..1
          - MUST be "CopyNumberCount"
       *  - copies
          - integer | :ref:`Range`
          - 1..1
          - The integral number of copies of the subject in a system
