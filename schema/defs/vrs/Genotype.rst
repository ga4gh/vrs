**Computational Definition**

A set of trans-phased :ref:`MolecularVariation` members, with associated copy counts, across a specified number of genomic locus `copies`.

**Information Model**

Some Genotype attributes are inherited from :ref:`Variation`.

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
      - Variation Id. MUST be unique within document.
   *  - type
      - string
      - 1..1
      - MUST be "Genotype"
   *  - members
      - :ref:`GenotypeMember`
      - 1..m
      - Each GenotypeMember in `members` describes a :ref:`MolecularVariation` and the count of that variation at the locus.
   *  - copies
      - :ref:`Number` | :ref:`IndefiniteRange` | :ref:`DefiniteRange`
      - 1..1
      - The total number of copies of all :ref:`MolecularVariation` at this locus, MUST be greater than or equal to the sum of :ref:`GenotypeMember` copy counts. If greater than the total counts, this implies additional  :ref:`MolecularVariation` that are expected to exist but are not explicitly indicated.
