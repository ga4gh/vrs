.. _algorithms:

Algorithms
!!!!!!!!!!

The VR Specification REQUIRES implementation of the following
algorithms:

* normalization: Expands Alleles to the maximal region of
  representational ambiguity.  (Conventional left and right shuffling
  is insufficient for compliance with the specification.)
* ga4gh digest: A convention for constructing and representing digests
  from binary data for the purposes of constructing an identifier.
* ga4gh serialization: Converts objects into canonical binary forms in order
  to generate consistent digests across implementations and computing
  languages.
* ga4gh identifer: A proposed string format for object identifiers
  across all GA4GH products.


.. toctree::
   :maxdepth: 1

   digest
   identification
   normalization
   serialization
