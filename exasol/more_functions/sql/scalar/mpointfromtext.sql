-- [impl -> dsn~st-alias-functions~1]
create or replace function mpointfromtext (value varchar(2000000)) return geometry is begin return st_mpointfromtext(value); end mpointfromtext;
/
