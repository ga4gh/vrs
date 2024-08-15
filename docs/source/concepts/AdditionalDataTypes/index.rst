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

.. include::  ../../def/Ga4ghIdentifiableObject.rst

.. _Variation:

Variation
#########

The root of all variant data classes, `Variation` primarily plays a role as a common
schema for representing variants and associated variant expressions, such as HGVS or
SPDI strings.

Definition and Information Model
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

.. include::  ../../def/Variation.rst


Supporting Classes
@@@@@@@@@@@@@@@@@@

Supporting data classes are used to support primary concept classes in VRS.

.. _Expression:

Expression
##########

An `Expression` is a data class used only by `Variation` objects. It is used to
represent variants using other syntaxes, including HGVS and SPDI.

Definition and Information Model
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

.. include::  ../../def/Ga4ghIdentifiableObject.rst

