.. _Terminus:

Terminus
!!!!!!!!

.. admonition:: New in v2

   The Terminus class was added in v2 to describe molecules resulting from structural variation.

Terminus is a data class for describing the termination of a molecule, typically
resulting from genomic rearrangements such as inversions or translocations.

Definition and Information Model
################################

.. include::  ../../def/vrs/Terminus.rst

Example
#######

.. code-block:: json

   {
      "id": "ga4gh:TM.8xpg7Q826fQJJ_6rImuqufhTXj0mh5gV",
      "type": "Terminus"
      "location": {
         "end": 44908822,
         "start": 44908821,
         "sequenceReference": {
            "refgetAccession": "SQ.F-LrLMe1SRpfUZHkQmvkVKFEGaoDeHul",
            "type": "SequenceReference"
         },
         "type": "SequenceLocation"
      }
   }