# Design

This document describes the technical design of `more-functions` in an arc42-style structure.
It intentionally omits sections dedicated to user requirements.

## Architecture Constraints

- Functions are implemented for Exasol.
- The repository may contain SQL functions and Lua functions.
- Behavior is specified in `doc/system_requirements.md` and linked detail files.
- Verification is performed through automated tests in this repository.

### SQL Functions vs. Lua Scripts

SQL functions are closer to the database engine, so they can be optimized better. That being said, there are a number of technical limitations that narrow down where SQL functions are applicable.

| Feature                           |   SQL Functions    |  Lua Scripts  |
|-----------------------------------|:------------------:|:-------------:|
| Parameter type overloading        |                    | ✓[^1]         |
| Variable-length parameterlist     |                    |       ✓       |
| Logic                             |    if and loop     | full language |
| Access to built-in SQL functions  |         ✓          |               |

[^1]: Simulated via variable-length parameter list

## Context And Scope

`more-functions` provides database-side functions for Exasol users.
The repository supplies function definitions and automated tests.

## Solution Strategy

The solution keeps each supported function small and self-contained.
Each function has:

- a user-facing requirement in `doc/system_requirements/`
- a design item in this document if the design adds technical information
- automated tests that verify the implemented behavior

Behavior belongs in the system requirements.
This design document records technical structure, implementation decisions, and forwarding to verification artifacts.

## Building Block View

The system consists of these main building blocks:

- SQL scalar functions
- Lua functions
- automated tests

### SQL Scalar Functions

SQL scalar functions are implemented as standalone Exasol SQL function definitions under `exasol/more_functions/sql/scalar/`.

#### QUOTE Function Design
`dsn~quote-function~1`

The `quote` function is implemented as an Exasol SQL scalar function.
It returns the text `NULL` for null input.
For non-null input it wraps the value in single quotes and escapes embedded single quotes by doubling them.

Needs: impl

Covers:
- `req~quote-function~1`

### Lua Scalar Functions

Lua scalar functions are implemented as standalone Exasol Lua scalar script definitions under `exasol/more_functions/lua/scalar/`.

#### BIT_COUNT Function Design
`dsn~bit-count-function~2`

The `bit_count` function is implemented as an Exasol Lua scalar script with a `DECIMAL(36,0)` input parameter.
For `NULL` input it returns `NULL`.
For non-null integer-valued input it counts the set bits in the low 64 bits and returns that count.
The implementation normalizes negative values into a two's-complement representation, extracts its two low 32-bit blocks, and counts the set bits in each block with Lua integer bit operations. It deliberately does not process higher blocks; in particular, it retains the upper 32-bit block of the low 64-bit word.

Needs: impl

Covers:
- `req~bit-count-function~2`

## Runtime View

At runtime the caller executes the scalar function inside Exasol.
The function evaluates the input, distinguishes null from non-null values, performs SQL-literal escaping for single quotes, and returns the resulting string.

The scenario requirements are forwarded to verification without repeating them here:

### AREA (Alias of ST_AREA)

dsn --> impl, itest : req~area-function~1 

### QUOTE

dsn --> impl, itest : scn~quote-null~1
dsn --> impl, itest : scn~quote-empty-string~1
dsn --> impl, itest : scn~quote-non-empty-string~1

### BIT_COUNT

dsn --> impl, itest : scn~bit-count-null~1
dsn --> impl, itest : scn~bit-count-integer-literal~1
dsn --> impl, itest : scn~bit-count-exact-numeric-integer~1
dsn --> impl, itest : scn~bit-count-floating-point-integer~1
dsn --> impl, itest : scn~bit-count-ignore-higher-bits~1

## Deployment View

The function definitions are deployed into an Exasol database schema.
Automated integration tests load the SQL definitions into the target schema before execution.

## Crosscutting Concepts

### Traceability

Requirements are defined in `doc/system_requirements.md` and linked detail documents.
Design items in this document cover function requirements where technical decisions are needed.
Source code and tests provide lower-level coverage.

### Testing

Implementation is verified primarily through integration tests that execute the functions in Exasol.

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
