**Computational Definition**

A Location on a chromosome defined by a species and chromosome name.

**Information Model**

Some ChromosomeLocation attributes are inherited from :ref:`Entity`.

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
      - `CURIE <core.json#/$defs/CURIE>`_
      - 0..1
      - The 'logical' identifier of the entity in the system of record, and MUST be represented as a CURIE. This 'id' is unique within a given system, but may also refer to an 'id' for the shared concept in  another system (represented by namespace, accordingly).
   *  - type
      - string
      - 1..1
      - MUST be "ChromosomeLocation"
   *  - species_id
      - `CURIE <core.json#/$defs/CURIE>`_
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
