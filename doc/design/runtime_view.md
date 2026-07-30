# Runtime View

At runtime the caller executes the scalar function inside Exasol.
The function evaluates the input, distinguishes null from non-null values, performs SQL-literal escaping for single quotes, and returns the resulting string.

The scenario requirements are forwarded to verification without repeating them here:

## BIT_COUNT

dsn --> impl, itest : scn~bit-count-null~1
dsn --> impl, itest : scn~bit-count-integer-literal~1
dsn --> impl, itest : scn~bit-count-exact-numeric-integer~1
dsn --> impl, itest : scn~bit-count-floating-point-integer~1
dsn --> impl, itest : scn~bit-count-ignore-higher-bits~1

## CONNECTION_ID

dsn --> impl, itest : scn~connection-id-returns-current-session~1

## DATABASE

dsn --> impl, itest : scn~database-returns-current-schema~1

## QUOTE

dsn --> impl, itest : scn~quote-null~1
dsn --> impl, itest : scn~quote-empty-string~1
dsn --> impl, itest : scn~quote-non-empty-string~1

## ST_* Alias Functions

dsn --> impl, itest : scn~st-alias-functions~1

## VERSION

dsn --> impl, itest : scn~version-returns-exasol-db-version~1