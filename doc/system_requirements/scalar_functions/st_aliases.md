# ST_* Aliases

## MariaDB-Compatible Geospatial Aliases
`req~st-alias-functions~1`

`more-functions` provides the MariaDB-compatible unprefixed aliases for the available Exasol geospatial `ST_*` functions identified in the function coverage matrix. Each alias accepts the same parameters as its corresponding `ST_*` function and returns its result unchanged. Aliases whose MariaDB semantics require a binary type are not provided because Exasol has no binary type and therefore no corresponding `ST_*` function.

Needs: scn

Covers:
- `feat~scalar-functions~1`

## ST_* Alias Invocation
`scn~st-alias-functions~1`

**Given** a geospatial operation for which MariaDB defines an unprefixed alias and Exasol provides the corresponding `ST_*` function
**When** a caller invokes the alias with valid parameters for that operation
**Then** the alias accepts those parameters and returns the result of the corresponding Exasol `ST_*` function

Needs: dsn

Covers:
- `req~st-alias-functions~1`
