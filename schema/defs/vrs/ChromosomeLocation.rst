**Computational Definition**

A Location on a chromosome defined by a species and chromosome name.

**Information Model**

Some ChromosomeLocation attributes are inherited from :ref:`Location`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto
   
   *  - Field
      - Type
      - Limits
      - Description
   *  - _id
      - :ref:`CURIE`
      - 0..1
      - Location Id. MUST be unique within document.
   *  - type
      - string
      - 1..1
      - MUST be "ChromosomeLocation"
   *  - species_id
      - :ref:`CURIE`
      - 1..1
      - :ref:`CURIE` representing a species from the `NCBI species taxonomy <https://registry.identifiers.org/registry/taxonomy>`_. Default: "taxonomy:9606" (human)
   *  - chr
      - string
      - 1..1
      - The symbolic chromosome name. For humans, For humans, chromosome names MUST be one of 1..22, X, Y (case-sensitive)
   *  - interval
      - :ref:`CytobandInterval`
      - 1..1
      - The chromosome region defined by a :ref:`CytobandInterval`
