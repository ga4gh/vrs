.. _SequenceReference:

SequenceReference
!!!!!!!!!!!!!!!!!

.. admonition:: New in v2

    The SequenceReference class was added in v2 to leverage the new :ref:`VRS-metadata` and provide context
    to the RefGet sequence identifiers used as references in :ref:`SequenceLocation`.

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include::  ../../def/SequenceReference.rst

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

RefSeq and Ensembl Accessions
#############################

The SequenceReference class provides a convenient mechanism for describing sequences by established sequence
accessions. These accessions may be used as the content for the `SequenceReference.id`, with the refget computed
identifier (which is necessary for :ref:`computed-identifiers`) explicitly linked to the `SequenceReference.refgetAccession`.

Circular chromosomes
####################

The optional ``circular`` property may be set to ``True`` or ``False`` to explicitly indicate if a reference is
circular, and provide useful context for parent :ref:`SequenceLocation` objects for evaluating `start` and `end`
coordinate behavior.
