.. admonition:: Trial Use
    :class: note

    May change in future releases. See |maturity-model|.

**Abstract Class** — not instantiated directly; concrete subclasses inherit its attributes.

**Computational Definition**

A :ref:`variation` on a contiguous molecule.

**Information Model**

This class must match **one of** the following:

* :ref:`Allele`
* :ref:`RelativeAllele`
* :ref:`CisPhasedBlock`
* :ref:`Adjacency`
* :ref:`Terminus`
* :ref:`DerivativeMolecule`


**Subclasses:** :ref:`Adjacency`, :ref:`Allele`, :ref:`CisPhasedBlock`, :ref:`DerivativeMolecule`, :ref:`RelativeAllele`, :ref:`Terminus`
