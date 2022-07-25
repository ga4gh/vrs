**Computational Definition**

The absolute count of discrete copies of a :ref:`MolecularVariation`, :ref:`Feature`, :ref:`SequenceExpression`, or a :ref:`CURIE` reference within a system (e.g. genome, cell, etc.).

**Information Model**

Some CopyNumber attributes are inherited from :ref:`Entity`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto
   
   *  - Field
      - Type
      - Limits
      - Description
   *  - _id
      - `CURIE <core.json#/$defs/CURIE>`_
      - 0..1
      - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is  unique within a given system. The identified entity may have a different 'id' in a different  system.
   *  - type
      - string
      - 1..1
      - MUST be "CopyNumber"
   *  - subject
      - :ref:`MolecularVariation` | :ref:`Feature` | :ref:`SequenceExpression` | `CURIE <core.json#/$defs/CURIE>`_
      - 1..1
      - Subject of the Copy Number object
   *  - copies
      - :ref:`Number` | :ref:`IndefiniteRange` | :ref:`DefiniteRange`
      - 1..1
      - The integral number of copies of the subject in a system
