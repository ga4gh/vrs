.. _AdditionalDataTypes:

Additional Data Types
!!!!!!!!!!!!!!!!!!!!!

Below are the additional data types used by the VRS models.

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

Primitive Types
@@@@@@@@@@@@@@@

Primitive types represent simple values with syntactic or other
constraints. They enable correctness for values stored in VRS.

.. _Range:

Range
#####

.. include:: ../../def/vrs/Range.rst

.. _Residue:

Residue
#######

.. include:: ../../def/vrs/Residue.rst

.. _SequenceString:

SequenceString
##############

.. include:: ../../def/vrs/SequenceString.rst

Imported Classes
@@@@@@@@@@@@@@@@

The following classes are used by VRS but maintained by the GA4GH GKS
Work Stream as common data classes.

.. toctree::
   :titlesonly:

   Entity
   Element
   Extension
   Coding
   Code
   IRI
