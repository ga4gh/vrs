**Computational Definition**

A molecule derived from segments of multiple adjoined molecular sequences, typically resulting from structural variation.

**Information Model**

Some DerivativeMolecule attributes are inherited from :ref:`Variation`.

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
      - `Extension </ga4gh/schema/gks-common/1.0.0-ballot.2024.08.1/data-types/json/Extension>`_
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
      - MUST be "DerivativeMolecule".
   *  - components
      - `IRI </ga4gh/schema/gks-common/1.0.0-ballot.2024-08.1/data-types/json/IRI>`_ | :ref:`TraversalBlock`
      - 2..m
      - The molecular components that constitute the derivative molecule.
   *  - circular
      - boolean
      - 0..1
      - A boolean indicating whether the molecule represented by the sequence is circular (true) or linear (false).
