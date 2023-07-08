**Computational Definition**

The state of a molecule at a :ref:`Location`.

**Information Model**

Some Allele attributes are inherited from :ref:`ValueObject`.

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
      - MUST be "Allele"
   *  - digest
      - string
      - 0..1
      - A sha512t24u digest created using the VRS Computed Identifier algorithm.
   *  - location
      - `IRI <core.json#/$defs/IRI>`_ | :ref:`Location`
      - 1..1
      - Where Allele is located
   *  - state
      - :ref:`SequenceExpression`
      - 1..1
      - An expression of the sequence state
