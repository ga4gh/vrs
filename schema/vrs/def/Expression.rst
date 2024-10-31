
.. note:: This data class is at a **trial use** maturity level and may change
    in future releases. Maturity levels are described in the :ref:`maturity-model`.
                      
                    
**Computational Definition**

Representation of a variation by a specified nomenclature or syntax for a Variation object. Common examples of expressions for the description of molecular variation include the HGVS and ISCN nomenclatures.

**Information Model**

Some Expression attributes are inherited from :ref:`gks-core:Element`.

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
      - The 'logical' identifier of the data element in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference an object from another.
   *  - extensions
      - :ref:`Extension`
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - syntax
      - string
      - 1..1
      - The syntax used to describe the variation. The value should be one of the supported syntaxes.
   *  - value
      - string
      - 1..1
      - The expression of the variation in the specified syntax. The value should be a valid expression in the specified syntax.
   *  - syntax_version
      - string
      - 0..1
      - The version of the syntax used to describe the variation. This is particularly important for HGVS expressions, as the syntax has evolved over time.
