# GH-6 ST_* Alias Functions

## Goal

Provide the MariaDB-compatible unprefixed aliases for Exasol's supported geospatial `ST_*` functions. This lets users port spatial SQL that uses the MariaDB aliases without rewriting each call to its `ST_*` equivalent.

## Scope

In scope:

* Add SQL scalar-function wrappers for every Exasol `ST_*` function for which the MariaDB function index defines an unprefixed alias, using the mappings in the function-coverage matrix as the authoritative alias inventory.
* Add traced requirements, design, implementation, and integration-test coverage for the alias family.
* Correct the function-coverage matrix: its unprefixed geospatial alias rows currently incorrectly imply that Exasol provides them. Mark them as supplied by `more-functions` once their wrappers exist.

Out of scope:

* Implementing new geospatial algorithms or aliases that MariaDB does not define.
* Changing Exasol's `ST_*` function semantics, argument validation, or return values.
* Supporting aliases for Exasol `ST_*` functions that do not have a MariaDB-compatible unprefixed name or that require a binary type unavailable in Exasol.

## Design References

* [System Requirements](../system_requirements.md)
* [Design](../design.md)
* [Developer Guide](../developer_guide.rst)
* [Function Coverage](../user_guide/function_coverage.md)
* [Exasol Geospatial Functions](https://docs.exasol.com/db/latest/sql_references/geospatialfunctions.htm)
* [MariaDB Spatial Function Reference](https://mariadb.com/docs/server/reference/sql-statements/geometry-constructors/geometry-relations/)

## Strategy

Treat each alias as a thin SQL wrapper that calls exactly one Exasol `ST_*` function. Before adding each wrapper, derive its parameter list, return type, and overload set from the current Exasol SQL reference; the wrapper must expose the same callable signature as its target. Keep one alias per SQL source file under `exasol/more_functions/sql/scalar/`, following `area.sql`.

The implementation inventory is the set of geo rows in `doc/user_guide/function_coverage.md` that map an unprefixed MariaDB function to an Exasol `ST_*` function. Every row in this inventory is a compatibility function; its current Exasol-coverage marker is incorrect because Exasol provides only the `ST_*` target, not the unprefixed alias. Examples include `AREA` → `ST_AREA`, `BOUNDARY` → `ST_BOUNDARY`, `BUFFER` → `ST_BUFFER`, `CONTAINS` → `ST_CONTAINS`, `GEOMETRYTYPE` → `ST_GEOMETRYTYPE`, and `WITHIN` → `ST_WITHIN`. The task implementing the inventory must reconcile every mapped row, including case-sensitive mixed-case MariaDB names, rather than relying on this abbreviated list.

Add a parameterized integration-test suite, with a valid geometry fixture and per-alias SQL expressions and expected values. It must load each alias source and demonstrate that the alias result equals its `ST_*` target result. Use function-specific fixtures where a common geometry cannot exercise the target.

## Task List

- [x] Create and checkout a new Git branch `feature/6-st-alias-functions`

### Requirements And Design

- [ ] Add a user-facing requirement and scenario for the MariaDB-compatible geospatial alias family in `doc/system_requirements/scalar_functions/`, covering the scalar-functions feature and enumerating the supported alias-to-`ST_*` mappings.
- [ ] Stop and ask user for a review of the system requirements.
- [ ] Add a design item to `doc/design.md` describing one-file-per-alias SQL wrappers, signature parity with each `ST_*` target, and forwarding of the alias-family scenario to implementation and integration testing.
- [ ] Stop and ask user for a review of the design.

### Implementation

- [ ] Reconcile every MariaDB alias → Exasol `ST_*` mapping in `doc/user_guide/function_coverage.md` against the current Exasol and MariaDB references; record the complete supported inventory in the requirement.
- [ ] Add one traced SQL scalar-function source per missing alias in `exasol/more_functions/sql/scalar/`, preserving exact aliases, signatures, overloads, and target return types from the Exasol reference and delegating directly to the target `ST_*` function.
- [ ] Add implementation coverage tags that cover the new alias-family design item.
- [ ] Correct the function-coverage matrix by changing each implemented alias from an incorrect Exasol built-in marker to a `more-functions` marker while retaining its Exasol `ST_*` target.

### Verification

- [ ] Add parameterized integration tests that load every alias and verify its result is identical to the mapped `ST_*` function for representative valid inputs; add separate fixtures/cases for constructors, accessors, predicates, and geometry-returning operations as necessary.
- [ ] Add OFT integration-test coverage for the alias-family scenario.
- [ ] Run the targeted geospatial alias integration-test module against an Exasol backend.
- [ ] Run the complete integration-test suite to detect schema or function-name collisions between alias definitions.
- [ ] Keep the OpenFastTrace trace clean for the affected `feat`, `req`, `scn`, `dsn`, `impl`, and `itest` artifacts (`poetry run nox -s oft:trace`).
- [ ] Run the repository's relevant format, lint, and unit-test Nox sessions required by the developer tooling.

### Update User Documentation

- [ ] Update `doc/user_guide/function_coverage.md` with the alias-provided status for the complete supported inventory.
- [ ] Add user-guide documentation only if the final alias inventory needs usage guidance beyond the coverage matrix; otherwise record that no separate user-guide page is needed because all aliases exactly delegate to documented Exasol functions.

## Version And Changelog Update

- [ ] Raise the project version for this feature release according to the repository's release process.
- [ ] Add an unreleased changelog entry announcing the MariaDB-compatible geospatial aliases.
