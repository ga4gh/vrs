**Computational Definition**

An assessment of the copy number of a :ref:`Location` or a :ref:`Gene` within a system (e.g. genome, cell, etc.) relative to a baseline ploidy.

**Information Model**

Some CopyNumberChange attributes are inherited from :ref:`CopyNumber`.

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
      - `Extension </ga4gh/schema/gks-common/1.x/data-types/json/Extension>`_
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
   *  - location
      - `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_ | :ref:`Location`
      - 1..1
      - A location for which the number of systemic copies is described.
   *  - type
      - string
      - 1..1
      - MUST be "CopyNumberChange"
   *  - copyChange
      - `Coding <../data-types/data-types-source.json#/$defs/Coding>`_
      - 1..1
      - MUST be a `Coding` representing one of "EFO:0030069" (complete genomic loss), "EFO:0020073" (high-level loss), "EFO:0030068" (low-level loss), "EFO:0030067" (loss), "EFO:0030064" (regional base ploidy), "EFO:0030070" (gain), "EFO:0030071" (low-level gain), "EFO:0030072" (high-level gain).
