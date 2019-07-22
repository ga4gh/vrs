.. _impl-guide:

Implementation Guide
!!!!!!!!!!!!!!!!!!!!

Implementations of the VR Specification will require the following
algorithms:

* :ref:`normalization`: Expands Alleles to the maximal region of
  representational ambiguity.  (Conventional left and right shuffling
  is insufficient for compliance with the specification.)
* :ref:`digest`: A convention for constructing and representing
  digests from binary data for the purposes of constructing an
  identifier.
* :ref:`serialization`: Converts objects into canonical binary
  forms in order to generate consistent digests across implementations
  and computing languages.
* :ref:`computed-identifier`: A proposed string format for object
  identifiers across all GA4GH products.



.. toctree::
   :hidden:
   :maxdepth: 1

   normalization
   digest
   serialization
   computed_identifier
  
