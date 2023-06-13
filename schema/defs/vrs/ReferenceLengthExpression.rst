**Computational Definition**

An expression of a length of a sequence from a repeating reference.

**Information Model**

Some ReferenceLengthExpression attributes are inherited from :ref:`SequenceExpression`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto
   
   *  - Field
      - Type
      - Limits
      - Description
   *  - type
      - string
      - 0..1
      - MUST be "ReferenceLengthExpression"
   *  - length
      - integer | :ref:`Range`
      - 1..1
      - The number of residues in the expressed sequence.
   *  - sequence
      - :ref:`Sequence`
      - 0..1
      - the :ref:`Sequence` encoded by the Reference Length Expression.
   *  - repeatSubunitLength
      - integer
      - 0..1
      - The number of residues in the repeat subunit.
