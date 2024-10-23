
.. warning:: This data class is at a **draft** maturity level and may change
    significantly in future releases. Maturity levels are described in 
    the :ref:`maturity-model`.
                      
                    
**Computational Definition**

The absolute count of discrete copies of a :ref:`Location` or :ref:`Gene`, within a system (e.g. genome, cell, etc.).

**Information Model**

Some CopyNumberCount attributes are inherited from :ref:`CopyNumber`.

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
   *  - location
      - :ref:`IRI` | :ref:`Location`
      - 1..1
      - A location for which the number of systemic copies is described.
   *  - type
      - string
      - 1..1
      - MUST be "CopyNumberCount"
   *  - copies
      - integer | :ref:`Range`
      - 1..1
      - The integral number of copies of the subject in a system
