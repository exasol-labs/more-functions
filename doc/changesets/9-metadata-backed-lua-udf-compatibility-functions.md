# GH-9 Metadata-Backed Lua UDF Compatibility Functions

## Goal

Provide deployable MariaDB-compatible information functions whose values come
directly from Exasol Lua UDF metadata. This establishes a repeatable pattern
for compatibility functions that do not need system-table queries.

## Scope

In scope:

* Add no-argument Lua scalar UDFs for `DATABASE()`, `CONNECTION_ID()`, and
  `VERSION()`.
* Source their values from `exa.meta.current_schema`, `session_id`, and
  `database_version`.
* Add traced requirements, design, implementation, and integration-test
  coverage; update the function-coverage matrix, user-facing caveats, and
  unreleased changelog.
* Verify whether the `SYS` schema is writable for normal user-defined
  functions before keeping any `SYS.*` compatibility claims in scope.

Out of scope:

* Querying Exasol system tables or adding a general metadata abstraction.
* Implementing further MariaDB compatibility functions discovered by this
  prototype.
* Claiming MariaDB-identical connection or user identity semantics where
  Exasol metadata has different meanings.

## Design References

* [System Requirements](../system_requirements/system_requirements.md)
* [Design](../design/design.md)
* [Developer Guide](../developer_guide.rst)
* [Function Coverage](../user_guide/function_coverage.md)
* [Unreleased Changelog](../changes/unreleased.md)
* [Exasol Lua UDF metadata](https://docs.exasol.com/db/latest/database_concepts/udf_scripts/lua.htm)

## Strategy

Add one requirements document per deployable compatibility function, indexed
under scalar functions. Each document defines one requirement and one scenario
for its metadata mapping, then forwards that scenario to implementation and
integration testing rather than duplicating scenario text.

Each script should use the established `--| ` Lua SQL-header convention and
return its corresponding `exa.meta` field without a system-table query.

Before finalizing the requirement or code, run a small deployment probe against
the supported Exasol backend. The probe showed that `SYS` is not a writable
application schema, so the `SYS.VERSION_*` names are out of scope. The probe
also showed that several MariaDB metadata names are not deployable as ordinary
UDFs on this backend, so they were removed from this changeset instead of being
silently renamed.

This repository currently has neither `doc/design/quality_requirements.md` nor
`doc/changesets/README.md`. Verification therefore follows the current design,
developer guide, Nox sessions, and existing Lua-function changesets.

## Task List

- [x] Create and checkout a new Git branch `feature/9-metadata-backed-lua-udf-compatibility-functions`

### Requirements And Design

- [x] Add the deployable metadata-backed compatibility functions to the scalar-function index and create dedicated requirement files for `DATABASE()`, `CONNECTION_ID()`, and `VERSION()`.
- [x] Stop and ask user for a review of the system requirements.
- [x] Add design items to `../design/design.md` describing one no-argument Lua scalar script per deployable compatibility name, direct `exa.meta` reads, and forwarding of each new scenario to `impl` and `itest`.
- [x] Record the resolved deployment decision for the `CURRENT_SCHEMA` built-in name and `SYS.VERSION_*` namespace; the on-prem Exasol backend rejects the unsupported UDF names and `SYS` is not modifiable.
- [x] Stop and ask user for a review of the design.

### Implementation

- [x] Add traced Lua scalar sources under `exasol/more_functions/lua/scalar/` for the deployable compatibility names, using the existing Lua-header format and no SQL/system-table lookup.
- [x] Implement `DATABASE()`, `CONNECTION_ID()`, and `VERSION()` from their specified metadata fields.
- [x] Add `impl` coverage tags for the new design items and preserve the normal extension-based Lua function loader; add `exa` to the Lua-linter globals.

### Verification

- [x] Add integration tests that load each script through `ScalarFunctionTestBase` and assert representative metadata-backed return values against the session/database context.
- [x] Add integration-test coverage tags for every new scenario.
- [x] Run a targeted deployment/invocation probe for the metadata-function names and record the unsupported names before treating the function inventory as complete.
- [ ] Run `poetry run nox -s lua:lint`, the affected unit tests, the targeted metadata-function integration tests, and the complete integration-test suite against an Exasol backend.
- [x] Keep the OpenFastTrace trace clean for affected `feat`, `req`, `scn`, `dsn`, `impl`, and `itest` artifacts (`poetry run nox -s oft:trace`).

### Update User Documentation

- [x] Update `doc/user_guide/function_coverage.md` to mark the deployable compatibility functions as provided by `more-functions`, while leaving unsupported metadata names unclaimed.
- [x] Add concise user-facing documentation for the intentional semantic differences: Exasol session IDs are exposed rather than MariaDB connection identities.

## Version And Changelog Update

- [ ] Determine the next feature-release version using the repository release process and update project version metadata if this issue is included in that release.
- [x] Add an unreleased changelog entry for the metadata-backed compatibility-function family and its documented compatibility caveats.
