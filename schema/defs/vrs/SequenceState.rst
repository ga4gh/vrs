**Computational Definition**

DEPRECATED. A :ref:`Sequence` as a :ref:`State`. This is the State class to use for representing "ref-alt" style variation, including SNVs, MNVs, del, ins, and delins. This class is deprecated. Use :ref:`LiteralSequenceExpression` instead.

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
      - 1..1
      - MUST be "SequenceState"
   *  - sequence
      - :ref:`Sequence`
      - 1..1
      - A string of :ref:`Residues <Residue>`
