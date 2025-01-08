.. _CopyNumberCount:

Copy Number Count
!!!!!!!!!!!!!!!!!


A copy number count is used to represent the integer number of copies of
a :ref:`SequenceLocation` in a genome.

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include::  ../../def/vrs/CopyNumberCount.rst

.. _CopyNumberCount:

Example
@@@@@@@

.. code-block:: json

  {
    "id": "ga4gh:CN.ezEUXykQvIhX8jHADILwC9f8k-jp8tZC",
    "type": "CopyNumberCount",
    "copies": [3, null],
    "location": {
      "sequenceReference": {
        "refgetAccession": "SQ.jdEWLvLvT8827O59m1Agh5H3n6kTzBsJ",
        "type": "SequenceReference"
      },
      "end": 44909393,
      "start": 44905795,
      "type": "SequenceLocation"
    }
  }
