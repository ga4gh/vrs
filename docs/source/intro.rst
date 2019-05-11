Introduction
!!!!!!!!!!!!

Maximizing the personal, public, research, and clinical value of
genomic information will require that clinicians, researchers, and
testing laboratories exchange genetic variation data reliably. This
document, written by a partnership among national information resource
providers, major public initiatives, and diagnostic testing
laboratories, proposes a specification to standardize the exchange of
variation data. Four contributions are made:

* Terminology. Definitions for biological terms may be abstract or
  intentionally ambiguous, often accurately reflecting scientific
  uncertainty or understanding at the time. Abstract and ambiguous
  terms are not readily translatable into a representation of
  knowledge. Therefore, the specification begins with precise
  computational definitions for biological concepts that are essential
  to representing sequence variation.
* Information model. The VMC information model specifies how the
  computational definitions are to be represented in terms of fields,
  semantics, objects, and object relationships.
* Machine readable schema definition. To be useful for information
  exchange, the information model should be realized in a schema
  definition language. VMC is currently implemented using JSON
  Schema. However, the construction of VMC 1 is intended to support
  translations to other schema systems, such as XML, OpenAPI, and
  GraphQL.
* Globally unique computed identifiers. This specification also
  recommends a specific algorithm for constructing distributed and
  globally-unique identifiers for genetic states. Importantly, this
  algorithm enables data providers and consumers to computationally
  generate consistent, globally unique identifiers for variation
  without a central authority.

The machine readable schema definitions and example code are available
at https://github.com/ga4gh/vr-schema.

The initial scope of VMC is purposefully limited to provide only the
most essential elements for contemporary needs for next generation
sequencing. This document includes a roadmap for adoption by key
stakeholders, recognized functional gaps in the current specification,
and a recommendation for the governance of the specification that
promotes technical collaboration and, therefore, long-term benefit to
human health through accurate data exchange.

