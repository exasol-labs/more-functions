-- [impl -> dsn~metadata-backed-lua-functions~1]
-- [impl -> dsn~lua-function-source-header~1]
--| CREATE OR REPLACE LUA SCALAR SCRIPT connection_id()
--| RETURNS DECIMAL(20,0) AS
function run(_)
    -- [impl -> dsn~metadata-backed-lua-functions-connection-id~1]
    return exa.meta.session_id
end
