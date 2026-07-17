More Functions
==============

``more-functions`` is a collection of SQL and Lua functions which are useful in practice but not built into the Exasol database engine directly.




Project Goal
------------

The project is intended to provide reusable function definitions and deployment
helpers for artifacts such as:

- SQL functions
- Lua scalar scripts
- Lua set scripts

The package currently contains placeholder infrastructure so concrete functions
can be added without changing the project layout again.

Quick Start
-----------

Create a local environment and install dependencies:

.. code-block:: shell

    poetry env use python3.12
    poetry install

List available toolbox sessions:

.. code-block:: shell

    nox -l

Run unit tests:

.. code-block:: shell

    poetry run pytest test/unit

Run integration tests against the Exasol Docker backend configured by the
toolbox / ITDE stack:

.. code-block:: shell

    poetry run pytest test/integration

Repository Layout
-----------------

- ``exasol/more_functions``: package code
- ``test/unit``: fast unit tests for rendering and registry behavior
- ``test/integration``: Exasol-backed smoke tests
- ``doc``: Sphinx documentation
