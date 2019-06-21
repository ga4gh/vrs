.. _digest:

Digest
!!!!!!

Computing digests for identifiable VR objects consists of three steps:

1. Compute the `SHA-512`_ digest of a binary object.
2. Truncate the digest to the left-most 24 bytes (192 bits).  See
   `FIPS-180 <SHA-512>`_ page 27 for details.
3. Encode the truncated digest as a base64url_ ASCII string.


.. code-block:: python

   >>> import base64, hashlib
   >>> blob = b"ACGT"
   >>> digest = hashlib.sha512(blob).digest()
   >>> digest
   b'h\xa1x\xf7\xc7@\xc5\xc2@\xaag\xbaA\x84;\x11\x9d;\xf9\xf8 ...
   >>> base64.urlsafe_b64encode(digest[:24]).decode("ASCII")
   'aKF498dAxcJAqme6QYQ7EZ07-fiw8Kw2'
