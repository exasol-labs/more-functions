# DATABASE
`req~metadata-database-function~1`

The scalar function `DATABASE()` returns the current Exasol schema name.
Exasol has no separate database catalog level, so the current schema is the
closest available MariaDB-compatible result.

Needs: scn

Covers:
- `feat~scalar-functions~1`

## DATABASE Invocation
`scn~metadata-database-function~1`

**Given** a caller has an active Exasol session
**When** the caller invokes `DATABASE()`
**Then** the function returns the name of the current schema.

Needs: dsn

Covers:
- `req~metadata-database-function~1`
