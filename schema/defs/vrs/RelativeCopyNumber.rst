**Computational Definition**

The relative copies of a :ref:`MolecularVariation`, :ref:`Feature`, :ref:`SequenceExpression`, or a :ref:`CURIE` reference against an unspecified baseline in a system (e.g. genome, cell, etc.).

**Information Model**

Some RelativeCopyNumber attributes are inherited from :ref:`Entity`.

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
      - MUST be "RelativeCopyNumber"
   *  - location
      - `CURIE <core.json#/$defs/CURIE>`_ | :ref:`Location`
      - 1..1
      - The location within the system.
   *  - relative_copy_class
      - string
      - 1..1
      - MUST be one of "EFO:0030070", "EFO:0030072", "EFO:0030071", "EFO:0030067", "EFO:0030069", or "EFO:0030068".
