.. _Allele:

Allele
!!!!!!

The allele class is used for representing contiguous changes on a reference sequence. This class covers the most 
commonly described forms of variation, including all "small" variants such as SNVs and indels that are also representable 
in other contemporary genomic variant formats, such as SPDI, HGVS, and VCF.

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include::  ../../def/vrs/Allele.rst

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

Sequence Location Coordinates
#############################

The ``location`` property of the allele will almost always have ``start`` and ``end`` coordinates that are specified using
integers (not :ref:`Range`). There are some situations, such as the detection of deleted sequence by microarray, where it may
be appropriate to represent the variant as an Allele; however, other classes for representing such findings should also be
considered (e.g. :ref:`CopyNumberCount`).

Normalization
#############

The ``Allele`` also includes conventions for variant normalization (see :ref:`allele-normalization`) that allows for compact and 
uniform representation of variants.

.. admonition:: New in v2

    In VRS v1.x, normalization included methods for full justification of variants, as derived from the NCBI `VOCA`_ algorithm.
    In v2, this has been extended to include reference length encoding (see :ref:`ReferenceLengthExpression`), to 
    accommodate compressed representation of variants that occur in large repetitive regions.

    For alleles in small repeating regions, it may be convenient to also use the ``ReferenceLengthExpression.sequence`` attribute
    to represent the sequence state explicitly alongside the reference encoding.

.. _VOCA: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7523648/

Expressions
###########

.. admonition:: New in v2

    The v2 :ref:`variation` classes now support :ref:`expressions`. This is a convenient mechanism for annotating Alleles using
    string syntaxes following the conventions other variant standards (e.g. HGVS, SPDI) and resources (e.g. ClinVar, gnomAD).