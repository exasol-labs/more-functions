# GH-2 Add BIT_COUNT Function

## Goal

Add a `BIT_COUNT` function to `more-functions` that mimics MariaDB's `BIT_COUNT(N)` behavior for Exasol users, verifies the supported Exasol integer input forms with integration tests, and adds a compact agent-oriented guide for introducing additional functions in this repository.

## Scope

In scope:

* Add traced requirements and scenarios for `BIT_COUNT`.
* Add technical design for a Lua scalar implementation of `BIT_COUNT`.
* Implement the new function in the repository's Exasol function sources.
* Add integration tests for the supported Exasol ways to pass integer-valued arguments.
* Add a compact agent file that explains which repository artifacts must change when adding a new function.
* Update user-facing function inventory and release notes for the new function.

Out of scope:

* Adding other bitwise helper functions besides `BIT_COUNT`.
* Broad refactoring of the function-loading test infrastructure beyond what is needed to exercise the new Lua function.
* Defining behavior for non-integer inputs unless implementation work shows that Exasol or MariaDB compatibility requires it to make the function usable.

## Design References

* [System Requirements](../system_requirements/system_requirements.md)
* [Design](../design.md)
* [Developer Guide](../developer_guide.rst)
* [Function Coverage](../user_guide/function_coverage.md)
* [Unreleased Changelog](../changes/unreleased.md)
* [MariaDB BIT_COUNT Reference](https://mariadb.com/docs/server/reference/sql-functions/secondary-functions/bit-functions-and-operators/bit_count)

## Strategy

This repository does not yet contain a dedicated `doc/design/quality_requirements.md` or an existing `doc/changesets/README.md`, so this changeset derives its verification tasks from the current project conventions in `doc/design.md`, `doc/developer_guide.rst`, the existing OFT setup in `noxfile.py`, and the integration-test layout under `test/`.

The implementation should stay aligned with the repository structure by introducing a dedicated requirement file for `BIT_COUNT`, extending the shared design with one technical design item, and keeping behavior details in the requirement scenarios. Since the issue explicitly asks for a Lua function, the design needs to define how Lua scalar functions are stored and loaded for tests before production code is added.

## Task List

- [x] Create and checkout a new Git branch `feature/2-add-bit-count-function`

### Requirements And Design

- [x] Add `BIT_COUNT` to the scalar-function index in `../system_requirements/system_requirements.md`
- [x] Create `doc/system_requirements/scalar_functions/bit_count.md` with one user-facing requirement for MariaDB-compatible bit counting and scenario items for representative Exasol integer argument forms
- [x] Stop and ask user for a review of the system requirements
- [x] Extend `doc/design.md` with `dsn~bit-count-function~1` describing the Lua scalar function location, runtime behavior, and forwarding from scenarios to `impl` and `itest`
- [x] Add a compact agent file that explains which repository files and trace artifacts must be updated when introducing a new function
- [x] Stop and ask user for a review of the design

### Implementation

- [x] Add the Lua scalar function source for `BIT_COUNT` under the repository's Exasol function tree
- [x] Extend test utilities as needed so integration tests can load and execute the Lua scalar function without duplicating setup logic
- [x] Update the list of functions this project add under `doc/user_guide/function_coverage.md`
- [x] Add OFT implementation coverage tags for the new design and scenario items

### Verification

- [x] Add integration tests that prove `BIT_COUNT` works for the supported Exasol integer input variants named in the issue acceptance criteria
- [x] Add OFT integration-test coverage tags for the new design and scenario items
- [x] Fix the OFT input path in `noxfile.py` from `tests` to `test` so trace verification covers the actual test directory
- [x] Keep the OpenFastTrace trace clean for the updated requirement, design, implementation, and integration-test artifacts
- [x] Keep the relevant integration-test and toolbox verification tasks green

### Update User Documentation

- [x] Update `doc/user_guide/function_coverage.md` to mark `BIT_COUNT` as provided by `more-functions`
- [x] Update `README.rst` or other user-facing function overview documentation if `BIT_COUNT` needs to be listed there

## Version And Changelog Update

- [x] Add an unreleased changelog entry for `BIT_COUNT` and the new agent guidance in `doc/changes/unreleased.md`
