# BIN
`req~bin-function~1`

The scalar function `BIN(value)` returns the binary representation of the 64-bit integer value produced from an integer-valued input. Values above `18446744073709551615` saturate to that maximum, values at or below `-18446744073709551616` saturate to that maximum, values in the range `-18446744073709551615` to `-1` are interpreted as unsigned 64-bit residues, and bits above the 64-bit range are ignored.

Needs: scn

Covers:
- `feat~scalar-functions~1`

## BIN: Null Input
`scn~bin-null~1`

**Given** `NULL`
**When** `BIN(value)` is executed
**Then** the function returns `NULL`.

Needs: dsn

Covers:
- `req~bin-function~1`

## BIN: Integer-Valued Input
`scn~bin-integer-literal~1`

**Given** an integer-valued input
**When** `BIN(value)` is executed
**Then** the function returns the binary representation of that integer-valued input without leading zeros, except that zero is returned as `0`.

Needs: dsn

Covers:
- `req~bin-function~1`

## BIN: Exact Numeric Integer-Valued Input
`scn~bin-exact-numeric-integer~1`

**Given** an exact numeric integer-valued input
**When** `BIN(value)` is executed
**Then** the function returns the same result as for the corresponding integer-valued input.

Needs: dsn

Covers:
- `req~bin-function~1`

## BIN: Floating-Point Integer-Valued Input
`scn~bin-floating-point-integer~1`

**Given** a floating-point integer-valued input
**When** `BIN(value)` is executed
**Then** the function returns the same result as for the corresponding integer-valued input.

Needs: dsn

Covers:
- `req~bin-function~1`

## BIN: Input With Bits Above 64 Bits
`scn~bin-ignore-higher-bits~1`

**Given** an integer-valued input with bits above the low 64 bits set
**When** `BIN(value)` is executed
**Then** the function returns the binary representation of the 64-bit integer value produced from the integer-valued input and ignores all higher bits.

Needs: dsn

Covers:
- `req~bin-function~1`
