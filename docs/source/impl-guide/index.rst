.. _impl-guide:

Implementation Guide
!!!!!!!!!!!!!!!!!!!!

This section discusses topics relevant to implementations of the VR
Specification.

* :ref:`data-proxy`: All implementations will require access to
  sequences and sequence accessions. The Data Proxy section provides
  guidance on the abstract functionality that is required in order to
  implement VR.
* :ref:`normalization`: Expands Alleles to the maximal region of
  representational ambiguity.  (Conventional left and right shuffling
  is insufficient for compliance with the specification.)
* :ref:`computed-identifiers`: Generate globally unique identifiers
  based solely on the variation definition.



.. toctree::
   :hidden:
   :maxdepth: 1

   data_proxy
   normalization
   computed_identifier
  
