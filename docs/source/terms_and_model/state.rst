.. _state:

State
!!!!!

**Biological definition**

None.

**Computational definition**

*State* objects are one of two primary components specifying a VR
:ref:`Allele` (in addition to :ref:`Location`), and the designated
components for representing change (or non-change) of the features
indicated by the Allele Location. As an abstract class, State may
encompass concrete :ref:`sequence` changes (see :ref:`SequenceState
<sequence-state>`), complex translocations, copy number changes,
expression variation, rule-based variation, and more (see
:ref:`planned-states`).

.. _sequence-state:

SequenceState
@@@@@@@@@@@@@

**Biological definition**

None.

**Computational definition**

The *SequenceState* class specifically captures a :ref:`sequence` as a
:ref:`State`. This is the State class to use for representing
"ref-alt" style variation, including SNVs, MNVs, del, ins, and delins.

**Information model**

.. csv-table::
   :header: Field, Type, Label, Description
   :align: left
   :widths: 12, 9, 10, 30

   id, :ref:`Id`, optional, State Id; must be unique within document
   type, string, required, State type; must be set to 'SequenceState'
   sequence, :ref:`Sequence`, required, The sequence that is to be used as the state for other types.
   
**Examples**

* See example usage in the `reference implementation documentation <impl-vr-python>`.
