.. _metadata_functions:

Metadata Functions
==================

The metadata functions expose information about the current Exasol session and database using MariaDB-compatible names.

``DATABASE()`` and ``SCHEMA()`` both return the current schema. Exasol has no database catalog level, so the current schema is the closest equivalent.

``CONNECTION_ID()`` returns the current Exasol session identifier.
``SESSION_USER()`` and ``SYSTEM_USER()`` both return the current Exasol user.

``VERSION()`` returns the Exasol database version.
