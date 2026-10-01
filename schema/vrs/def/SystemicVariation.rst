.. admonition:: Trial Use
    :class: note

    May change in future releases. See |maturity-model|.

**Abstract Class** — not instantiated directly; concrete subclasses inherit its attributes.

**Sealed** — SystemicVariation has a closed, exhaustive set of concrete subclasses; every one is listed below. No other subclass is permitted, and a conforming instance must be exactly one of these types.

**Computational Definition**

A Variation of multiple molecules in the context of a system, e.g. a genome, sample, or homologous chromosomes.

**Information Model**

This class must match **one of** the following:

* :ref:`CopyNumberChange`
* :ref:`CopyNumberCount`


**Inherits:** :ref:`Variation`

**Subclasses:** :ref:`CopyNumberChange`, :ref:`CopyNumberCount`
