.. _impl-guide:

Implementation Guide
!!!!!!!!!!!!!!!!!!!!

This section discusses topics that implementations of the VR
Specification must address.


* :ref:`data-proxy`: All implementations will require access to
  sequences and sequence accessions. The Data Proxy section provides
  guidance on the abstract functionality that is required in order to
  implement VR.
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

   data_proxy
   normalization
   digest
   serialization
   computed_identifier
  
