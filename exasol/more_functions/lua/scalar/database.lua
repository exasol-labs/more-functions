-- [impl -> dsn~lua-function-source-header~1]
--| CREATE OR REPLACE LUA SCALAR SCRIPT database()
--| RETURNS VARCHAR(128) AS
function run(_)
    -- [impl -> req~metadata-database-function~1]
    return exa.meta.current_schema
end
