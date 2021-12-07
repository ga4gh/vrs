**Computational Definition**

An expression of a sequence comprised of a tandem repeating subsequence.

**Information Model**

Some RepeatedSequenceExpression attributes are inherited from :ref:`SequenceExpression`.

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
      - 1..1
      - MUST be "RepeatedSequenceExpression"
   *  - seq_expr
      - :ref:`LiteralSequenceExpression` | :ref:`DerivedSequenceExpression`
      - 1..1
      - An expression of the repeating subsequence
   *  - count
      - :ref:`Number` | :ref:`IndefiniteRange` | :ref:`DefiniteRange`
      - 1..1
      - The count of repeated units, as an integer or inclusive range
