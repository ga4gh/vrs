**Computational Definition**

A Location on a human chromosome defined by cytogenetic markers.

**Information Model**

Some CytogenomicLocation.v2 attributes are inherited from :ref:`Location.v2`.

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
      - MUST be "CytogenomicLocation"
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
