**Computational Definition**

A class for expressing the count of a specific :ref:`MolecularVariation` present _in-trans_ at a genomic locus represented by a :ref:`Genotype`.

    **Information Model**
    
Some GenotypeMember attributes are inherited from :ref:`ValueObject`.

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
       *  - count
          - :ref:`Range` | integer
          - 1..1
          - The number of copies of the `variation` at a :ref:`Genotype` locus.
       *  - variation
          - :ref:`Allele` | :ref:`Haplotype`
          - 1..1
          - A :ref:`MolecularVariation` at a :ref:`Genotype` locus.
