.. _impl-guide:

Implementation Guide
!!!!!!!!!!!!!!!!!!!!

This section describes the data and algorithmic components that are
required for implementations of the VR Specification.

* :ref:`required-data`: All implementations will require access to
  sequences and sequence accessions. The Required External Data
  section provides guidance on the abstract functionality that is
  required in order to implement VR.
* :ref:`normalization`: Expands Alleles to the maximal region of
  representational ambiguity.  (Conventional left and right shuffling
  is insufficient for compliance with the specification.)
* :ref:`computed-identifiers`: Generate globally unique identifiers
  based solely on the variation definition.



.. toctree::
   :hidden:
   :maxdepth: 1

   required_data
   normalization
   computed_identifier
  
