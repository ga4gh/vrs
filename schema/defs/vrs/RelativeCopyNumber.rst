**Computational Definition**

The relative copies of a :ref:`MolecularVariation`, :ref:`Feature`, :ref:`SequenceExpression`, or a :ref:`CURIE` reference against an unspecified baseline in a system (e.g. genome, cell, etc.).

**Information Model**

Some RelativeCopyNumber attributes are inherited from :ref:`Variation`.

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
      - MUST be "RelativeCopyNumber"
   *  - subject
      - :ref:`SequenceLocation` | :ref:`Feature`
      - 1..1
      - Subject of the Copy Number object
   *  - relative_copy_class
      - string
      - 1..1
      - MUST be one of "complete loss", "partial loss", "copy neutral", "low-level gain" or "high-level gain".
