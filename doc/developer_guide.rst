Developer Guide
===============

Development Environment
-----------------------

Set up the local environment with:

.. code-block:: shell

    poetry env use python3.12
    poetry install

Tooling
-------

The project is managed by Exasol's Python Toolbox through ``noxconfig.py`` and
``noxfile.py``. Use ``nox -l`` to inspect available sessions.

Tests
-----

- Unit tests live in ``test/unit``.
- Integration tests live in ``test/integration`` and expect an Exasol backend
  provided by ITDE / ``pytest-exasol-backend``.
