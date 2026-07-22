# QUOTE
`req~quote-function~1`

The scalar SQL function `quote(value)` converts an input value into an SQL string literal representation that can be embedded into generated SQL statements safely with respect to single-quote escaping.

Rationale:

Callers need a database-side helper that turns values into SQL string literals without reimplementing quoting rules in every query or script.

Needs: scn, dsn

Covers:
- `feat~scalar-functions~1`

## QUOTE: Null Input
`scn~quote-null~1`

**Given** `NULL`
**When** `quote(value)` is executed
**Then** the function returns the text `NULL`.

Needs: dsn

Covers:
- `req~quote-function~1`

## QUOTE: Empty String Input In Exasol
`scn~quote-empty-string~1`

**Given** an empty string
**When** Exasol evaluates the call
**Then** Exasol treats the input as `NULL`
**And** `quote(value)` therefore returns the text `NULL`.

Needs: dsn

Covers:
- `req~quote-function~1`

## QUOTE: Non-empty String
`scn~quote-non-empty-string~1`

**Given** a non-empty string value that contains one or more single quote characters
**When** `quote(value)` is executed
**Then** the function returns the value wrapped in single quotes
**And** each embedded escaped by doubling it.

Needs: dsn

Covers:
- `req~quote-function~1`
