-- [impl -> req~metadata-connection-id-function~1]
create or replace function connection_id ()
return decimal(20,0)
is
begin
    return current_session;
end connection_id;
/
