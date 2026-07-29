-- [impl -> dsn~metadata-backed-lua-functions~1]
-- [impl -> dsn~lua-function-source-header~1]
--| CREATE OR REPLACE LUA SCALAR SCRIPT system_user()
--| RETURNS VARCHAR(128) AS
function run(_)
    -- [impl -> dsn~metadata-backed-lua-functions-system-user~1]
    return exa.meta.current_user
end
