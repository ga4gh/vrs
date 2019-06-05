.. _ga4gh-digest:

GA4GH Digest
!!!!!!!!!!!!

.. warning::

   The encoding of the digest is currently under debate, as it is highly similar (but not identical) to the `refget Checksum Algorithm`_. This part of the implementation is subject to change prior to PRC submission. Please review accordingly, and contribute to the discussion at: https://github.com/ga4gh/vr-spec/issues/58

The `ga4gh_digest` algorithm is a method for generating and
representing digests.  It is based on 

 — [SHA-512]_ hashing and [Base64]_ encoding — 


.. [SHA-512] `NIST FIPS 180-4 <https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf>`__
.. [Base64] `Base64 https://tools.ietf.org/html/rfc4648 <https://tools.ietf.org/html/rfc4648>`__
.. _refget Checksum Algorithm: https://samtools.github.io/hts-specs/refget.html#refget-checksum-algorithm
