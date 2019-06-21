.. _identification:

Identification
@@@@@@@@@@@@@@

VR Spec implementations MUST normalize
:ref:`Alleles <Allele>` to a fully justified ("expanded") form when
generating :ref:`computed-identifiers`.


.. warning::

   The final structure of the identifier is under active debate. This part of the implementation is subject to change prior to PRC submission. Please review accordingly, and contribute to the discussion at: https://github.com/ga4gh/vr-spec/issues/32

The final process of generating a Computed Identifier is to assemble a
CURIE-formatted identifier as follows:

    "ga4gh" ":" <prefix> "." <digest>

Example::

    ga4gh:SQ.v_QTc1p-MUYdgrRv4LMT6ByXIOsdw3C_


.. csv-table::
   :header: Prefix, Type
   :align: left

   SQ, Sequence
   VA, (Variation) Allele
   VT, (Variation) Text
   VH, reserved for Haplotype
   VG, reserved for Genotype
   VT, reserved for Translocation
