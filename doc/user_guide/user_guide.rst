.. _user_guide:

User Guide
==========

``more-functions`` is intended to collect deployable SQL and Lua functions for
Exasol in a form that is easy to test, review, and publish.

Current Scope
-------------

The repository currently provides the initial plumbing:

- a small model for function definitions
- rendering helpers for ``CREATE ... SCRIPT`` statements
- toolbox-managed quality tooling
- integration-test wiring for Docker-based Exasol environments

Adding a New Function
---------------------

The intended workflow for concrete functions is:

1. Add a new ``FunctionDefinition`` to the package.
2. Register it in a local or shared ``FunctionRegistry``.
3. Add unit tests for statement rendering.
4. Add integration tests that deploy and exercise the function in Exasol.

Integration Testing
-------------------

Integration tests use the backend-aware fixtures provided by the Exasol test
stack. The current smoke test only verifies connectivity, which keeps the
initial scaffold stable while the first real functions are designed.

Function Coverage Matrix
------------------------

The MariaDB-to-Exasol comparison table lives on a dedicated page:

- :doc:`mariadb_function_coverage`

.. toctree::
   :maxdepth: 1
   :hidden:

   mariadb_function_coverage
