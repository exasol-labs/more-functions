def test_backend_connection_smoke(connection):
    rows = connection.execute('SELECT 1 FROM DUAL').fetchall()
    assert len(rows) == 1
