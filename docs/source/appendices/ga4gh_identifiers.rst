.. _ga4gh-identifiers:

GA4GH Computed Identifier Alignment
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

This appendix describes alignment on standard practices for
for serializing data, computing digests on serialized data, and
constructing CURIE identifiers from the digests.  Essentially, it is a
generalization of the :ref:`computed-identifiers` section.

This mechanism for generating identifiers has been in place
since VRS version 1.0.

Background
@@@@@@@@@@

The GA4GH mission entails structuring, connecting, and sharing data
reliably. A key component of this effort is to be able to *identify*
entities, that is, to associate identifiers with entities. Ideally,
there will be exactly one identifier for each entity, and one entity
for each identifier.  Traditionally, identifiers are assigned to
entities, which means that disconnected groups must coordinate on
identifier assignment.

The computed identifier scheme used in VRS computes identifiers 
from the data itself.  Because identifers depend on the data, groups 
that independently generate the same variation will generate the same 
computed identifier for that entity, thereby obviating centralized 
identifier systems and enabling identifiers to be used in isolated 
settings such as clinical labs. 

The computed identifier mechanism is broadly applicable and useful to
the entire GA4GH ecosystem.  Adopting a common identifier scheme will
make interoperability of GA4GH entities more obvious to consumers,
will enable the entire organization to share common entity definitions
(such as sequence identifiers), and will enable all GA4GH products to
share tooling that manipulate identified data.  In short, it provides
an important consistency within the GA4GH ecosystem.

Here we detail alignment between VRS and other GA4GH products to work
towards consistent approaches to identifier design.

VRS Convention
@@@@@@@@@@@@@@

The following algorithmic processes, described in depth in the VRS
:ref:`computed-identifiers` convention, are included in this overview by
reference:

* **GA4GH Digest Serialization** is the process of converting an
  object to a canonical binary form based on JSON and the `RFC 8785`_
  specification. This strategy was chosen for its visibility as an
  independent standard (not IETF-endorsed) on the IETF site, and the
  selection of this standard by the Sequence Collections draft standard.
* **GA4GH Truncated Digest** is a convention for using `SHA-512`_,
  truncated to 24 bytes, and encoding using `base64url`_. This convention
  is shared with the `RefGet v2.0`_ specification.
* **GA4GH Identification** is the CURIE-based syntax for constructing
  a namespaced and typed identifier for an object. This convention is
  shared with the `RefGet v2.0`_ specification, and the identifier syntax
  has been approved by `GA4GH TASC`_.

.. _RefGet v2.0: https://samtools.github.io/hts-specs/refget.html#refget-checksum-algorithm
.. _GA4GH TASC: https://github.com/ga4gh/TASC/issues/16
.. _RFC 8785: https://www.rfc-editor.org/rfc/rfc8785


.. _ga4gh-digest-keys:

GA4GH Digest Keys
#################
When creating computed identifiers from objects, VRS uses a custom schema
attribute, ``ga4ghDigest``, that contains the keys used for filtering out 
properties. For example, the Allele JSON Schema:

.. parsed-literal::

  {
   "$schema": "https://json-schema.org/draft/2020-12/schema",
   "$id": "https://w3id.org/ga4gh/schema/vrs/2.x/json/Allele",
   "title": "Allele",
   "type": "object",
   "maturity": "draft",
   "ga4ghDigest": {
      "prefix": "VA",
      "keys": [
         "location",
         "state",
         "type"
      ]
   },
   "description": "The state of a molecule at a Location.",
   "properties": {
      ...

.. note::

  The `ga4ghDigest` property names are currently being aligned with the Sequence 
  Collections effort (see `SeqCol#84 <https://github.com/ga4gh/refget/issues/84>`_) 
  and may potentially change.

GA4GH Type Prefixes
@@@@@@@@@@@@@@@@@@@

A GA4GH identifier is constructed according to this syntax::

  "ga4gh" ":" type_prefix "." digest

The `digest` is computed as described above. The type_prefix is a
short alphanumeric code that corresponds to the type of object being
represented.

We use the following guidelines for type prefixes:

* Prefixes SHOULD be short, approximately 2-4 characters.
* Prefixes SHOULD be used only for concrete classes, not abstract parent classes.
* Prefixes SHOULD be used only for stand-alone classes (e.g. :ref:`Variation`, :ref:`Location`), 
  not classes that require additional context to be meaningful (e.g. :ref:`Range`, :ref:`SequenceExpression`)
  or are primarily used for adding descriptive context to external data types (e.g. :ref:`SequenceReference`) 
* A prefix MUST map 1:1 with a schema.

Administration
##############

Type prefix administration is to be managed by the `GA4GH TASC`_.
