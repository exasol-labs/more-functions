def test_backend_connection_smoke(connection):
    connection.execute('create schema test_schema')
    connection.execute('open schema test_schema')
    with open('exasol/more_functions/sql/string_functions/quote.sql') as file:
        sql = file.read()
    connection.execute(sql)
    result = connection.execute("select quote('Hello ''World''!')").fetchall()
    assert result[0][0] == 'Hello \'World\''