**Computational Definition**

A quantified set of _in-trans_ :ref:`MolecularVariation` at a genomic locus.

    **Information Model**
    
Some Genotype attributes are inherited from :ref:`Variation`.

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
          - `Extension <gks.common.json#/$defs/Extension>`_
          - 0..m
          - 
       *  - digest
          - string
          - 0..1
          - A sha512t24u digest created using the VRS Computed Identifier algorithm.
       *  - type
          - string
          - 0..1
          - MUST be "Genotype"
       *  - expressions
          - :ref:`Expression`
          - 0..m
          - 
       *  - members
          - :ref:`GenotypeMember`
          - 1..m
          - Each GenotypeMember in `members` describes a :ref:`MolecularVariation` and the count of that variation at the locus.
       *  - count
          - integer | :ref:`Range`
          - 1..1
          - The total number of copies of all :ref:`MolecularVariation` at this locus, MUST be greater than or equal to the sum of :ref:`GenotypeMember` copy counts. If greater than the total counts, this implies additional :ref:`MolecularVariation` that are expected to exist but are not explicitly indicated.
