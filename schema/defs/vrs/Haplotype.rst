**Computational Definition**

An ordered set of co-occurring :ref:`variants <Variation>` on the same molecule.

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
          - MUST be "Haplotype"
       *  - expressions
          - :ref:`Expression`
          - 0..m
          - 
       *  - members
          - :ref:`Adjacency` | :ref:`Allele` | `IRI <gks.common.json#/$defs/IRI>`_
          - 2..m
          - A list of :ref:`Alleles <Allele>` and :ref:`Adjacencies <Adjacency>` that comprise a Haplotype.  Members must share the same reference sequence as adjacent members. Alleles should not have overlapping or adjacent coordinates with neighboring Alleles. Neighboring alleles should be ordered  by ascending coordinates, unless represented on a DNA inversion (following an Adjacency with  end-defined adjoinedSequences), in which case they should be ordered in descending coordinates.  Sequence references MUST be consistent for all members between and including the end of one  Adjacency and the beginning of another.
