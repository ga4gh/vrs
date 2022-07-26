**Computational Definition**

A re-usable structure that encapsulates provenance metadata that applies to a specific concrete record of information as encoded in a particular system, as opposed to  provenance of the abstract information content/knowledge the record represents.

**Information Model**

Some RecordMetadata attributes are inherited from :ref:`Entity`.

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
      - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is  unique within a given system. The identified entity may have a different 'id' in a different  system.
   *  - type
      - string
      - 1..1
      - MUST be "RecordMetadata".
   *  - is_version_of
      - :ref:`CURIE`
      - 0..1
      - 
   *  - version
      - string
      - 0..1
      - 
