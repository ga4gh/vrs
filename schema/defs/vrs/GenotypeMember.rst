**Computational Definition**

A class for expressing the count of a specific :ref:`MolecularVariation` present *in-trans* at a genomic locus represented by a :ref:`Genotype`.

**Information Model**

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
      - 0..1
      - MUST be "GenotypeMember".
   *  - count
      - :ref:`Number` | :ref:`IndefiniteRange` | :ref:`DefiniteRange`
      - 1..1
      - The number of copies of the `variation` at a :ref:`Genotype` locus.
   *  - variation
      - :ref:`Allele` | :ref:`Haplotype`
      - 1..1
      - A :ref:`MolecularVariation` at a :ref:`Genotype` locus.
