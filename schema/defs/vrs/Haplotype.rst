**Computational Definition**

A set of non-overlapping :ref:`Allele` members that co-occur on the same molecule.

    **Information Model**
    
Some Haplotype attributes are inherited from :ref:`Variation`.

    .. list-table::
       :class: clean-wrap
       :header-rows: 1
       :align: left
       :widths: auto
       
       *  - Field
          - Type
          - Limits
          - Description
       *  - id
          - string
          - 0..1
          - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is  unique within a given system. The identified entity may have a different 'id' in a different  system, or may refer to an 'id' for the shared concept in another system (e.g. a CURIE).
       *  - label
          - string
          - 0..1
          - A primary label for the entity.
       *  - description
          - string
          - 0..1
          - A free-text description of the entity.
       *  - extensions
          - `Extension <core.json#/$defs/Extension>`_
          - 0..m
          - 
       *  - digest
          - string
          - 0..1
          - A sha512t24u digest created using the VRS Computed Identifier algorithm.
       *  - type
          - string
          - 1..1
          - MUST be "Haplotype"
       *  - expressions
          - :ref:`Expression`
          - 0..m
          - 
       *  - members
          - :ref:`Allele` | `IRI <core.json#/$defs/IRI>`_
          - 2..m
          - A list of :ref:`Alleles <Allele>` (or IRI references to `Alleles`) that comprise a Haplotype. Since each `Haplotype` member MUST be an `Allele`, and all members MUST share a common :ref:`SequenceReference`, implementations MAY use a compact representation of Haplotype that omits type and :ref:`SequenceReference` information in individual Haplotype members. Implementations MUST transform compact `Allele` representations into an `Allele` when computing GA4GH identifiers.
