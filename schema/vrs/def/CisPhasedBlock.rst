**Computational Definition**

An ordered set of co-occurring :ref:`variants <Variation>` on the same molecule.

    **Information Model**
    
Some CisPhasedBlock attributes are inherited from :ref:`Variation`.

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
          - `Extension <../gks-common/common.json#/$defs/Extension>`_
          - 0..m
          - A list of extensions to the entity. Extensions are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.
       *  - digest
          - string
          - 0..1
          - A sha512t24u digest created using the VRS Computed Identifier algorithm.
       *  - expressions
          - `Expression <../gks-common/common.json#/$defs/Expression>`_
          - 0..m
          - 
       *  - type
          - string
          - 1..1
          - MUST be "CisPhasedBlock"
       *  - members
          - :ref:`Allele` | `IRI <../gks-common/common.json#/$defs/IRI>`_
          - 2..m
          - A list of :ref:`Alleles <Allele>` that are found in-cis on a shared molecule.
       *  - sequenceReference
          - :ref:`SequenceReference`
          - 0..1
          - An optional Sequence Reference on which all of the in-cis Alleles are found. When defined, this may be used to implicitly define the `sequenceReference` attribute for each of the CisPhasedBlock member Alleles.
