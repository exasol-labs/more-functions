##### BIT_COUNT Function
`req~bit-count-function~1`

The scalar function `BIT_COUNT(value)` returns the number of bits that are set to `1` in the binary representation of an integer value, compatible with MariaDB's `BIT_COUNT(value)` behavior.

Needs: scn, dsn

Covers:
- `feat~scalar-functions~1`

##### BIT_COUNT: Null Input
`scn~bit-count-null~1`

**Given** `NULL`
**When** `BIT_COUNT(value)` is executed
**Then** the function returns `NULL`.

Needs: dsn

Covers:
- `req~bit-count-function~1`

##### BIT_COUNT: Integer Literal Input
`scn~bit-count-integer-literal~1`

**Given** an integer literal
**When** `BIT_COUNT(value)` is executed
**Then** the function returns the number of bits set to `1` in that integer value

Needs: dsn

Covers:
- `req~bit-count-function~1`

##### BIT_COUNT: Exact Numeric Input Representing An Integer
`scn~bit-count-exact-numeric-integer~1`

**Given** an exact numeric value whose numeric value is an integer
**When** `BIT_COUNT(value)` is executed
**Then** the function returns the same result as for the corresponding integer literal.

Needs: dsn

Covers:
- `req~bit-count-function~1`

##### BIT_COUNT: Floating-Point Input Representing An Integer
`scn~bit-count-floating-point-integer~1`

**Given** a floating-point value whose numeric value is an integer
**When** `BIT_COUNT(value)` is executed
**Then** the function returns the same result as for the corresponding integer literal.

Needs: dsn

Covers:
- `req~bit-count-function~1`
