Special Purpose Types
@@@@@@@@@@@@@@@@@@@@@

.. _SequenceExpression:

Sequence Expressions
@@@@@@@@@@@@@@@@@@@@@@

VRS provides several syntaxes for expressing a sequence,
collectively referred to as *Sequence Expressions*. They are:

* :ref:`LiteralSequenceExpression`: An explicit :ref:`Sequence`.
* :ref:`ReferenceLengthExpression`: TBD
* :ref:`LengthExpression`: 

Some SequenceExpression instances may appear to resolve to the same
sequence, but are intended to be semantically distinct. There MAY be
reasons to select or enforce one form over another that SHOULD be
managed by implementations. See discussion on :ref:`equivalence`.

.. include:: ../defs/SequenceExpression.rst

.. _ReferenceLengthExpression:

ReferenceLengthExpression
#########################

A ReferenceLengthExpression ...

.. include:: ../defs/ReferenceLengthExpression.rst

**Examples**

.. parsed-literal::

    tbd

.. _LengthExpression:

LengthExpression
################

A LengthExpression ...

.. include:: ../defs/LengthExpression.rst

**Examples**

.. parsed-literal::

    tbd

.. _LiteralSequenceExpression:

LiteralSequenceExpression
#########################

A LiteralSequenceExpression "wraps" a string representation of a
sequence for parallelism with other SequenceExpressions.

.. include:: ../defs/LiteralSequenceExpression.rst

**Examples**

.. parsed-literal::

    {
      "sequence": "ACGT",
      "type": "LiteralSequenceExpression"
    }


.. _SequenceReference:

Sequence Reference
@@@@@@@@@@@@@@@@@@

tbd

.. include:: ../defs/SequenceReference.rst

.. _genotypemember:

GenotypeMember
@@@@@@@@@@@@@@

.. include:: ../defs/GenotypeMember.rst