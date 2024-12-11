.. _resource-identifiers:

Resource Identifiers
!!!!!!!!!!!!!!!!!!!!

.. admonition:: New in v2

    In VRS v1, references to VRS objects by GA4GH :ref:`computed-identifiers` 
    were allowed in some data classes. In VRS v2, such references have been expanded to 
    include any :ref:`iriReference`, and consequently VRS now also supports references to 
    objects from classes that do not have GA4GH Computed Identifiers.

Some VRS data classes, such as the :ref:`Allele`, may reference other classes by an
:ref:`iriReference`. This enables data producers to reference other objects following
the `rfc3987`_ standard. GA4GH :ref:`computed-identifiers` may serve as IRI
references in VRS.

.. _rfc3987: https://datatracker.ietf.org/doc/html/rfc3987

**Example:**

The three Alleles below share a :ref:`SequenceLocation` and define it by reference:

.. code-block:: json

    {
        "alleles": [
            {
                "type": "Allele",
                "state": {
                    "type": "LiteralSequenceExpression",
                    "sequence": "A"
                },
                "location": "ga4gh:SL.4t6JnYWqHwYw9WzBT_lmWBb3tLQNalkT"
            },{
                "type": "Allele",
                "state": {
                    "type": "LiteralSequenceExpression",
                    "sequence": "G"
                },
                "location": "ga4gh:SL.4t6JnYWqHwYw9WzBT_lmWBb3tLQNalkT"
            },{
                "type": "Allele",
                "state": {
                    "type": "LiteralSequenceExpression",
                    "sequence": "C"
                },
                "location": "ga4gh:SL.4t6JnYWqHwYw9WzBT_lmWBb3tLQNalkT"
            }]
    }

This Sequence Location may be defined elsewhere (e.g. another API endpoint, document, or 
internal data structure) and retrievable by ID:

.. code-block:: json

    {
        "id": "ga4gh:SL.4t6JnYWqHwYw9WzBT_lmWBb3tLQNalkT",
        "type": "SequenceLocation",
        "sequenceReference": "GRCh38.chr7",
        "start": 44908821,
        "end": 44908822,
        "sequence": "T"
    }

And in turn, the :ref:`SequenceReference` object referenced by the Sequence Location:

.. code-block:: json

    {
        "id": "GRCh38.chr7",
        "label": "Chromosome 7 (build GRCh38)",
        "type": "SequenceReference",
        "refgetAccession": "SQ.F-LrLMe1SRpfUZHkQmvkVKFEGaoDeHul",
        "residueAlphabet": "na",
        "moleculeType": "genomic"
    }

A dereferenced Allele would include all of the above, nested components:

.. code-block:: json

    {
        "type": "Allele",
        "state": {
            "type": "LiteralSequenceExpression",
            "sequence": "A"
        },
        "location": {
            "id": "ga4gh:SL.4t6JnYWqHwYw9WzBT_lmWBb3tLQNalkT",
            "type": "SequenceLocation",
            "sequenceReference": {
                "id": "GRCh38.chr7",
                "label": "Chromosome 7 (build GRCh38)",
                "type": "SequenceReference",
                "refgetAccession": "SQ.F-LrLMe1SRpfUZHkQmvkVKFEGaoDeHul",
                "residueAlphabet": "na",
                "moleculeType": "genomic"
            }
            "start": 44908821,
            "end": 44908822,
            "sequence": "T"
        }
    }
