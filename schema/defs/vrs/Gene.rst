**Computational Definition**

A reference to a Gene as defined by an authority. For human genes, the use of `hgnc <https://registry.identifiers.org/registry/hgnc>`_ as the gene authority is RECOMMENDED.

**Information Model**

Some Gene attributes are inherited from :ref:`Feature`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto
   
   *  - Field
      - Type
      - Limits
      - Description
   *  - type
      - string
      - 1..1
      - MUST be "Gene"
   *  - gene_id
      - :ref:`CURIE`
      - 1..1
      - A CURIE reference to a Gene concept
