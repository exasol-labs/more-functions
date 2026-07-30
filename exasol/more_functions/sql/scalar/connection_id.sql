create or replace function connection_id ()
return decimal(20,0)
is
begin
    -- [impl -> dsn~connection-id-returns-current-session~1]
    return current_session;
end connection_id;
/
