**Computational Definition**

A :ref:`Location` defined by an interval on a referenced :ref:`Sequence`.

**Information Model**

Some SequenceLocation.v2 attributes are inherited from :ref:`Location.v2`.

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
   *  - start
      - :ref:`Number` | :ref:`IndefiniteRange` | :ref:`DefiniteRange`
      - 1..1
      - The start coordinate or range of the interval. The minimum value of this coordinate or range is 0. MUST represent a coordinate or range less than the value of `end`.
   *  - end
      - :ref:`Number` | :ref:`IndefiniteRange` | :ref:`DefiniteRange`
      - 1..1
      - The end coordinate or range of the interval. The minimum value of this coordinate or range is 0. MUST represent a coordinate or range greater than the value of `start`.
