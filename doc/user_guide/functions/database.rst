.. _database:

DATABASE
--------

``DATABASE()`` returns the current Exasol schema name. Exasol has no separate
database catalog level, so the current schema is the closest available result.

Syntax
------

.. code-block:: sql

   DATABASE()

DESCRIPTION
-----------

================== ================= ===============
Parameter / Return Type              Range
================== ================= ===============
Return             ``VARCHAR(128)``
================== ================= ===============

Returns the name of the currently selected schema.