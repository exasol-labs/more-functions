# Building Block View

The system consists of these main building blocks:

- SQL scalar functions
- Lua functions
- automated tests

## Scalar Functions

SQL scalar functions are implemented as standalone Exasol SQL function definitions under `../../exasol/more_functions/sql/scalar`.

Lua scalar functions are implemented under `../../exasol/more_functions/lua/scalar` as Lua files. For integration tests and to create the installation package, they are wrapped in a thin SQL declaration.
