-- [impl -> dsn~lua-function-source-header~1]
--| CREATE OR REPLACE LUA SCALAR SCRIPT version()
--| RETURNS VARCHAR(128) AS
function run(_)
    -- [impl -> req~metadata-version-function~1]
    return exa.meta.database_version
end
