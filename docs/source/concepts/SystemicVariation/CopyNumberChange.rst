.. _CopyNumberChange:

Copy Number Change
!!!!!!!!!!!!!!!!!!

A copy number change is used to represent the change in copy number of a sequence in a genome.

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include::  ../../def/vrs/CopyNumberChange.rst

Copy Change term definitions
############################

The `CopyChange` attribute uses a valueset derived from the 
`Experimental Factor Ontology (EFO) <https://www.ebi.ac.uk/efo/>`_:

* **gain** (`EFO:0030070 <http://www.ebi.ac.uk/efo/EFO_0030070>`_ - *copy number gain*):
  Assessment of genomic copy number gain.
    * **high-level gain** (`EFO:0030072 <http://www.ebi.ac.uk/efo/EFO_0030072>`_ - *high-level copy number gain*):
      Assessment of high-level genomic copy number gain.
    * **low-level gain** (`EFO:0030071 <http://www.ebi.ac.uk/efo/EFO_0030071>`_ - *low-level copy number gain*):
      Assessment of low-level genomic copy number gain.
* **regional base ploidy** (`EFO:0030064 <http://www.ebi.ac.uk/efo/EFO_0030064>`_ - *regional base ploidy*):
  Copy number assessment of regional base ploidy.
* **loss** (`EFO:0030067 <http://www.ebi.ac.uk/efo/EFO_0030067>`_ - *copy number loss*):
  Assessment of genomic copy number loss.
    * **low-level loss** (`EFO:0030068 <http://www.ebi.ac.uk/efo/EFO_0030068>`_ - 
      *low-level copy number loss*): Assessment of low-level genomic copy number loss.
    * **high-level loss** (`EFO:0020073 <http://www.ebi.ac.uk/efo/EFO_0020073>`_ - 
      *high-level copy number loss*): Assessment of high-level genomic copy number loss.
        * **complete genomic loss** (`EFO:0030069 <http://www.ebi.ac.uk/efo/EFO_0030069>`_ -
          *complete genomic deletion*: Assessment of complete genomic deletion.

Example
@@@@@@@

.. code-block:: json

  {
    "id": "ga4gh:CX.2_fT_6-IpUm5aS0wp8ZAkJ01MCE569L2",
    "type": "CopyNumberChange",
    "copyChange": "low-level gain",
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
