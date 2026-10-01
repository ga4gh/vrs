.. _RelativeAllele:

Relative Allele
!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include::  ../../def/vrs/RelativeAllele.rst

Example
@@@@@@@

There are several :ref:`splice-adjacent-examples` with more details.
Below is an example of a splice acceptor downstream relative allele.

.. code-block:: json

    {
      "type": "RelativeAllele",
      "relativeLocation": {
        "baseSequenceLocation": {
          "type": "SequenceLocation",
          "sequenceReference": {
            "type": "SequenceReference",
            "id": "NC_000010.11",
            "refgetAccession": "SQ.ss8r_wB0-b9r44TQTMmVTI92884QvBiB"
          },
          "start": 95387120,
          "end": 95387121
        },
        "mappedSequenceLocation": {
          "sequenceReference": {
            "type": "SequenceReference",
            "id": "NM_001034954.3",
            "refgetAccession": "SQ.SDt4gIJa8ChOmuI3te-3gpbJExmt1dHX"
          },
          "anchor": 1543,
          "anchorOrientation": "right",
          "offsetStart": -2837,
          "offsetEnd": -2836
        }
      },
      "mappedState": {
        "type": "LiteralSequenceExpression",
        "sequence": "G"
      },
      "baseState": {
        "type": "LiteralSequenceExpression",
        "sequence": "C"
      }
    }

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

Normalization
#############

The ``RelativeAllele`` also includes conventions for variant normalization (see :ref:`relative-allele-normalization`) that allows for compact and
uniform representation of relative allele variants.
