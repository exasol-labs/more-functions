# CONNECTION_ID
`req~connection-id-function~1`

The scalar function `CONNECTION_ID()` returns the current Exasol session identifier.

Needs: scn

Covers:
- `feat~scalar-functions~1`

## CONNECTION_ID Invocation
`scn~connection-id-returns-current-session~1`

**Given** a caller has an active Exasol session
**When** the caller invokes `CONNECTION_ID()`
**Then** the function returns the identifier of the current Exasol session.

Needs: dsn

Covers:
- `req~connection-id-function~1`
