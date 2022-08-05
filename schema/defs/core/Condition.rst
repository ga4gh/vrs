**Computational Definition**

A set of phenotype and/or disease concepts that constitute a condition.

**Information Model**

Some Condition attributes are inherited from :ref:`Entity`.

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
      - :ref:`CURIE`
      - 0..1
      - The 'logical' identifier of the entity in the system of record, and MUST be represented as a CURIE. This 'id' is unique within a given system, but may also refer to an 'id' for the shared concept in  another system (represented by namespace, accordingly).
   *  - type
      - string
      - 1..1
      - The schema class that is instantiated by the data object. Must be the name of a class from  the VA schema.
   *  - members
      - :ref:`Disease` | :ref:`Phenotype`
      - 2..m
      - 
