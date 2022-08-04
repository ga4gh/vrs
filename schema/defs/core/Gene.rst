**Computational Definition**

A reference to a Gene as defined by an authority. For human genes, the use of `hgnc <https://registry.identifiers.org/registry/hgnc>`_ as the gene authority is RECOMMENDED.

**Information Model**

Some Gene attributes are inherited from :ref:`Entity`.

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
      - 1..1
      - The 'logical' identifier of the entity in the system of record, and MUST be represented as a CURIE. This 'id' is unique within a given system, but may also refer to an 'id' for the shared concept in  another system (represented by namespace, accordingly).
   *  - type
      - string
      - 1..1
      - MUST be "Gene"
