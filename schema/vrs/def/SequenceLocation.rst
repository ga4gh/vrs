**Computational Definition**

A :ref:`Location` defined by an interval on a referenced :ref:`Sequence`.

    **Information Model**
    
Some SequenceLocation attributes are inherited from :ref:`Ga4ghIdentifiableObject`.

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
          - `Extension <../gks-common/core.json#/$defs/Extension>`_
          - 0..m
          - 
       *  - type
          - string
          - 0..1
          - MUST be "SequenceLocation"
       *  - digest
          - string
          - 0..1
          - A sha512t24u digest created using the VRS Computed Identifier algorithm.
       *  - sequenceReference
          - `IRI <../gks-common/$defs/IRI>`_ | :ref:`SequenceReference`
          - 0..1
          - A :ref:`SequenceReference`.
       *  - start
          - integer | :ref:`Range`
          - 0..1
          - The start coordinate or range of the SequenceLocation. The minimum value of this coordinate or range is 0. MUST represent a coordinate or range less than or equal to the value of `end`.
       *  - end
          - integer | :ref:`Range`
          - 0..1
          - The end coordinate or range of the SequenceLocation. The minimum value of this coordinate or range is 0. MUST represent a coordinate or range greater than or equal to the value of `start`.
