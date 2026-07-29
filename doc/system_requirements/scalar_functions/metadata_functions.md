# MariaDB-Compatible Information Functions

## MariaDB-Compatible Information Functions
`req~metadata-backed-lua-functions~1`

`more-functions` provides the following no-argument MariaDB-compatible scalar
functions for accessing information about the current Exasol session and
database:

| Function              | Result                            |
|-----------------------|-----------------------------------|
| `CURRENT_SCHEMA()`    | Name of the current schema        |
| `DATABASE()`          | Name of the current database      |
| `SCHEMA()`            | Name of the current database      |
| `CONNECTION_ID()`     | Identifier of the current session |
| `VERSION()`           | Database version                  |
| `SESSION_USER()`      | Current user                      |
| `SYSTEM_USER()`       | Current user                      |

`DATABASE()` and `SCHEMA()` are aliases and return the same database name.

Needs: scn, dsn

Covers:
- `feat~scalar-functions~1`

## CURRENT_SCHEMA Invocation
`scn~metadata-backed-lua-functions-current-schema~1`
**Given** a caller has an active Exasol session
**When** the caller invokes `CURRENT_SCHEMA()`
**Then** the function returns the name of the current schema.

Needs: dsn

Covers:
- `req~metadata-backed-lua-functions~1`

## DATABASE Invocation
`scn~metadata-backed-lua-functions-database~1`
**Given** a caller has an active Exasol session
**When** the caller invokes `DATABASE()`
**Then** the function returns the name of the current schema.

Rationale:

Exasol does not have databases as a catalog level, schema is the next best match.

Needs: dsn

Covers:
- `req~metadata-backed-lua-functions~1`

## SCHEMA Invocation
`scn~metadata-backed-lua-functions-schema~1`
**Given** a caller has an active Exasol session
**When** the caller invokes `SCHEMA()`
**Then** the function returns the name of the current schema.

Needs: dsn

Covers:
- `req~metadata-backed-lua-functions~1`

## CONNECTION_ID Invocation
`scn~metadata-backed-lua-functions-connection-id~1`
**Given** a caller has an active Exasol session
**When** the caller invokes `CONNECTION_ID()`
**Then** the function returns the identifier of the current Exasol session.

Needs: dsn

Covers:
- `req~metadata-backed-lua-functions~1`

## VERSION Invocation
`scn~metadata-backed-lua-functions-version~1`
**Given** a caller has an active Exasol session
**When** the caller invokes `VERSION()`
**Then** the function returns the Exasol database version.

Needs: dsn

Covers:
- `req~metadata-backed-lua-functions~1`

## SYS.VERSION_MAJOR Invocation
`scn~metadata-backed-lua-functions-version-major~1`
**Given** the Exasol database version has major, minor, and patch decimal
components separated by periods
**When** the caller invokes `SYS.VERSION_MAJOR()`
**Then** the function returns the major component of the database version.

Needs: dsn

Covers:
- `req~metadata-backed-lua-functions~1`

## SYS.VERSION_MINOR Invocation
`scn~metadata-backed-lua-functions-version-minor~1`
**Given** the Exasol database version has major, minor, and patch decimal
components separated by periods
**When** the caller invokes `SYS.VERSION_MINOR()`
**Then** the function returns the minor component of the database version.

Needs: dsn

Covers:
- `req~metadata-backed-lua-functions~1`

## SYS.VERSION_PATCH Invocation
`scn~metadata-backed-lua-functions-version-patch~1`
**Given** the Exasol database version has major, minor, and patch decimal
components separated by periods
**When** the caller invokes `SYS.VERSION_PATCH()`
**Then** the function returns the patch component of the database version.

Needs: dsn

Covers:
- `req~metadata-backed-lua-functions~1`

## SESSION_USER Invocation
`scn~metadata-backed-lua-functions-session-user~1`
**Given** a caller has an active Exasol session
**When** the caller invokes `SESSION_USER()`
**Then** the function returns the current Exasol user.

Needs: dsn

Covers:
- `req~metadata-backed-lua-functions~1`

## SYSTEM_USER Invocation
`scn~metadata-backed-lua-functions-system-user~1`
**Given** a caller has an active Exasol session
**When** the caller invokes `SYSTEM_USER()`
**Then** the function returns the current Exasol user.

Needs: dsn

Covers:
- `req~metadata-backed-lua-functions~1`
