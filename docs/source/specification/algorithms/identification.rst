.. _identification:

Identification
@@@@@@@@@@@@@@

Computed Identifiers
!!!!!!!!!!!!!!!!!!!!

The VR-Spec provides an algorithmic solution to deterministically
generate a globally unique identifier from a VR object itself. All
valid implementations of the VR Computed Identifier will generate the
same identifier when the objects are identical, and will generate
different identifiers when they are not. Adopting the VR Computed
Digest algorithm obviates centralized registration services, allows
computational pipelines to generate ids in isolation of other systems,
and makes it easier for distributed groups to share data.

The VR Computed Identifier algorithm uses two well-established standard
algorithms, the SHA-512 hash function, which generates a binary digest
from binary data, and Base64 URL encoding, which encodes binary data
using printable characters.

To generate a VR Computed Identifier, an implementation:

* MUST normalize the Allele, if the object is an Allele, as described in :ref:`normalization`
* MUST serialize the object into a binary string as described in :ref:`serialization`
* MUST generate a :ref:`digest`
* MUST construct a CURIE Identifier as described in :ref:`identification`
* MUST NOT use any other normalization, serialization, or digest
  mechanism to generate a GA4GH Computed Identifier.


.. important:: The VR Computed Identifier algorithm applies only to *identifiable* objects, that is, objects with an `id` property.  In addition, the algorithm is defined only when nested objects use `ga4gh` identifiers.  For example, generating a Computed Identifier for an Allele requires a Computed Identifier for the embedded location, which requires that the reference sequence is defined using a Computed Identifier.




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
