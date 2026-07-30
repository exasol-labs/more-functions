-- [impl -> dsn~lua-function-source-header~1]
--| CREATE OR REPLACE LUA SCALAR SCRIPT connection_id()
--| RETURNS VARCHAR(128) AS
function run(_)
    -- [impl -> req~metadata-connection-id-function~1]
    return exa.meta.session_id
end
