.. _design_decisions:

Design Decisions
!!!!!!!!!!!!!!!!

The following design decisions were made in the development of the VRS:

GA4GH Inherent Properties over Value Objects
--------------------------------------------

In VRS 1.0 we operated under the principle that all identifiable objects in VRS (e.g. Allele, SequenceLocation, etc.)
would be *value objects*. This meant that they should be immutable and contain only required fields that are 
necessary to uniquely identify the object. This approach somewhat simplified the ability to genertate the digests by
allowing the computation of the digest to be based on the entire object. An exception was made for properties with a
leading underscore (namely, the *_id* property), which was removed from the object before a digest was calculated.

In VRS 2.0 we extended the principle of excepting designated attributes by explicitly defining *inherent properties*
that constitute the properties used to compute an object digest. This was done to enable expressivity of VRS, 
enabling implementations to pass common, descriptive metadata as part of the identifiable objects without sacrificing 
the ability to create globally unique, federated identifiers from VRS 1.3.

As a result, we had to introduce a new field in the digest model called *ga4gh.inherent* which is described in detail
in the section on :ref:`ga4gh-inherent-properties`.

IRIs over CURIEs
----------------

In VRS 2.0 we moved away from the use of CURIEs in favor of |iris| or more specifically IRI-References. Several
factors played a role in this decision.

The main decision to move away from CURIEs occurred as a result of reviwing the approach the FHIR standard 
has taken in their *CodeableConcept* datatype. The *Coding.system* attribute uses a URI instead of namespaces. 

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

The :ref:`versioning` section describes the versioning and release naming conventions for the VRS product.
Approved releases will be assigned to the version number alone, but connect, ballot and snapshot releases will
include the context term and date in addition to the target version number. 

During the GA4GH Connect April 2023 meeting the maturity model was discussed at length and the following
proposal was presented for instance and class GKS identifiers.

.. image:: ../images/2023-connect-gks-identifier-proposal.png
   :alt: GKS Identifiers Proposal from 2023 April Connect Session
   :align: center

As an example, the Github JSON Schema URL ($id) for the VRS 2.0.0 Allele is:

.. code-block:: json

  {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://w3id.org/ga4gh/schema/vrs/2.0.0/json/Allele",
    ...
  }

During the **release and versioning** discussion at the GA4GH Connect April 2023 meeting the proposal
delved into the idea of including the major version number in the VRS identifier itself. Concern for the
change in digests (and their derived identifiers) between major versions of the same VRS object will
be clearly visible in the identifier itself if the major version is included in the identifier.

The trade-off is that new identifiers would be required for every type of VRS object for every major
version release. Meaning that even if a given type of object has no change that would result in a new
digest, a new identifier would still be required for the new major version.

After much discussion, the decision was made to not include the major version number in the VRS identifier
itself. Therefore, the :ref:`identifier-construction` does NOT contain the version number as follows:

**CURIE namespace resolution**

.. code-block::

  ga4gh:VA.Oop4kjdTtKcg1kiZjIJAAR3bp7qi4aNT

**URI Syntax**

.. code-block::

  https://w3id.org/ga4gh/vrs/VA.Oop4kjdTtKcg1kiZjIJAAR3bp7qi4aNT

