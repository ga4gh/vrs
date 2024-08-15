.. _ReferenceLengthExpression:

Reference Length Expression
!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. admonition:: New in v2

    The `ReferenceLengthExpression` class is new in VRS v2, and was designed as a means for 
    compact encoding of large ambiguous sequence states following VOCA normalization.

Reference length expressions are used for expressing the state of :ref:`Alleles<Allele>`
where normalization results in a state other than an unambiguous indel or complete deletion
(where `length` = 0). This feature allows for compact representation of the sequence as an
expression of a reference subsequence that can be expanded or contracted to the designated
length to result in the sequence state. See :ref:`allele-normalization` for more details.

Reference length expressions also allow for the optional expression of the literal sequence
derived from the reference in cases where it is convenient to do so.

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include::  ../../def/ReferenceLengthExpression.rst
