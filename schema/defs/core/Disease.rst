**Computational Definition**

A reference to a Disease as defined by an authority. For human diseases, the use of `MONDO <https://registry.identifiers.org/registry/mondo>`_ as the disease authority is RECOMMENDED.

**Information Model**

Some Disease attributes are inherited from :ref:`Entity`.

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
      - MUST be "Disease".
   *  - disease_id
      - :ref:`CURIE`
      - 1..1
      - A :ref:`CURIE` reference to a disease concept.
