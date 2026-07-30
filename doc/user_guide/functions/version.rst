.. _version:

VERSION
-------

``VERSION()`` returns the Exasol database version string.

Syntax
------

.. code-block:: sql

   VERSION()

DESCRIPTION
-----------

================== ================= ===============
Parameter / Return Type              Range
================== ================= ===============
Return             ``VARCHAR(128)``
================== ================= ===============

Returns the version number of Exasol.

Examples
--------

.. code-block:: sql

   SELECT VERSION();

Returns a version number like ``2026.1.0``.
