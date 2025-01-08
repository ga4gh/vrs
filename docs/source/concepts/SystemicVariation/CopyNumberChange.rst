.. _CopyNumberChange:

Copy Number Change
!!!!!!!!!!!!!!!!!!

A copy number change is used to represent the change in copy number of a sequence in a genome.

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include::  ../../def/vrs/CopyNumberChange.rst

Example
@@@@@@@

.. code-block:: json

  {
    "id": "ga4gh:CX.2_fT_6-IpUm5aS0wp8ZAkJ01MCE569L2",
    "type": "CopyNumberChange",
    "copyChange": "EFO:0030071",
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
