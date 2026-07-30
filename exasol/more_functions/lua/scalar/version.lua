--| CREATE OR REPLACE LUA SCALAR SCRIPT version()
--| RETURNS VARCHAR(128) AS
function run(_)
    -- [impl -> dsn~version-returns-exasol-db-version~1]
    return exa.meta.database_version
end
