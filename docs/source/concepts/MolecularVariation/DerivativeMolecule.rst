.. _DerivativeMolecule:

Derivative Molecule
!!!!!!!!!!!!!!!!!!!

.. admonition:: New in v2
   
   The `DerivativeMolecule` class was added in v2 to describe molecules resulting from structural variation.

A derivative molecule is created by two or more adjoined molecular structures. The `DerivativeMolecule` class
may be used to represent molecules resulting from genomic rearrangements such as inversions or translocations.

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include::  ../../def/vrs/DerivativeMolecule.rst

Components
@@@@@@@@@@

.. _TraversalBlock:

Traversal Block
###############

The TraversalBlock is a key component of the `DerivativeMolecule` class, and is used for resolving the
orientation of double-stranded nucleic acid molecules when assembled into a derivative molecule.

.. include:: ../../def/vrs/TraversalBlock.rst

Example
@@@@@@@

.. code-block:: json

   {
      "id": "ga4gh:DM.wthhP9ryLEU1ueo6V25gqbSVJC8H4z-M",
      "type": "DerivativeMolecule",
      "components": [
         {
            "type": "TraversalBlock",
            "orientation": "forward",
            "component": {
               "type": "Adjacency",
               "linker": {
                  "type": "LiteralSequenceExpression",
                  "sequence": "GTC"
               },
               "adjoinedSequences": [
                  {
                     "type": "SequenceLocation",
                     "sequenceReference": {
                        "type": "SequenceReference",
                        "refgetAccession": "SQ.S_KjnFVz-FE7M0W6yoaUDgYxLPc1jyWU",
                        "residueAlphabet": "na",
                        "id": "NC_000001.10"
                     },
                     "end": 123
                  },
                  {
                     "type": "SequenceLocation",
                     "sequenceReference": {
                        "type": "SequenceReference",
                        "refgetAccession": "SQ.9KdcA9ZpY1Cpvxvg8bMSLYDUpsX6GDLO",
                        "residueAlphabet": "na",
                        "id": "NC_000002.11"
                     },
                     "start": 500
                  }
               ]
            }
         },
         {
            "type": "TraversalBlock",
            "orientation": "forward",
            "component": {
               "type": "Adjacency",
               "adjoinedSequences": [
                  {
                     "type": "SequenceLocation",
                     "end": 15000
                  },
                  {
                     "type": "SequenceLocation",
                     "sequenceReference": {
                        "type": "SequenceReference",
                        "refgetAccession": "SQ.S_KjnFVz-FE7M0W6yoaUDgYxLPc1jyWU",
                        "residueAlphabet": "na",
                        "id": "NC_000001.10"
                     },
                     "start": 10000
                  }
               ]
            }
         }
      ]
   }
