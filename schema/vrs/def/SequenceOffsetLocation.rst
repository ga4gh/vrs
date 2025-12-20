.. warning:: This data class is at a **draft** maturity level and may \
    change significantly in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

A location defined by an offset relative to an anchor on a  mapped sequence reference.

**Information Model**

Some SequenceOffsetLocation attributes are inherited from :ref:`gks-core:Entity`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   *  - Field
      - Flags
      - Type
      - Limits
      - Description
   *  - id
      -
      - string
      - 0..1
      - The 'logical' identifier of the Entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference an object from another.
   *  - name
      -
      - string
      - 0..1
      - A primary name for the entity.
   *  - description
      -
      - string
      - 0..1
      - A free-text description of the Entity.
   *  - aliases
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - string
      - 0..m
      - Alternative name(s) for the Entity.
   *  - extensions
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Extension`
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - type
      -
      - string
      - 1..1
      - MUST be "SequenceOffset"
   *  - sequenceReference
      -
      - :ref:`SequenceReference` | :ref:`iriReference`
      - 0..1
      - A sequence reference that has been mapped from which a relative location is defined.
   *  - anchor
      -
      - integer
      - 0..1
      - The position on the sequence reference from which the relative location offset is calculated.
   *  - anchorOrientation
      -
      - string
      - 0..1
      - Indicates which side of a discontinuous anchor on the  sequenceReference is used as the reference point for  interpreting offsetStart/offsetEnd. The anchor is an  inter-residue coordinate on the sequenceReference. When  that anchor corresponds to a boundary whose realization  on a base sequence yields two distinct locations (e.g.,  an exon junction), this property disambiguates which  anchor side on the sequenceReference is intended.  `left` denotes the side immediately preceding the anchor  in sequenceReference coordinate order; `right` denotes the  side immediately following the anchor in sequenceReference  coordinate order.
   *  - offsetStart
      -
      - integer | :ref:`Range`
      - 0..1
      - The start offset, in inter-residue coordinates, from the  anchor realization selected by anchorOrientation on the  sequenceReference.
   *  - offsetEnd
      -
      - integer | :ref:`Range`
      - 0..1
      - The end offset, in inter-residue coordinates, from the  anchor realization selected by anchorOrientation on the  sequenceReference.
