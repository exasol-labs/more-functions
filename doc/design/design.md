# Design

This document describes the technical design of `more-functions` in an arc42-style structure.
It intentionally omits sections dedicated to user requirements.

## Architecture Constraints

- Functions are implemented for Exasol.
- The repository may contain SQL functions and Lua functions.
- Behavior is specified in `../system_requirements/system_requirements.md` and linked detail files.
- Verification is performed through automated tests in this repository.

### SQL Functions vs. Lua Scripts

SQL functions are closer to the database engine, so they can be optimized better. That being said, there are a number of technical limitations that narrow down where SQL functions are applicable.

| Feature                          | SQL Functions |  Lua Scripts  |
|----------------------------------|:-------------:|:-------------:|
| Parameter type overloading       |               |    ✓[^1]     |
| Variable-length parameterlist    |               |      ✓       |
| Logic                            |  if and loop  | full language |
| Access to built-in SQL functions |      ✓       |               |

[^1]: Simulated via variable-length parameter list

## Context And Scope

`more-functions` provides database-side functions for Exasol users.
The repository supplies function definitions and automated tests.

## Solution Strategy

The solution keeps each supported function small and self-contained.
Each function has:

- a user-facing requirement in `../system_requirements`
- a design item in this document if the design adds technical information
- automated tests that verify the implemented behavior

Behavior belongs in the system requirements.
This design document records technical structure, implementation decisions, and forwarding to verification artifacts.

## Building Block View

See ["Building Block View"](building_block_view.md)

## Runtime View

See ["Runtime View"](runtime_view.md)

## Deployment View

The function definitions are deployed into an Exasol database schema.
Automated integration tests load the SQL definitions into the target schema before execution.

## Crosscutting Concepts

### Traceability

Requirements are defined in `../system_requirements/system_requirements.md` and linked detail documents.
Design items in this document cover function requirements where technical decisions are needed.
Source code and tests provide lower-level coverage.

### Testing

Implementation is verified primarily through integration tests that execute the functions in Exasol.

### Lua Scalar Functions

Lua scalar functions are implemented as standalone Exasol Lua scalar script definitions under `../../exasol/more_functions/lua/scalar`.

#### Function Source Loader Selection
`dsn~function-source-loader-selection~1`

The integration-test function loader selects the source format from the file extension: SQL function definitions use `.sql` files and Lua function sources use `.lua` files. SQL source content is executed unchanged; Lua source content is prepared according to the Lua source-header design.

Needs: utest

#### Lua Function Source Header
`dsn~lua-function-source-header~1`

Lua function sources are stored as `.lua` files in their respective function categories. Their Exasol SQL declaration lines use the `--| ` prefix; the remaining lines are ordinary Lua code. Before execution, the Lua loader removes the prefix from the declaration lines and appends the SQL script terminator.

Needs: utest

## Architecture Decisions

- Functions are documented individually in dedicated requirement files.
- SQL scalar functions are stored one function per file.
- Lua scalar functions are stored one function per file.
- Scenario text remains in the requirement files and is not duplicated in the design.

## Risks And Technical Debt

- SQL and Lua functions may require different testing and deployment patterns.
- Exasol-specific behavior such as empty-string handling must be documented explicitly to avoid false assumptions.

## Open Issues

### Functions That Need to be Implemented in the Core Database

The following functions were investigated in the cause of creating `more-functions` and were deemed to be not feasible with SQL functions, Lua Scripts and UDFs

#### ADDDATE / DATE_ADD, ADDTIME / TIME_ADD

Requires complex interval types as parameters which Exasol does not have yet.

#### BENCHMARK

```sql
BENCHMARK(n, <expression>)
```

The second parameter of benchmark works like a function pointer, since benchmark runs the given function _n_ times to allow timing it. Such a function pointer is not possible with add-on-functions.

## Glossary

- Exasol: The target database system.
- OFT: OpenFastTrace, used for tracing requirements, design, implementation, and tests.
