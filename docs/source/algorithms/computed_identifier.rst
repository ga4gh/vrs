.. _computed-identifier:

Computed Identifier
!!!!!!!!!!!!!!!!!!!

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

The VR Computed Identifier algorithm applies only to *identifiable*
objects, that is, objects with an `id` property.  In addition, the
algorithm is defined only when nested objects use `ga4gh` identifiers.
For example, generating a Computed Identifier for an Allele requires a
Computed Identifier for the embedded location, which requires that the
reference sequence is defined using a Computed Identifier.

To generate a VR Computed Identifier, an implementation MUST:

* if the object is an Allele, normalize as described in
  :ref:`normalization`
* serialize the object into a binary string as described in
  :ref:`serialization`
* generate a :ref:`digest`
* construct a CURIE Identifier, described below

In addition, the VR Computed Identifier is explicitly NOT defined
(that is, invalid) if used with any other normalization,
serialization, or digest mechanism to generate a GA4GH Computed
Identifier.


Identifier Construction
@@@@@@@@@@@@@@@@@@@@@@@

A `W3C CURIE <curie-spec>`_ format has the form::

    prefix ":" reference

The GA4GH VR Spec constructs computed identifiers as follows::

    "ga4gh" ":" <type_prefix> "." <digest>

Type prefixes used by VR are:

.. csv-table::
   :header: type_prefix, VR Spec class name
   :align: left

   SQ, Sequence
   VA, Allele
   VL, Location
   VT, Text
   VH, (reserved) Haplotype
   VG, (reserved) Genotype
   VT, (reserved) Translocation

For example::

    ga4gh:SQ.v_QTc1p-MUYdgrRv4LMT6ByXIOsdw3C_


.. note:: Do not confuse the W3C CURIE `prefix` ("ga4gh" in this case)
          with a prefix used to indicate type.




.. note:: **Proposal for GA4GH-wide use**

	  The Variation Representation team created the computed
          identifier scheme for VR objects.  However, this scheme is
          applicable and useful to the entire GA4GH ecosystem.  As a
          result, we are proposing that the computed identifier scheme
          described here be considered for adoption as a GA4GH-wide
          standard.  For this reason, we have adopted the use of the
          `ga4gh` prefix above. 

	  If the Computed Identifier scheme is adopted as a GA4GH-wide
	  standard, documentation and type prefixes would moved from
	  the VR specification to a separate repository for GA4GH-wide
	  use.
