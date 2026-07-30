.. _user_guide:

User Guide
==========

``more-functions`` is intended to collect deployable SQL and Lua functions for
Exasol in a form that is easy to test, review, and publish.

Function Coverage Matrix
------------------------

The function coverage table lives on a dedicated page:

- :doc:`function_coverage`

.. toctree::
    :maxdepth: 1
    :hidden:

    function_coverage

Functions
---------

.. toctree::
    :maxdepth: 1

    functions/bit_count
    functions/connection_id
    functions/database
    functions/sys_functions
    functions/st_function_aliases
    functions/version

Unsupported Functions
---------------------

The following functions either conflict with existing reserved words or are reserved but not implemented in the Exasol core database:

- ``CONTAINS``
- ``CURRENT_SCHEMA``
- ``EQUALS``
- ``OVERLAPS``
- ``SCHEMA``
- ``SESSION_USER``
- ``WITHIN``

Alias Functions for Which the Original does not exist
-----------------------------------------------------

The following alias functions are not available since the function that should be aliased does not exists.

* ``POINTONSURFACE``
* ``SRID``
