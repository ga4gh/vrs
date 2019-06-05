.. _state:

State
!!!!!

**Biological definition**

None.

**Computational definition**

*State* objects are one of two primary components specifying a VR :ref:`Allele` (in addition to :ref:`Location`), and the designated components for representing change (or non-change) of the features indicated by the Allele Location. As an abstract class, State may encompass concrete :ref:`sequence` changes (see :ref:`SequenceState <sequence-state>`), complex translocations, copy number changes, expression variation, rule-based variation, and more (see :ref:`planned-states`).

.. _sequence-state:

SequenceState
@@@@@@@@@@@@@

**Computational definition**

The *SequenceState* class specifically captures :ref:`sequence` changes over a defined :ref:`Location`. This is the State class to use for representing "ref-alt" style variation, including SNVs, MNVs, del, ins, and delins.

**Examples**

* See :ref:`example usage <simple-sequence-replacements>` in the reference implementation documentation.