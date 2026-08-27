.. _AdditionalDataTypes:

Additional Data Types
!!!!!!!!!!!!!!!!!!!!!

Below are the additional data types used by the VRS models.
Any classes with the *imported* tag are used by VRS but maintained by the GA4GH GKM
Work Stream as common data classes.

Abstract Classes
@@@@@@@@@@@@@@@@

Abstract classes provide common semantics and properties that are shared by
multiple inheriting classes. This provides a useful structure for consistency
across multiple concrete classes (e.g. different variation types).

.. _Ga4ghIdentifiableObject:

GA4GH Identifiable Object
#########################

Many VRS objects are GA4GH Identifiable Objects, which may be used to create
:ref:`computed-identifiers`.

In addition to having GA4GH serialization keys (see :ref:`digest-serialization`),
GA4GH identifiable objects also have a defined GA4GH identifier type prefix (see
:ref:`identifier-construction`).

Definition and Information Model
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

.. include::  ../../def/vrs/Ga4ghIdentifiableObject.rst

.. _Variation:

Variation
#########

The root of all variant data classes, `Variation` primarily plays a role as a common
schema for representing variants and associated variant expressions, such as HGVS, ISCN,
or SPDI strings.

Definition and Information Model
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

.. include::  ../../def/vrs/Variation.rst

Components
$$$$$$$$$$

.. _Expression:

Expression
%%%%%%%%%%

An `Expression` is a data class used only by :ref:`Variation` objects. It is used to
represent variants using other syntaxes, including HGVS and SPDI.

.. include::  ../../def/vrs/Expression.rst

.. _gkm-core:Entity:
.. _Entity:

Entity
######
*imported*

.. include::  ../../def/gkm-core/Entity.rst

.. _gkm-core:Element:
.. _Element:

Element
#######
*imported*

.. include::  ../../def/gkm-core/Element.rst

General Purposes Types
@@@@@@@@@@@@@@@@@@@@@@

General purpose data types.

.. _Extension:

Extension
#########
*imported*

.. include::  ../../def/gkm-core/Extension.rst

.. _MappableConcept:

Mappable Concept
################
*imported*

.. include::  ../../def/gkm-core/MappableConcept.rst

.. _ConceptSet:

ConceptSet
##########
*imported*

.. include::  ../../def/gkm-core/ConceptSet.rst

.. _ConceptMapping:

Concept Mapping
###############
*imported*

.. include::  ../../def/gkm-core/ConceptMapping.rst

.. _Coding:

Coding
######
*imported*

.. include::  ../../def/gkm-core/Coding.rst


Primitive Types
@@@@@@@@@@@@@@@

Primitive types represent simple values with syntactic or other
constraints. They enable correctness for values stored in VRS.

.. _Range:

Range
#####

.. include:: ../../def/vrs/Range.rst

.. _residue:

residue
#######

.. include:: ../../def/vrs/residue.rst

.. _sequenceString:

sequenceString
##############

.. include:: ../../def/vrs/sequenceString.rst

.. _code:

code
####
*imported*

.. include::  ../../def/gkm-core/code.rst

.. _iriReference:

iriReference
############
*imported*

.. include::  ../../def/gkm-core/iriReference.rst
