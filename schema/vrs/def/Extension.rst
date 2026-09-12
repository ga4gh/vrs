.. admonition:: Trial Use
    :class: note

    May change in future releases. See |maturity-model|.

**Computational Definition**

The Extension class provides entities with a means to include additional attributes that are outside of the specified standard but needed by a given content provider or system implementer. These extensions are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.

**Information Model**

Some Extension attributes are inherited from :ref:`Element`.

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
      - The 'logical' identifier of the data element in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference an object from another.
   *  - extensions
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Extension`
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - name
      -
      - string
      - 1..1
      - A name for the Extension. Should be indicative of its meaning and/or the type of information it value represents.
   *  - value
      -
      - ['number', 'string', 'boolean', 'object', 'array', 'null']
      - 1..1
      - The value of the Extension - can be any primitive or structured object
   *  - description
      -
      - string
      - 0..1
      - A description of the meaning or utility of the Extension, to explain the type of information it is meant to hold.

**Used in:** :ref:`Adjacency`, :ref:`Allele`, :ref:`CisPhasedBlock`, :ref:`Coding`, :ref:`ConceptMapping`, :ref:`ConceptSet`, :ref:`CopyNumberChange`, :ref:`CopyNumberCount`, :ref:`DerivativeMolecule`, :ref:`Entity`, :ref:`Expression`, :ref:`Ga4ghIdentifiableObject`, :ref:`LengthExpression`, :ref:`LiteralSequenceExpression`, :ref:`Location`, :ref:`MappableConcept`, :ref:`MolecularVariation`, :ref:`ReferenceLengthExpression`, :ref:`RelativeAllele`, :ref:`RelativeSequenceLocation`, :ref:`SequenceExpression`, :ref:`SequenceLocation`, :ref:`SequenceOffsetLocation`, :ref:`SequenceReference`, :ref:`SystemicVariation`, :ref:`Terminus`, :ref:`TraversalBlock`, :ref:`Variation`
