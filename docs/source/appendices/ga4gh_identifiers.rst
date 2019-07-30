.. _ga4gh-identifiers:

Proposal for GA4GH-wide Computed Identifier Standard
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

This appendix describes a proposal for creating a GA4GH-wide standard
for serializing data, computing digests on serialized data, and
constructing CURIE identifiers from the digests.  Essentially, it is a
generalization of the :doc:`../impl-guide/computed_identifier` section.

This standard is proposed now because the VR Specification needs a
well-defined mechanism for generating identifiers.  Changing the
identifier mechanism later will create significant issues for VR
adopters.


Background
@@@@@@@@@@

The GA4GH mission entails structuring, connecting, and sharing data
reliably. A key component of this effort is to be able to *identify*
entities, that is, to associate identifiers with entities. Ideally,
there will be exactly one identifier for each entity, and one entity
for each identifier.  Traditionally, identifiers are assigned to
entities, which means that disconnected groups must coordinate on
identifier assignment.

The computed identifier scheme proposed in the VR Specification
computes identifiers from the data itself.  Because identifers depend
on the data, groups that independently generate the same variation
will generate the same computed identifier for that entity, thereby
obviating centralized identifier systems and enabling identifiers to
be used in isolated settings such as clinical labs. 

The computed identifier mechanism is broadly applicable and useful to
the entire GA4GH ecosystem.  As a result, we are proposing that the
computed identifier scheme described in the VR specification be
considered for adoption as a GA4GH-wide standard.

Adopting a common identifier scheme will make interoperability of
GA4GH entities more obvious to consumers, will enable the entire
organization to share common entity definitions (such as sequence
identifiers), and will enable all GA4GH products to share tooling that
manipulate identified data.  In short, it provides an important
consistency within the GA4GH ecosystem.


Proposal
@@@@@@@@

The GA4GH computed identifier proposal consists of a truncated digest,
syntax for a GA4GH identifier, declaration of the namespace, and a
system for adminstering entity type prefixes.

* seralization
* truncated digest
* identifier GA4GH Identifier
* namespace
* type prefix administration


.. todo:: add section administration of standard and prefixes

.. todo:: move prefixes here
