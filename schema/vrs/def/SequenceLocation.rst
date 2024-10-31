
.. note:: This data class is at a **trial use** maturity level and may change
    in future releases. Maturity levels are described in the :ref:`maturity-model`.
                      
                    
**Computational Definition**

A :ref:`Location` defined by an interval on a referenced :ref:`Sequence`.

**Information Model**

Some SequenceLocation attributes are inherited from :ref:`Ga4ghIdentifiableObject`.

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
   *  - type
      - string
      - 1..1
      - MUST be "SequenceLocation"
   *  - sequenceReference
      - :ref:`IRI` | :ref:`SequenceReference`
      - 0..1
      - A reference to a :ref:`Sequence` on which the location is defined.
   *  - start
      - integer | :ref:`Range`
      - 0..1
      - The start coordinate or range of the SequenceLocation. The minimum value of this coordinate or range is 0. MUST represent a coordinate or range less than or equal to the value of `end`.
   *  - end
      - integer | :ref:`Range`
      - 0..1
      - The end coordinate or range of the SequenceLocation. The minimum value of this coordinate or range is 0. MUST represent a coordinate or range greater than or equal to the value of `start`.
   *  - sequence
      - :ref:`SequenceString`
      - 0..1
      - The literal sequence encoded by the `sequenceReference` at these coordinates.
