.. admonition:: Trial Use
    :class: note

    May change in future releases. See |maturity-model|.

**Abstract Class** — not instantiated directly; concrete subclasses inherit its attributes.

**Sealed** — MolecularVariation has a closed, exhaustive set of concrete subclasses; every one is listed below. No other subclass is permitted, and a conforming instance must be exactly one of these types.

**Computational Definition**

A :ref:`variation` on a contiguous molecule.

**Information Model**

This class must match **one of** the following:

* :ref:`Adjacency`
* :ref:`Allele`
* :ref:`CisPhasedBlock`
* :ref:`DerivativeMolecule`
* :ref:`RelativeAllele`
* :ref:`Terminus`


**Inherits:** :ref:`Variation`

**Subclasses:** :ref:`Adjacency`, :ref:`Allele`, :ref:`CisPhasedBlock`, :ref:`DerivativeMolecule`, :ref:`RelativeAllele`, :ref:`Terminus`
