.. admonition:: Trial Use
    :class: note

    May change in future releases. See |maturity-model|.

**Abstract Class** — not instantiated directly; concrete subclasses inherit its attributes.

**Sealed** — Location has a closed, exhaustive set of concrete subclasses; every one is listed below. No other subclass is permitted, and a conforming instance must be exactly one of these types.

**Computational Definition**

A contiguous segment of a biological sequence.

**Information Model**

This class must match **one of** the following:

* :ref:`RelativeSequenceLocation`
* :ref:`SequenceLocation`


**Inherits:** :ref:`Ga4ghIdentifiableObject`

**Subclasses:** :ref:`RelativeSequenceLocation`, :ref:`SequenceLocation`

**Used in:** :ref:`Adjacency`, :ref:`Terminus`
