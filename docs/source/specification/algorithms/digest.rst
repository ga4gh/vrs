.. _digest:

Digest
!!!!!!

Computing digests for identifiable VR objects consists of three steps:

1) Computing the `SHA-512 hash function`_ digest of a :ref:`serialized <serialization>` VR object.
2) Truncating the digest to the left-most 24 bytes.
3) Encoding the truncated digest as a base64url_ string.

See :ref:`example digest <digest-example>` from the reference implementation.

.. _SHA-512 hash function: https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf
.. _base64url: https://tools.ietf.org/html/rfc4648
