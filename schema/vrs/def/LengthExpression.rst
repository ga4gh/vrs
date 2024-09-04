**Computational Definition**

A sequence expressed only by its length.

**Information Model**

Some LengthExpression attributes are inherited from :ref:`SequenceExpression`.

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
   *  - type
      - string
      - 1..1
      - MUST be "LengthExpression"
   *  - length
      - :ref:`Range` | integer
      - 0..1
      - The length of the sequence.
