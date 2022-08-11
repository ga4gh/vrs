**Computational Definition**

The absolute count of discrete copies of a :ref:`MolecularVariation`, :ref:`Feature`, :ref:`SequenceExpression`, or a :ref:`CURIE` reference within a system (e.g. genome, cell, etc.).

**Information Model**

Some AbsoluteCopyNumber attributes are inherited from :ref:`Entity`.

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
      - MUST be "AbsoluteCopyNumber".
   *  - location
      - `CURIE <core.json#/$defs/CURIE>`_ | :ref:`Location`
      - 1..1
      - The location within the system.
   *  - copies
      - :ref:`Number` | :ref:`IndefiniteRange` | :ref:`DefiniteRange`
      - 1..1
      - The integral number of copies of the subject in a system.
