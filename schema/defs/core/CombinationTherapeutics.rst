**Computational Definition**

A collection of therapeutics that are taken during a course of treatment.

**Information Model**

Some CombinationTherapeutics attributes are inherited from :ref:`Entity`.

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
      - MUST be "CombinationTherapeutics"
   *  - members
      - :ref:`Therapeutic`
      - 0..m
      - The therapeutics that constitute the described collection.
