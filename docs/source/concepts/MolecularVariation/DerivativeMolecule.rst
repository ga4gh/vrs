.. _DerivativeMolecule:

Derivative Molecule
!!!!!!!!!!!!!!!!!!!

.. admonition:: New in v2
   
   The `DerivativeMolecule` class was added in v2 to describe molecules resulting from structural variation.

A derivative molecule is created by two or more adjoined molecular structures. The `DerivativeMolecule` class
may be used to represent molecules resulting from genomic rearrangements such as inversions or translocations.

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include::  ../../def/DerivativeMolecule.rst

.. _TraversalBlock:

TraversalBlock
@@@@@@@@@@@@@@

The TraversalBlock is a key component of the `DerivativeMolecule` class, and is used for resolving the
orientation of double-stranded nucleic acid molecules when assembled into a derivative molecule.

.. include:: ../../def/TraversalBlock.rst
