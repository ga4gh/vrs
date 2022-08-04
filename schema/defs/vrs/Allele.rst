**Computational Definition**

The state of a molecule at a :ref:`Location`.

**Information Model**

Some Allele attributes are inherited from :ref:`Entity`.

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
      - MUST be "Allele"
   *  - location
      - `CURIE <core.json#/$defs/CURIE>`_ | :ref:`Location`
      - 1..1
      - Where Allele is located
   *  - state
      - :ref:`SequenceExpression` | :ref:`SequenceState` (deprecated)
      - 1..1
      - An expression of the sequence state
