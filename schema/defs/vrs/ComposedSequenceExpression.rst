**Computational Definition**

An expression of a sequence composed from multiple other :ref:`Sequence Expressions<SequenceExpression>` objects. MUST have at least one component that is not a ref:`LiteralSequenceExpression`. CANNOT be composed from nested composed sequence expressions.

**Information Model**

Some ComposedSequenceExpression attributes are inherited from :ref:`SequenceExpression`.

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
      - MUST be "ComposedSequenceExpression"
   *  - components
      - :ref:`LiteralSequenceExpression` | :ref:`RepeatedSequenceExpression` | :ref:`DerivedSequenceExpression`
      - 2..m
      - An ordered list of :ref:`SequenceExpression` components comprising the expression.
