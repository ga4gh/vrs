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

In VRS 2.0 we moved away from the use of CURIEs in favor of :ref:`iriReference`. Several factors played a role in 
this decision.

JSON Schema, the default data model for GKS specifications, does not allow for encoding of CURIE namespaces as is done 
in other frameworks such as JSON-LD or XML. As a result, namespaces must be captured from custom data structures, API 
endpoints, or documentation that may not persist as messages are exchanged between systems. To address this, references
in GKS specs now use IRIs to reference objects explicitly. 

IRI-References over IRIs
------------------------
We opted for the general use of IRI-References as a way to provide a more flexible approach to the use of IRIs
in most GKS message structures. IRI-references (relative IRIs) benefit the users allow for compact representation
of concepts that are accessible within a system (e.g. a directory structure or web API).

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

