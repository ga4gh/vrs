**Computational Definition**

A :ref:`Location` defined by an interval on a referenced :ref:`Sequence`.

**Information Model**

Some SequenceLocation attributes are inherited from :ref:`Entity`.

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
      - `CURIE <core.json#/$defs/CURIE>`_
      - 0..1
      - The 'logical' identifier of the entity in the system of record, and MUST be represented as a CURIE. This 'id' is unique within a given system, but may also refer to an 'id' for the shared concept in  another system (represented by namespace, accordingly).
   *  - type
      - string
      - 1..1
      - MUST be "SequenceLocation"
   *  - sequence_id
      - `CURIE <core.json#/$defs/CURIE>`_
      - 1..1
      - A VRS :ref:`Computed Identifier <computed-identifiers>` for the reference :ref:`Sequence`.
   *  - start
      - :ref:`Number` | :ref:`IndefiniteRange` | :ref:`DefiniteRange`
      - 0..1
      - The start coordinate or range of the SequenceLocation. The minimum value of this coordinate or range is 0. MUST represent a coordinate or range less than the value of `end`.
   *  - end
      - :ref:`Number` | :ref:`IndefiniteRange` | :ref:`DefiniteRange`
      - 0..1
      - The end coordinate or range of the SequenceLocation. The minimum value of this coordinate or range is 0. MUST represent a coordinate or range greater than the value of `start`.
