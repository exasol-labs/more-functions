# Add A New Function

When adding a new function to `more-functions`, update these artifacts in this order:

1. Add or update the user-facing requirement in `../doc/system_requirements/system_requirements.md` and the matching sub-document in `doc/system_requirements/`.
2. Add or update the technical design and OFT forwarding in `../doc/design/design.md`.
3. Add the function source under the matching implementation directory:
   `exasol/more_functions/sql/scalar/`, `exasol/more_functions/lua/scalar/`, or the corresponding analytic or set directory.
4. Add OFT implementation coverage tags in the function source.
5. Add integration tests under `test/integration/more_functions/`.
6. Add OFT integration-test coverage tags in the tests.
7. Update user-facing inventory and release notes:
   `doc/user_guide/function_coverage.md`, `README.rst`, and `doc/changes/unreleased.md` as needed.
8. Run the relevant integration tests and keep the OFT trace clean.
