.. _design_decisions:

Design Decisions
!!!!!!!!!!!!!!!!

The following design decisions were made in the development of the VRS:

GA4GH Digest 'ga4gh.inherit' over value objects
-----------------------------------------------

In VRS 1.0 we operated under the principle that all identifiable objects in VRS (e.g. Allele, SequenceLocation, etc.)
would be *true* value objects. This meant that they should be immutable and contain only required fields that are 
necessary to uniquely identify the object. This approach somewhat simplified the ability to genertate the digests by
allowing the computation of the digest to be based on the entire object.

In VRS 2.0 we deviated from this principle by allowing optional attributes to be added to VRS identifiable objects.
This was done to allow for the VRS to be more flexible, easing implementers requirements to pass useful attributes
as part of the identifiable objects without additional complexity.

As a result, we had to introduce a new field in the digest model called *ga4gh.inherit* which is described in detail
in the section on :ref: `ga4gh-inherent-properties``


IRIs over CURIEs
----------------

In VRS 2.0 we moved away from the use of CURIEs in favor of |iris| or more specifically IRI-References. Several
factors played a role in this decision.

The main decision to move away from CURIEs occurred as a result of reviwing the approach the FHIR standard 
has taken in their *CodebaleConcept* datatype. The *Coding.system* attribute uses a URI instead of namespaces. 

Using URIs instead of Namespaces when sharing data between organizations offers global uniqueness, explicitness,
and interoperability. URIs avoid the ambiguity and context dependency of namespaces, align with modern web
standards, and ensure seamless integration across heterogeneous and distributed systems. These advantages make
URIs the superior choice for robust, scalable, and interoperable communication.

Choosing to use IRIs over URIs was made because IRIs provide a more inclusive, flexible, and user-friendly
approach to data sharing than URIs, particularly in internationalized or multilingual contexts. By supporting
Unicode characters, IRIs reduce complexity, enhance readability, and align with modern web standards, making
them the preferred choice for global data exchange.



IRI-References over IRIs
------------------------
We opted for the general use of IRI-References as a way to provide a more flexible approach to the use of IRIs
in the VRS and GKS messages. IRI-references (relative IRIs) benefit the users be allowing efficient, localized
references within a document or local document system. IRI-References do not prohibit the use of absolute IRIs
and can be easily converted to absolute IRIs when needed. 


VRS identifier syntax and versioning
------------------------------------

The :ref: `versioning` section describes the versioning and release naming conventions for the VRS product.
Approved releases will be assigned to the version number alone, but connect, ballot and snapshot releases will
include the context term and date in addition to the target version number. 

During the GA4GH Connect April 2023 meeting the maturity model was discussed at length and the following
proposal was presented for naming release version in the VRS identifier.

.. image:: ../_static/vrs_identifier_syntax.png
   :alt: VRS Identifier Syntax
   :align: center

As an example, the Github JSON Schema URL ($id) for the VRS 2.0.0 Allele is:

.. code-block:: json

  {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://w3id.org/ga4gh/schema/vrs/2.0.0/json/Allele",
    ...
  }

During the "release and versioning" discussion at the GA4GH Connect April 2023 meeting the proposal
delved into the idea of including the major version number in the VRS identifier itself. Concern for the
change in digests (and their derived identifiers) between major versions of the same VRS object will
be clearly visible in the identifier itself if the major version is included in the identifier.

The trade-off is that new identifiers would be required for every type of VRS object for every major
version release. Meaning that even if a given type of object has no change that would result in a new
digest, a new identifier would still be required for the new major version.

After much discussion, the decision was made to not include the major version number in the VRS identifier
itself. Therefore, the :ref: `identifier-construction` does NOT contain the version number as follows:

CURIE namespace resolution
  ga4gh:VA.Oop4kjdTtKcg1kiZjIJAAR3bp7qi4aNT

URI Syntax
  https://w3id.org/ga4gh/vrs/VA.Oop4kjdTtKcg1kiZjIJAAR3bp7qi4aNT

