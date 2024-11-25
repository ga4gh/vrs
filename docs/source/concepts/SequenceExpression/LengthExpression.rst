.. _LengthExpression:

Length Expression
!!!!!!!!!!!!!!!!!

.. admonition:: New in V2

A length expression is used to represent molecular sequences with known length
but unknown sequence content, typically as determined by molecular weight assays
(e.g. gel electrophoresis).

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include::  ../../def/vrs/LengthExpression.rst

Example
@@@@@@@

.. code-block:: json

  {
    "type": "LengthExpression",
    "length": 20000
  }