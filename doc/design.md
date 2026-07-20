# Design

This document describes the technical design of `more-functions` in an arc42-style structure.
It intentionally omits sections dedicated to user requirements.

## Architecture Constraints

- Functions are implemented for Exasol.
- The repository may contain SQL functions and Lua functions.
- Behavior is specified in `doc/system_requirements.md` and linked detail files.
- Verification is performed through automated tests in this repository.

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

#### SQL Scalar Functions

SQL scalar functions are implemented as standalone Exasol SQL function definitions under `exasol/more_functions/sql/scalar/`.

#### QUOTE Function Design
`dsn~quote-function~1`

The `quote` function is implemented as an Exasol SQL scalar function in [exasol/more_functions/sql/scalar/quote.sql](/home/seb/git/more-functions/exasol/more_functions/sql/scalar/quote.sql).
It returns the text `NULL` for null input.
For non-null input it wraps the value in single quotes and escapes embedded single quotes by doubling them.

Needs: impl

Covers:
- `req~quote-function~1`

## Runtime View

At runtime the caller executes the scalar function inside Exasol.
The function evaluates the input, distinguishes null from non-null values, performs SQL-literal escaping for single quotes, and returns the resulting string.

The scenario requirements are forwarded to verification without repeating them here:

dsn --> impl, itest : scn~quote-null~1
dsn --> impl, itest : scn~quote-empty-string~1
dsn --> impl, itest : scn~quote-non-empty-string~1

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
- Scenario text remains in the requirement files and is not duplicated in the design.

## Risks And Technical Debt

- SQL and Lua functions may require different testing and deployment patterns.
- Exasol-specific behavior such as empty-string handling must be documented explicitly to avoid false assumptions.

## Glossary

- Exasol: The target database system.
- OFT: OpenFastTrace, used for tracing requirements, design, implementation, and tests.
