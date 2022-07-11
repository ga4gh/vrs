**Computational Definition**

A class describing a :ref:`Genotype` `member`.

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
   *  - copies
      - :ref:`Number` | :ref:`IndefiniteRange` | :ref:`DefiniteRange`
      - 1..1
      - The number of copies of the `variation` at a :ref:`Genotype` locus.
   *  - variation
      - :ref:`MolecularVariation`
      - 1..1
      - A :ref:`MolecularVariation` at a :ref:`Genotype` locus.
