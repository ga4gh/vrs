
.. note:: This data class is at a **trial use** maturity level and may change
    in future releases. Maturity levels are described in the :ref:`maturity-model`.
                      
                    
**Computational Definition**

The `Adjacency` class represents the adjoining of the end of a sequence with the beginning of an adjacent sequence, potentially with an intervening linker sequence.

**Information Model**

Some Adjacency attributes are inherited from :ref:`Variation`.

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
   *  - digest
      - string
      - 0..1
      - A sha512t24u digest created using the VRS Computed Identifier algorithm.
   *  - expressions
      - :ref:`Expression`
      - 0..m
      - 
   *  - type
      - string
      - 1..1
      - MUST be "Adjacency".
   *  - adjoinedSequences
      - :ref:`IRI` | :ref:`Location`
      - 2..2
      - The terminal sequence or pair of adjoined sequences that defines in the adjacency.
   *  - linker
      - :ref:`SequenceExpression`
      - 0..1
      - The sequence found between adjoined sequences.
   *  - homology
      - boolean
      - 0..1
      - A flag indicating if coordinate ambiguity in the adjoined sequences is from sequence homology (true) or other uncertainty, such as instrument ambiguity (false).
