**Computational Definition**

The `Adjacency` class can represent either the termination of a sequence or the adjoining of the end of a sequence with the beginning of an adjacent sequence, potentially with an intervening linker sequence.

**Information Model**

Some Adjacency attributes are inherited from :ref:`Variation`.

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
      - :ref:`Expression`
      - 0..m
      - 
   *  - type
      - string
      - 1..1
      - MUST be "Adjacency".
   *  - adjoinedSequences
      - `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_ | :ref:`Location`
      - 2..2
      - The terminal sequence or pair of adjoined sequences that defines in the adjacency.
   *  - linker
      - :ref:`SequenceExpression`
      - 0..1
      - The sequence found between adjoined sequences.
   *  - homology
      - boolean
      - 0..1
      - A flag indicating if coordinate ambiguity in the adjoined sequences is from sequence homology (true) or other uncertainty (false).
