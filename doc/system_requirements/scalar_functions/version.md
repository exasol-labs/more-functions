# VERSION
`req~version-function~1`

The scalar function `VERSION()` returns the Exasol database version string.

Needs: scn

Covers:
- `feat~scalar-functions~1`

## VERSION Invocation
`scn~version-returns-exasol-db-version~1`

**Given** a caller has an active Exasol session
**When** the caller invokes `VERSION()`
**Then** the function returns the Exasol database version string.

Needs: dsn

Covers:
- `req~version-function~1`
