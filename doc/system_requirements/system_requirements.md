# System Requirements

This document is the entry point for user-facing requirements of `more-functions`.
Detailed requirements for individual functions live in dedicated files below ``.

## Features

### Scalar Functions
`feat~scalar-functions~1`

`more-functions` provides a set of SQL and Lua functions that extend Exasol with functionality that is useful in practice but not built into the database engine directly.

Needs: req

Status: approved

### High-level Requirements

#### Scalar Functions

- [BIT_COUNT](scalar_functions/bit_count.md)
- [DATABASE](scalar_functions/database.md)
- [CONNECTION_ID](scalar_functions/connection_id.md)
- [VERSION](scalar_functions/version.md)
- [QUOTE](scalar_functions/quote.md)
- [ST_* Aliases](scalar_functions/st_aliases.md)
- [SYS.* Functions](scalar_functions/sys_functions.md)
