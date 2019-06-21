Schema
!!!!!!


Overview
@@@@@@@@

.. _vr-schema-diagram:

.. figure:: images/object_graph.png
   :align: left

   **VR Schema Diagram**

   The VR Schema requires the use of multiple composite objects, which
   are grouped under four abstract classes: :ref:`Variation`,
   :ref:`Location`, :ref:`State`, and :ref:`Interval`. These classes
   and their relationships to the representation of Variation are
   illustrated here. All classes have a string `type`. Dashed borders
   denote abstract classes. Abstract classes are not
   instantiated. Thin solid borders denote classes that may be
   instantiated but are not identifiable. Bold borders denote
   identifiable objects (i.e., may be serialized and identified by
   computed identifier). Solid arrow lines denoted
   inheritance. Subclasses inherit all attributes from their
   parent. Inherited attributes are not shown.  These abstract classes
   and their concrete child classes are described in the following
   documents.


Machine Readable Specifications
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

The machine readable VR Specification is written using `JSON Schema
<https://json-schema.org/>`_.

The schema itself is written in YAML (|vr_yaml|) and converted to JSON
(|vr_json|).  Version |version| is current.

Contributions to the schema should be written in the YAML version.
