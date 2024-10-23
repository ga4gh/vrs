
.. warning:: This data class is at a **draft** maturity level and may change
    significantly in future releases. Maturity levels are described in 
    the :ref:`maturity-model`.
                      
                    
**Computational Definition**

A sequence of nucleic or amino acid character codes.

**Information Model**

Some SequenceReference attributes are inherited from :ref:`gks.core-im:Entity`.

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
      - The 'logical' identifier of the Entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference an object from another.
   *  - label
      - string
      - 0..1
      - A primary name for the entity.
   *  - description
      - string
      - 0..1
      - A free-text description of the Entity.
   *  - alternativeLabels
      - string
      - 0..m
      - Alternative name(s) for the Entity.
   *  - extensions
      - :ref:`Extension`
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - type
      - string
      - 1..1
      - MUST be "SequenceReference"
   *  - refgetAccession
      - string
      - 1..1
      - A `GA4GH RefGet <http://samtools.github.io/hts-specs/refget.html>`_ identifier for the referenced sequence, using the sha512t24u digest.
   *  - residueAlphabet
      - string
      - 0..1
      - The interpretation of the character codes referred to by the refget accession, where "aa" specifies an amino acid character set, and "na" specifies a nucleic acid character set.
   *  - circular
      - boolean
      - 0..1
      - A boolean indicating whether the molecule represented by the sequence is circular (true) or linear (false).
