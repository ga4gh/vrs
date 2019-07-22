.. _serialization:

Serialization
!!!!!!!!!!!!!

In the context of generating a Computed Identifier, serialization
converts a VR object into a binary representation.  Because the result
will be used to generate a digest, VR implementations MUST serialize
data identically.  The VR-Spec provides validation tests to ensure
compliance.

The criteria for the VR serialization method was that it must be
relatively easy and reliable to implement in any common computer
language.  Although several proposals exist [1]_:superscript:`,`
[2]_:superscript:`,` [3]_ for serializing arbitrary data in a
consistent manner, none have been ratified. As a result, VR-Spec
defines a custom serialization format that is consistent with these
proposals but does not rely on them for definition.

The first step in serialization is to generate message content that:

    * MUST replace nested identifiable objects (i.e., objects that
      have id properties) with their corresponding ids
    * MUST order arrays of Ids by Unicode Character Set values
    * MUST require that all arrays of ids are CURIE formatted and use the
      `ga4gh` namespace prefix
    * MUST NOT include id fields
    * MUST NOT include null values


The second step is to serialize the message content as JSON that:

    * MUST be encoded in UTF-8
    * MUST NOT include insignificant whitespace, as defined in `RFC8259§2
      <https://tools.ietf.org/html/rfc8259#section-2>`__
    * MUST order all keys by Unicode Character Set values
    * MUST use two-char escapes when available, as defined in `RFC8259§7
      <https://tools.ietf.org/html/rfc8259#section-7>`__



**References**

.. [1] `Gibson Canonical JSON <http://gibson042.github.io/canonicaljson-spec/>`__
.. [2] `OLPC Canonical JSON <http://wiki.laptop.org/go/Canonical_JSON>`__
.. [3] `JSON Canonicalization Scheme <https://tools.ietf.org/html/draft-rundgren-json-canonicalization-scheme-05>`__
       
