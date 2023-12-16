Terminology & Information Model
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

When biologists define terms in order to describe phenomena and
observations, they rely on a background of human experience and
intelligence for interpretation. Definitions may be abstract, perhaps
correctly reflecting uncertainty of our understanding at the
time. Unfortunately, such terms are not readily translatable into an
unambiguous representation of knowledge.

For example, "allele" might refer to "an alternative form of a gene or
locus" [`Wikipedia`_], "one of two or more forms of the DNA sequence
of a particular gene" [`ISOGG`_], or "one of a set of coexisting
sequence alleles of a gene" [`Sequence Ontology`_]. Even for human
interpretation, these definitions are inconsistent: does the
definition precisely describe a specific change on a specific
sequence, or, rather, a more general change on an undefined sequence?
In addition, all three definitions are inconsistent with the practical
need for a way to describe sequence changes outside regions associated
with genes.

**The computational representation of biological concepts requires
translating precise biological definitions into information models and
data structures that may be used in software.** This translation
should result in a representation of information that is consistent
with conventional biological understanding and, ideally, be able to
accommodate future data as well. The resulting *computational
representation* of information should also be cognizant of
computational performance, the minimization of opportunities for
misunderstanding, and ease of manipulating and transforming data.

Accordingly, for each term we define below, we begin by describing the
term as used by the genetics and/or bioinformatics communities as
available. When a term has multiple such definitions, we
explicitly choose one of them for the purposes of computational
modelling. We then define the **computational definition** that
reformulates the community definition in terms of information content.
Finally, we translate each of these computational definitions into precise
specifications for the (**information model**). Terms are ordered
"bottom-up" so that definitions depend only on previously-defined terms.

.. note:: The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
          NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and
          "OPTIONAL" in this document are to be interpreted as
          described in `RFC 2119`_.


Information Model Principles
@@@@@@@@@@@@@@@@@@@@@@@@@@@@

* **VRS objects are minimal** `value objects
  <https://en.wikipedia.org/wiki/Value_object>`_. Two objects are
  considered equal if and only if their respective attributes are
  equal.  As value objects, VRS objects are used as primitive types
  and MUST NOT be used as containers for related data, such as primary
  database accessions, representations in particular formats, or links
  to external data.  Instead, related data should be associated with
  VRS objects through identifiers.  See :ref:`computed-identifiers`.

* **VRS uses polymorphism.** VRS uses polymorphism extensively in
  order to provide a coherent top-down structure for variation while
  enabling precise models for variation data.  For example, Allele is
  a kind of Variation, SequenceLocation is a kind of Location, and
  SequenceState is a kind of State.  See :ref:`future-plans` for the
  roadmap of VRS data classes and relationships.  All VRS objects
  contain a ``type`` attribute, which is used to discriminate
  polymorphic objects.

* **Error handling is intentionally unspecified and delegated to
  implementation.**  VRS provides foundational data types that
  enable significant flexibility.  Except where required by this
  specification, implementations may choose whether and how to
  validate data.  For example, implementations MAY choose to validate
  that particular combinations of objects are compatible, but such
  validation is not required.

* **VRS uses** `snake_case
  <https://simple.wikipedia.org/wiki/Snake_case>`__ **to represent
  compound words.** Although the schema is currently JSON-based (which
  would typically use camelCase), VRS itself is intended to be neutral
  with respect to languages and database.

