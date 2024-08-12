**Computational Definition**

Representation of a variation by a specified nomenclature or syntax for a Variation object. Common examples of expressions for the description of molecular variation include the HGVS and ISCN nomenclatures.

    **Information Model**
    
    .. list-table::
       :class: clean-wrap
       :header-rows: 1
       :align: left
       :widths: auto
       
       *  - Field
          - Type
          - Limits
          - Description
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
