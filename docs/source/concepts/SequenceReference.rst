.. _sequencereference:

SequenceReference
!!!!!!!!!!!!!!!!!

The SequenceReference class is used to refer to a sequence by its 
`refget <https://samtools.github.io/hts-specs/refget.html#refget-checksum-algorithm>`_ accession.
The class also allows implementations to optionally specify extra characteristics about the sequence,
such as the alphabet used (nucleic acid or amino acid), if the sequence represents a circular molecule,
and labels used to describe the sequence.

.. admonition:: New in v2

    In VRS v1.x, sequence references were limited to the refget sequence accession within :ref:`SequenceLocation`
    objects. This made it difficult to indicate in a message that the referenced sequence was, for example, "GRCh38 chr 11".
    The SequenceReference class was created to enable the addition of such metadata.

Definition and Information Model
################################

.. include::  ../def/SequenceReference.rst
