**Computational Definition**

A :ref:`Location` defined by an interval on a referenced :ref:`Sequence`.

**Information Model**

Some SequenceLocation attributes are inherited from :ref:`ValueObject`.

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
      - 1..1
      - MUST be "SequenceLocation"
   *  - digest
      - string
      - 0..1
      - A sha512t24u digest created using the VRS Computed Identifier algorithm.
   *  - sequence
      - `IRI <core.json#/$defs/IRI>`_ | :ref:`SequenceReference`
      - 0..1
      - A :ref:`SequenceReference`.
   *  - start
      - integer | :ref:`Range`
      - 1..1
      - The start coordinate or range of the SequenceLocation. The minimum value of this coordinate or range is 0. MUST represent a coordinate or range less than the value of `end`.
   *  - end
      - integer | :ref:`Range`
      - 1..1
      - The end coordinate or range of the SequenceLocation. The minimum value of this coordinate or range is 0. MUST represent a coordinate or range greater than the value of `start`.
