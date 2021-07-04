.. _glossary:

Glossary
!!!!!!!!

.. glossary::

   computed identifier
      An identifier that is *generated* from the object's data.
      Multiple groups who generated `computed identifiers` the same
      way will generate the same identifier for the same underlying
      data.

   digest, ga4gh_digest
      A digest is a digital fingerprint of a block of binary data.  A
      digest is always the same size, regardless of the size of the
      input data.  It is statistically extremely unlikely for two
      fingerprints to match when the underlying data are distinct. 

   identifiable object
      An identifiable object in VRS is any data structure for
      which VRS defines a serialization method, which is the
      precursor to generating a computational digest. All
      Sequence, Location, and Variation types are identifiable.

   serialization
     The process of converting an object in memory into a stream of
     bytes that may be sent via the network, saved in a database, or
     written to a file.
