# GH-9 Metadata-Backed Lua UDF Compatibility Functions

## Goal

Provide an initial, compact family of MariaDB-compatible information functions
whose values come directly from Exasol Lua UDF metadata. This establishes a
repeatable pattern for compatibility functions that do not need system-table
queries.

## Scope

In scope:

* Add no-argument Lua scalar UDFs for `CURRENT_SCHEMA()`, `DATABASE()`,
  `SCHEMA()`, `CONNECTION_ID()`, `VERSION()`, `SYS.VERSION_MAJOR()`,
  `SYS.VERSION_MINOR()`, `SYS.VERSION_PATCH()`, `SESSION_USER()`, and
  `SYSTEM_USER()`.
* Source their values from `exa.meta.current_schema`, `database_name`,
  `session_id`, `database_version`, and `current_user`; make `SCHEMA()` an
  alias of `DATABASE()`.
* Parse the major, minor, and patch components from the Exasol database-version
  string and verify representative version strings.
* Add traced requirements, design, implementation, and integration-test
  coverage; update the function-coverage matrix, user-facing caveats, and
  unreleased changelog.
* Verify whether Exasol permits a user-defined `CURRENT_SCHEMA` function beside
  its existing built-in and whether the normal installation schema can define
  the `SYS.VERSION_*` names.

Out of scope:

* Querying Exasol system tables or adding a general metadata abstraction.
* Implementing further MariaDB compatibility functions discovered by this
  prototype.
* Claiming MariaDB-identical connection or user identity semantics where
  Exasol metadata has different meanings.

## Design References

* [System Requirements](../system_requirements.md)
* [Design](../design.md)
* [Developer Guide](../developer_guide.rst)
* [Function Coverage](../user_guide/function_coverage.md)
* [Unreleased Changelog](../changes/unreleased.md)
* [Exasol Lua UDF metadata](https://docs.exasol.com/db/latest/database_concepts/udf_scripts/lua.htm)

## Strategy

Add one requirements document for this compatibility-function family, indexed
under scalar functions. It will define one requirement and one scenario for
each function, including its metadata mapping, alias behavior, version-component
parsing, or intentional compatibility caveat. Add a single technical design
item for standalone no-argument Lua scalar scripts in
`exasol/more_functions/lua/scalar/`, then forward each scenario to
implementation and integration testing rather than duplicating scenario text.

Each script should use the established `--| ` Lua SQL-header convention and
return its corresponding `exa.meta` field without a system-table query. The
version scripts should share only the documented parsing contract; decide from
the observed `exa.meta.database_version` format whether compact duplicated Lua
parsing or a project-local Lua helper is the clearest implementation.

Before finalizing the requirement or code, run a small deployment probe against
the supported Exasol backend. The function-coverage matrix already records
`CURRENT_SCHEMA` as an Exasol built-in, and `SYS` may not be a writable
application schema. If either name cannot be installed and invoked through the
normal mechanism, stop and resolve the issue's requested compatibility name
and installation model with the user instead of silently omitting or renaming
it.

This repository currently has neither `doc/design/quality_requirements.md` nor
`doc/changesets/README.md`. Verification therefore follows the current design,
developer guide, Nox sessions, and existing Lua-function changesets.

## Task List

- [x] Create and checkout a new Git branch `feature/9-metadata-backed-lua-udf-compatibility-functions`

### Requirements And Design

- [x] Add the metadata-backed compatibility-function family to the scalar-function index and create `doc/system_requirements/scalar_functions/metadata_functions.md` with a requirement covering the ten requested names and user-visible results, plus one scenario per function for direct results, alias behavior, version-component parsing, and documented compatibility caveats.
- [x] Stop and ask user for a review of the system requirements.
- [x] Add a design item to `doc/design.md` describing one no-argument Lua scalar script per deployable compatibility name, direct `exa.meta` reads, the version-parser contract, and forwarding of each new scenario to `impl` and `itest`.
- [ ] Record the resolved deployment decision for the `CURRENT_SCHEMA` built-in name and `SYS.VERSION_*` namespace; the configured on-prem Exasol backend currently fails to start (`start_itde failed`), so the required probe remains pending.
- [ ] Stop and ask user for a review of the design.

### Implementation

- [ ] Add traced Lua scalar sources under `exasol/more_functions/lua/scalar/` for every compatibility name confirmed deployable by the probe, using the existing Lua-header format and no SQL/system-table lookup.
- [ ] Implement `DATABASE()` and `SCHEMA()` as equivalent accessors for `exa.meta.database_name`; implement `CURRENT_SCHEMA()`, `CONNECTION_ID()`, `VERSION()`, `SESSION_USER()`, and `SYSTEM_USER()` from their specified metadata fields.
- [ ] Implement the three `SYS.VERSION_*()` functions with a validated parser for the major, minor, and patch components of `exa.meta.database_version`, including the declared behavior for unexpected version formats.
- [ ] Add `impl` coverage tags for the new design item and preserve the normal extension-based Lua function loader; change that loader only if the deployment probe establishes a required qualified-name capability it cannot currently load.

### Verification

- [ ] Add integration tests that load each script through `ScalarFunctionTestBase`, assert representative metadata-backed return values against the session/database context, and prove `DATABASE()` and `SCHEMA()` return the same value.
- [ ] Add focused version-parser tests covering representative `major.minor.patch` values and the documented unexpected-format behavior; use unit tests for extracted pure parsing logic, otherwise integration tests against a testable Lua fixture.
- [ ] Add integration-test coverage tags for every new scenario, including the compatibility caveat documentation scenario where executable verification is applicable.
- [ ] Run a targeted deployment/invocation probe for `CURRENT_SCHEMA()` and all `SYS.VERSION_*()` names, recording the outcome before treating the function inventory as complete.
- [ ] Run `poetry run nox -s lua:lint`, the affected unit tests, the targeted metadata-function integration tests, and the complete integration-test suite against an Exasol backend.
- [ ] Keep the OpenFastTrace trace clean for affected `feat`, `req`, `scn`, `dsn`, `impl`, and `itest` artifacts (`poetry run nox -s oft:trace`).

### Update User Documentation

- [ ] Update `doc/user_guide/function_coverage.md` to mark each successfully installed compatibility function as provided by `more-functions`, retaining the pre-existing built-in status for `CURRENT_SCHEMA` if the probe shows that no additional UDF can be installed.
- [ ] Add concise user-facing documentation for the intentional semantic differences: Exasol session IDs and current-user values are exposed rather than MariaDB connection/authentication identities; state the exact observed behavior after the deployment probe.

## Version And Changelog Update

- [ ] Determine the next feature-release version using the repository release process and update project version metadata if this issue is included in that release.
- [ ] Add an unreleased changelog entry for the metadata-backed compatibility-function family and its documented compatibility caveats.
