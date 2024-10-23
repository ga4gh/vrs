
.. warning:: This data class is at a **draft** maturity level and may change
    significantly in future releases. Maturity levels are described in 
    the :ref:`maturity-model`.
                      
                    
**Computational Definition**

An ordered set of co-occurring :ref:`variants <Variation>` on the same molecule.

**Information Model**

Some CisPhasedBlock attributes are inherited from :ref:`Variation`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   *  - Field
      - Type
      - Limits
      - Description
   *  - id
      - string
      - 0..1
      - The 'logical' identifier of the Entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference an object from another.
   *  - label
      - string
      - 0..1
      - A primary name for the entity.
   *  - description
      - string
      - 0..1
      - A free-text description of the Entity.
   *  - alternativeLabels
      - string
      - 0..m
      - Alternative name(s) for the Entity.
   *  - extensions
      - :ref:`Extension`
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - digest
      - string
      - 0..1
      - A sha512t24u digest created using the VRS Computed Identifier algorithm.
   *  - expressions
      - :ref:`Expression`
      - 0..m
      - 
   *  - type
      - string
      - 1..1
      - MUST be "CisPhasedBlock"
   *  - members
      - :ref:`Allele` | :ref:`IRI`
      - 2..m
      - A list of :ref:`Alleles <Allele>` that are found in-cis on a shared molecule.
   *  - sequenceReference
      - :ref:`SequenceReference`
      - 0..1
      - An optional Sequence Reference on which all of the in-cis Alleles are found. When defined, this may be used to implicitly define the `sequenceReference` attribute for each of the CisPhasedBlock member Alleles.
