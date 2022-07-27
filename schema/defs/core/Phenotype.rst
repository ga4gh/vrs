**Computational Definition**

A reference to a Phenotype as defined by an authority. For human phenotypes, the use of `HPO <https://registry.identifiers.org/registry/hpo>`_ as the disease authority is RECOMMENDED.

**Information Model**

Some Phenotype attributes are inherited from :ref:`Entity`.

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
      - MUST be "Phenotype".
   *  - phenotype_id
      - :ref:`CURIE`
      - 1..1
      - A :ref:`CURIE` reference to a phenotype concept.
