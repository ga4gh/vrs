**Computational Definition**

An approximate expression of a sequence that is derived from a referenced sequence location. Use of this class indicates that the derived sequence is *approximately equivalent* to the reference indicated, and is typically used for describing large regions in contexts where the use of an approximate sequence is inconsequential.

**Information Model**

Some DerivedSequenceExpression attributes are inherited from :ref:`SequenceExpression`.

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
      - MUST be "DerivedSequenceExpression"
   *  - location
      - :ref:`SequenceLocation`
      - 1..1
      - The location from which the approximate sequence is derived
   *  - reverse_complement
      - boolean
      - 1..1
      - A flag indicating if the expressed sequence is the reverse complement of the sequence referred to by `location`
