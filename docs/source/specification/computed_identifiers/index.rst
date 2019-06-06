.. _computed-identifiers:

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

The VR Computed Identifer algorithm uses two well-established standard
algorithms, the SHA-512 hash function, which generates a binary digest
from binary data, and Base64 URL encoding, which encodes binary data
using printable characters.

To generate a VR Computed Indentifier, an implementation:

* MUST normalize the Allele, if the object is an Allele, as described in :ref:`normalization`
* MUST serialize the object into a binary string as described in :ref:`serialization`
* MUST generate a digest as described in :ref:`ga4gh-digest`
* MUST construct a CURIE Identifier as described in :ref:`identification`
* MUST NOT use any other normalization, serialization, or digest
  mechanism to generate a GA4GH Computed Identifier.


.. important:: The VR Computed Identifier algorithm applies only to *identifiable* objects, that is, objects with an `id` property.  In addition, the algorithm is defined only when nested objects use `ga4gh` identifiers.  For example, generating a Computed Identifier for an Allele requires a Computed Identifier for the embedded location, which requires that the reference sequence is defined using a Computed Identifier.

Algorithms
@@@@@@@@@@

.. toctree::
   :maxdepth: 1

   normalization
   serialization
   ga4gh_digest
   identification
