**Computational Definition**

A sequence of nucleic or amino acid character codes.

    **Information Model**

Some SequenceReference attributes are inherited from :ref:`gks.core:DomainEntity`.

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
          - 1..1
          - MUST be "SequenceReference"
       *  - mappings
          - `ConceptMapping <../gks-core-im/core.json#/$defs/ConceptMapping>`_
          - 0..m
          - A list of mappings to concepts in terminologies or code systems. Each mapping should include a coding and a relation.
       *  - refgetAccession
          - string
          - 1..1
          - A `GA4GH RefGet <http://samtools.github.io/hts-specs/refget.html>` identifier for the referenced sequence, using the sha512t24u digest.
       *  - residueAlphabet
          - string
          - 0..1
          - The interpretation of the character codes referred to by the refget accession, where "aa" specifies an amino acid character set, and "na" specifies a nucleic acid character set.
       *  - circular
          - boolean
          - 0..1
          - A boolean indicating whether the molecule represented by the sequence is circular (true) or linear (false).
