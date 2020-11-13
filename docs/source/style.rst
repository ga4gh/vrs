This page shows style conventions used in these docs.  It will be
built with other pages and you can view it (at
docs/build/html/style.html). Unfortunately, because it's intentionally
not included in the published docs, it generates the annoying warning
"WARNING: document isn't included in any toctree".


Headings
!!!!!!!!

ReST heading levels are determined by the character used beneath text.
Within a file, each new character creates a new heading level.

This documentation uses the characters ``!``, ``@``, ``#``, and ``$``.
That is, the first four shifted digit characters across a US keyboard.

For example::

  A Heading
  !!!!!!!!!

  The first subheading
  @@@@@@@@@@@@@@@@@@@@

  The first subsubeheading
  ########################

  The second subheading
  @@@@@@@@@@@@@@@@@@@@@

  Another Heading
  !!!!!!!!!!!!!!!


Text Styles
!!!!!!!!!!!

* Literal strings. Use double backticks. Example: ````a literal````
  renders as ``a literal``. 

* Classes: Use ref. Example: ``:ref:`Allele``` renders as :ref:`Allele`.

* Attributes and variables. Use \*. Example: ``*attribute*`` renders as *attribute*.
