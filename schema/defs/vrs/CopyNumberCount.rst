**Computational Definition**

The absolute count of discrete copies of a :ref:`Location` or :ref:`Feature`, within a system (e.g. genome, cell, etc.).

**Information Model**

Some CopyNumberCount attributes are inherited from :ref:`Variation`.

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
      - :ref:`CURIE`
      - 0..1
      - Variation Id. MUST be unique within document.
   *  - type
      - string
      - 1..1
      - MUST be "CopyNumberCount"
   *  - subject
      - :ref:`Location` | :ref:`CURIE` | :ref:`Feature`
      - 1..1
      - A location for which the number of systemic copies is described.
   *  - copies
      - :ref:`Number` | :ref:`IndefiniteRange` | :ref:`DefiniteRange`
      - 1..1
      - The integral number of copies of the subject in a system
