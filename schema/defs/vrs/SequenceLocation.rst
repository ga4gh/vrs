**Computational Definition**

A :ref:`Location` defined by an interval on a referenced :ref:`Sequence`.

**Information Model**

Some SequenceLocation attributes are inherited from :ref:`Location`.

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
      - Location Id. MUST be unique within document.
   *  - type
      - string
      - 1..1
      - MUST be "SequenceLocation"
   *  - sequence_id
      - :ref:`CURIE`
      - 1..1
      - A VRS :ref:`Computed Identifier <computed-identifiers>` for the reference :ref:`Sequence`.
   *  - interval
      - :ref:`SequenceInterval` | :ref:`SimpleInterval`
      - 1..1
      - Reference sequence region defined by a :ref:`SequenceInterval`.
