# GH-4 Lua Script SQL Wrapper

## Goal

Store the `BIT_COUNT` implementation as a real Lua source file so it can receive
Lua tooling support, while preserving the SQL script definition that Exasol
requires when integration tests load the function.

## Scope

In scope:

* Move the `BIT_COUNT` source from its SQL-wrapped `.sql` file to a `.lua` file.
* Represent the SQL declaration lines in the Lua source with the `--| ` prefix.
* Make the integration-test function loader load SQL and Lua sources according
  to their respective formats.
* Add automated coverage for the Lua-to-SQL transformation and a reproducible
  Lua lint check for `bit_count.lua`.
* Provision Lua and LuaRocks in CI through the Python Toolbox workflow patcher.

Out of scope:

* Changing the SQL-visible behavior, signature, or bit-counting algorithm of
  `BIT_COUNT`.
* Migrating additional Lua functions; `BIT_COUNT` is the only current Lua
  scalar function.
* Adding user-facing function documentation, a release-version change, or a
  changelog entry for this internal source-layout refactoring.

## Design References

* [System Requirements](../system_requirements/system_requirements.md)
* [BIT_COUNT Requirements](../system_requirements/scalar_functions/bit_count.md)
* [Design](../design.md)
* [Developer Guide](../developer_guide.rst)
* [Existing BIT_COUNT Changeset](2-add-bit-count-function.md)

## Strategy

Keep the SQL declaration in `bit_count.lua` as consecutive lines beginning
with `--| `, followed by ordinary Lua code. The loader will continue to execute
SQL files unchanged. For Lua files, it will remove that prefix only from
prefixed lines and append the Exasol SQL script terminator (`\n/\n`) before
execution. The pure source-transformation behavior should be unit-tested;
the existing `BIT_COUNT` integration tests will then prove that the generated
SQL definition deploys and runs in Exasol.

This repository currently has neither `doc/design/quality_requirements.md` nor
`doc/changesets/README.md`. Verification below therefore follows the current
Nox sessions, CI workflow, and the quality conventions recorded in the
developer guide. CI installs Lua and LuaRocks with `apt`. Local development
uses the configured user-local Lua and LuaRocks installations. LuaRocks uses
its standard local directory in the user's home tree so multiple projects
reuse downloaded rocks. The previous BIT_COUNT branch deliberately removed temporary
Lua test tooling for this follow-up issue, so this issue must add only the
reproducible Lua lint tooling needed by its acceptance criterion.

## Task List

- [x] Create and checkout a new Git branch `feature/4-lua-script-sql-wrapper`

### Requirements And Design

- [x] Confirm that `req~bit-count-function~2` and its scenarios remain accurate because the externally observable function behavior does not change; do not revise their IDs or text.
- [x] Stop and ask user for a review of the unchanged system requirements decision.
- [x] Add `dsn~function-source-loader-selection~1` and `dsn~lua-function-source-header~1` to `doc/design.md` to define reusable extension-based source selection and `--| ` Lua-header processing; retain `dsn~bit-count-function~2` because BIT_COUNT behavior and design remain unchanged.
- [x] Stop and ask user for a review of the design.

### Implementation

- [x] Rename `exasol/more_functions/lua/scalar/bit_count.sql` to `bit_count.lua`, preserve the BIT_COUNT implementation trace tags, add implementation coverage for `dsn~lua-function-source-header~1`, and convert its `CREATE OR REPLACE ...` and `RETURNS ... AS` declaration lines to `--| `-prefixed source lines; remove the in-file SQL slash terminator.
- [x] Refactor `ScalarFunctionTestBase.load_function()` to select SQL `.sql` sources and Lua `.lua` sources distinctly, execute SQL content unchanged, and transform Lua content by stripping each `--| ` prefix and adding exactly the final newline/slash/newline terminator.
- [x] Add `.workflow-patcher.yml` to provision Lua 5.4, its development headers, and LuaRocks in the single Python 3.12 `lint-code` CI matrix entry; regenerate and validate the patched `checks` workflow with the Python Toolbox.
- [x] Add a project rockspec that declares pinned Lua development dependencies, beginning with `luacheck`; add a reproducible `lua:install-dependencies` Nox session that installs them with LuaRocks' `--local` switch; and add a Lua-lint session that runs the installed linter through the appropriate automated checks in `.workflow_patcher.yml`.
- [x] Add OFT implementation and unit-test coverage for `dsn~function-source-loader-selection~1` and `dsn~lua-function-source-header~1` without changing existing BIT_COUNT design or scenario coverage.

### Verification

- [x] Add unit tests for loader source selection and transformation: SQL stays unchanged; Lua removes only `--| ` prefixes and gains the final `\n/\n`; missing definitions still raise the existing `FileNotFoundError`.
- [x] Run the Lua linter successfully on `bit_count.lua`.
- [ ] Run the BIT_COUNT integration tests against an Exasol backend to confirm the reconstructed Lua script deploys and preserves all documented scenarios.
- [x] Run the unit-test, Python lint/format, and required project checks affected by the loader and Nox configuration.
- [x] Keep the OpenFastTrace trace clean for the updated requirement, design, implementation, and integration-test artifacts.

## Version And Changelog Update

No version or changelog change is planned because this issue preserves the
published `BIT_COUNT` behavior and changes only its source representation and
test tooling.
