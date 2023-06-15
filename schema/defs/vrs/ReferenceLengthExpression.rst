**Computational Definition**

An expression of a length of a sequence from a repeating reference.

**Information Model**

Some ReferenceLengthExpression attributes are inherited from :ref:`gks.core:Entity`.

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
      - 
   *  - extensions
      - `Extension <core.json#/$defs/Extension>`_
      - 0..m
      - 
   *  - type
      - string
      - 0..1
      - MUST be "ReferenceLengthExpression"
   *  - length
      - integer | :ref:`Range`
      - 1..1
      - The number of residues in the expressed sequence.
   *  - sequence
      - :ref:`SequenceString`
      - 0..1
      - the :ref:`Sequence` encoded by the Reference Length Expression.
   *  - repeatSubunitLength
      - integer
      - 0..1
      - The number of residues in the repeat subunit.
