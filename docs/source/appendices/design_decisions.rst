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

The VRS identifier syntax is comprised of the following components:



There has been much discussion over the idea of including a version number in the VRS identifier.





