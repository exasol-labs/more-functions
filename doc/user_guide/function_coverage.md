# Function Coverage

In this project we picked the open source MariaDB as the northstar, since they have a very broad coverage of useful functions.
This table compares the official MariaDB function index for the latest stable release,

## Baseline

1. **MariaDB 12.3.2** (released **2026-05-29**)
2. **Exasol 2026.1.0** (released **2026-05-15**)
Sources:

- MariaDB releases: https://mariadb.org/mariadb/all-releases/
- MariaDB function index: https://mariadb.com/docs/server/reference/sql-functions/function-and-operator-reference.md
- Exasol built-in function catalog: https://docs.exasol.com/db/latest/sql_references/functions/all_functions.htm


## Coverage

| Function                               | Type     | Domain             | MariaDB | Exasol      |
|----------------------------------------|----------|--------------------|---------|-------------|
| `ABS`                                  | scalar   | math               | ✓       | ✓           |
| `ACOS`                                 | scalar   | math               | ✓       | ✓           |
| `ADD_MONTHS`                           | scalar   | date/time          | ✓       | ✓           |
| `ADDDATE`                              | scalar   | date/time          | ✓       |             |
| `ADDTIME`                              | scalar   | date/time          | ✓       |             |
| `AES_DECRYPT`                          | scalar   | crypto/compression | ✓       |             |
| `AES_ENCRYPT`                          | scalar   | crypto/compression | ✓       |             |
| `AREA`                                 | scalar   | geo                | ✓       | + → ST_AREA |
| `AsBinary`                             | scalar   | geo                | ✓       |             |
| `ASCII`                                | scalar   | string             | ✓       | ✓           |
| `ASIN`                                 | scalar   | math               | ✓       | ✓           |
| `AsText`                               | scalar   | geo                | ✓       |             |
| `AsWKB`                                | scalar   | geo                | ✓       |             |
| `AsWKT`                                | scalar   | geo                | ✓       |             |
| `ATAN`                                 | scalar   | math               | ✓       | ✓           |
| `ATAN2`                                | scalar   | math               | ✓       | ✓           |
| `AVG`                                  | set      | aggregate          | ✓       | ✓           |
| `BENCHMARK`                            | scalar   | information        | ✓       |             |
| `BIN`                                  | scalar   | string             | ✓       |             |
| `BINLOG_GTID_POS`                      | scalar   | information        | ✓       |             |
| `BIT_AND`                              | set      | aggregate          | ✓       | ✓           |
| `BIT_COUNT`                            | scalar   | bitwise            | ✓       |             |
| `BIT_LENGTH`                           | scalar   | string             | ✓       | ✓           |
| `BIT_OR`                               | set      | aggregate          | ✓       | ✓           |
| `BIT_XOR`                              | set      | aggregate          | ✓       | ✓           |
| `BOUNDARY`                             | scalar   | geo                | ✓       |             |
| `BUFFER`                               | scalar   | geo                | ✓       |             |
| `CASE`                                 | scalar   | control flow       | ✓       | ✓           |
| `CAST`                                 | scalar   | string             | ✓       | ✓           |
| `CEIL`                                 | scalar   | math               | ✓       |             |
| `CEILING`                              | scalar   | math               | ✓       |             |
| `CENTROID`                             | scalar   | geo                | ✓       |             |
| `CHARACTER_LENGTH`                     | scalar   | string             | ✓       | ✓           |
| `CHAR_LENGTH`                          | scalar   | string             | ✓       |             |
| `CHARSET`                              | scalar   | information        | ✓       |             |
| `CHR`                                  | scalar   | string             | ✓       |             |
| `COALESCE`                             | scalar   | misc               | ✓       | ✓           |
| `COERCIBILITY`                         | scalar   | information        | ✓       |             |
| `COLLATION`                            | scalar   | information        | ✓       |             |
| `COLUMN_ADD`                           | scalar   | dynamic columns    | ✓       |             |
| `COLUMN_CHECK`                         | scalar   | dynamic columns    | ✓       |             |
| `COLUMN_CREATE`                        | scalar   | dynamic columns    | ✓       |             |
| `COLUMN_DELETE`                        | scalar   | dynamic columns    | ✓       |             |
| `COLUMN_EXISTS`                        | scalar   | dynamic columns    | ✓       |             |
| `COLUMN_GET`                           | scalar   | dynamic columns    | ✓       |             |
| `COLUMN_JSON`                          | scalar   | dynamic columns    | ✓       |             |
| `COLUMN_LIST`                          | scalar   | dynamic columns    | ✓       |             |
| `COMPRESS`                             | scalar   | crypto/compression | ✓       |             |
| `CONCAT`                               | scalar   | string             | ✓       | ✓           |
| `CONCAT_WS`                            | scalar   | string             | ✓       |             |
| `CONNECTION_ID`                        | scalar   | information        | ✓       |             |
| `CONTAINS`                             | scalar   | geo                | ✓       |             |
| `CONVERT`                              | scalar   | string             | ✓       | ✓           |
| `CONV`                                 | scalar   | math               | ✓       |             |
| `CONVERT_TZ`                           | scalar   | date/time          | ✓       | ✓           |
| `CONVEXHULL`                           | scalar   | geo                | ✓       |             |
| `COS`                                  | scalar   | math               | ✓       | ✓           |
| `COT`                                  | scalar   | math               | ✓       | ✓           |
| `COUNT`                                | set      | aggregate          | ✓       | ✓           |
| `CRC32`                                | scalar   | math               | ✓       |             |
| `CRC32C`                               | scalar   | math               | ✓       |             |
| `CROSSES`                              | scalar   | geo                | ✓       |             |
| `CUME_DIST`                            | analytic | window             | ✓       | ✓           |
| `CURDATE`                              | scalar   | date/time          | ✓       | ✓           |
| `CURRENT_DATE`                         | scalar   | date/time          | ✓       | ✓           |
| `CURRENT_ROLE`                         | scalar   | information        | ✓       |             |
| `CURRENT_TIME`                         | scalar   | date/time          | ✓       |             |
| `CURRENT_TIMESTAMP`                    | scalar   | date/time          | ✓       | ✓           |
| `CURRENT_USER`                         | scalar   | information        | ✓       | ✓           |
| `CURTIME`                              | scalar   | date/time          | ✓       |             |
| `DATABASE`                             | scalar   | information        | ✓       |             |
| `DATEDIFF`                             | scalar   | date/time          | ✓       |             |
| `DATE_ADD`                             | scalar   | date/time          | ✓       |             |
| `DATE_FORMAT`                          | scalar   | date/time          | ✓       |             |
| `DATE_SUB`                             | scalar   | date/time          | ✓       |             |
| `DAY`                                  | scalar   | date/time          | ✓       | ✓           |
| `DAYNAME`                              | scalar   | date/time          | ✓       |             |
| `DAYOFMONTH`                           | scalar   | date/time          | ✓       |             |
| `DAYOFWEEK`                            | scalar   | date/time          | ✓       | ✓           |
| `DAYOFYEAR`                            | scalar   | date/time          | ✓       |             |
| `DECODE`                               | scalar   | crypto/compression | ✓       | ✓           |
| `DECODE_HISTOGRAM`                     | scalar   | information        | ✓       |             |
| `DEFAULT`                              | scalar   | information        | ✓       |             |
| `DEGREES`                              | scalar   | math               | ✓       | ✓           |
| `DENSE_RANK`                           | analytic | window             | ✓       | ✓           |
| `DES_DECRYPT`                          | scalar   | crypto/compression | ✓       |             |
| `DES_ENCRYPT`                          | scalar   | crypto/compression | ✓       |             |
| `DIMENSION`                            | scalar   | geo                | ✓       |             |
| `DISJOINT`                             | scalar   | geo                | ✓       |             |
| `DIV`                                  | scalar   | math               | ✓       | ✓           |
| `ELT`                                  | scalar   | string             | ✓       |             |
| `ENCODE`                               | scalar   | crypto/compression | ✓       |             |
| `ENCRYPT`                              | scalar   | crypto/compression | ✓       |             |
| `ENDPOINT`                             | scalar   | geo                | ✓       |             |
| `ENVELOPE`                             | scalar   | geo                | ✓       |             |
| `EQUALS`                               | scalar   | geo                | ✓       |             |
| `EXP`                                  | scalar   | math               | ✓       | ✓           |
| `EXPORT_SET`                           | scalar   | string             | ✓       |             |
| `ExteriorRing`                         | scalar   | geo                | ✓       |             |
| `EXTRACT`                              | scalar   | date/time          | ✓       | ✓           |
| `EXTRACTVALUE`                         | scalar   | string             | ✓       |             |
| `FIELD`                                | scalar   | string             | ✓       |             |
| `FIND_IN_SET`                          | scalar   | string             | ✓       |             |
| `FLOOR`                                | scalar   | math               | ✓       | ✓           |
| `FORMAT`                               | scalar   | string             | ✓       |             |
| `FORMAT_BYTES`                         | scalar   | misc               | ✓       |             |
| `FORMAT_PICO_TIME`                     | scalar   | date/time          | ✓       |             |
| `FOUND_ROWS`                           | scalar   | information        | ✓       |             |
| `FROM_BASE64`                          | scalar   | string             | ✓       |             |
| `FROM_DAYS`                            | scalar   | date/time          | ✓       |             |
| `FROM_UNIXTIME`                        | scalar   | date/time          | ✓       |             |
| `GeomCollFromText`                     | scalar   | geo                | ✓       |             |
| `GeomCollFromWKB`                      | scalar   | geo                | ✓       |             |
| `GEOMETRYCOLLECTION`                   | scalar   | geo                | ✓       |             |
| `GeometryCollectionFromText`           | scalar   | geo                | ✓       |             |
| `GeometryCollectionFromWKB`            | scalar   | geo                | ✓       |             |
| `GeometryFromText`                     | scalar   | geo                | ✓       |             |
| `GeometryFromWKB`                      | scalar   | geo                | ✓       |             |
| `GeomFromText`                         | scalar   | geo                | ✓       |             |
| `GeomFromWKB`                          | scalar   | geo                | ✓       |             |
| `GeometryN`                            | scalar   | geo                | ✓       |             |
| `GeometryType`                         | scalar   | geo                | ✓       |             |
| `GET_FORMAT`                           | scalar   | date/time          | ✓       |             |
| `GET_LOCK`                             | scalar   | misc               | ✓       |             |
| `GLENGTH`                              | scalar   | geo                | ✓       |             |
| `GREATEST`                             | scalar   | misc               | ✓       | ✓           |
| `GROUP_CONCAT`                         | set      | aggregate          | ✓       | ✓           |
| `HEX`                                  | scalar   | string             | ✓       |             |
| `HOUR`                                 | scalar   | date/time          | ✓       | ✓           |
| `IF`                                   | scalar   | control flow       | ✓       | ✓           |
| `IFNULL`                               | scalar   | control flow       | ✓       | ✓           |
| `INTERVAL`                             | scalar   | misc               | ✓       |             |
| `INET6_ATON`                           | scalar   | misc               | ✓       |             |
| `INET6_NTOA`                           | scalar   | misc               | ✓       |             |
| `INET_ATON`                            | scalar   | misc               | ✓       |             |
| `INET_NTOA`                            | scalar   | misc               | ✓       |             |
| `INSTR`                                | scalar   | string             | ✓       | ✓           |
| `InteriorRingN`                        | scalar   | geo                | ✓       |             |
| `INTERSECTS`                           | scalar   | geo                | ✓       |             |
| `IsClosed`                             | scalar   | geo                | ✓       |             |
| `IsEmpty`                              | scalar   | geo                | ✓       |             |
| `IS_FREE_LOCK`                         | scalar   | misc               | ✓       |             |
| `IS_IPV4`                              | scalar   | misc               | ✓       |             |
| `IS_IPV4_COMPAT`                       | scalar   | misc               | ✓       |             |
| `IS_IPV4_MAPPED`                       | scalar   | misc               | ✓       |             |
| `IS_IPV6`                              | scalar   | misc               | ✓       |             |
| `ISNULL`                               | scalar   | misc               | ✓       |             |
| `IsRing`                               | scalar   | geo                | ✓       |             |
| `IsSimple`                             | scalar   | geo                | ✓       |             |
| `IS_USED_LOCK`                         | scalar   | misc               | ✓       |             |
| `JSON_ARRAY`                           | scalar   | json               | ✓       |             |
| `JSON_ARRAYAGG`                        | set      | aggregate          | ✓       |             |
| `JSON_ARRAY_INTERSECT`                 | scalar   | json               | ✓       |             |
| `JSON_ARRAY_APPEND`                    | scalar   | json               | ✓       |             |
| `JSON_ARRAY_INSERT`                    | scalar   | json               | ✓       |             |
| `JSON_COMPACT`                         | scalar   | json               | ✓       |             |
| `JSON_CONTAINS`                        | scalar   | json               | ✓       |             |
| `JSON_CONTAINS_PATH`                   | scalar   | json               | ✓       |             |
| `JSON_DEPTH`                           | scalar   | json               | ✓       |             |
| `JSON_DETAILED`                        | scalar   | json               | ✓       |             |
| `JSON_EQUALS`                          | scalar   | json               | ✓       |             |
| `JSON_EXISTS`                          | scalar   | json               | ✓       |             |
| `JSON_EXTRACT`                         | scalar   | json               | ✓       | ✓           |
| `JSON_INSERT`                          | scalar   | json               | ✓       |             |
| `JSON_KEY_VALUE`                       | scalar   | json               | ✓       |             |
| `JSON_KEYS`                            | scalar   | json               | ✓       |             |
| `JSON_LENGTH`                          | scalar   | json               | ✓       |             |
| `JSON_LOOSE`                           | scalar   | json               | ✓       |             |
| `JSON_MERGE`                           | scalar   | json               | ✓       |             |
| `JSON_MERGE_PATCH`                     | scalar   | json               | ✓       |             |
| `JSON_MERGE_PRESERVE`                  | scalar   | json               | ✓       |             |
| `JSON_NORMALIZE`                       | scalar   | json               | ✓       |             |
| `JSON_OBJECT`                          | scalar   | json               | ✓       |             |
| `JSON_OBJECT_FILTER_KEYS`              | scalar   | json               | ✓       |             |
| `JSON_OBJECT_TO_ARRAY`                 | scalar   | json               | ✓       |             |
| `JSON_OBJECTAGG`                       | set      | aggregate          | ✓       |             |
| `JSON_OVERLAPS`                        | scalar   | json               | ✓       |             |
| `JSON_PRETTY`                          | scalar   | json               | ✓       |             |
| `JSON_QUERY`                           | scalar   | json               | ✓       |             |
| `JSON_QUOTE`                           | scalar   | json               | ✓       |             |
| `JSON_REMOVE`                          | scalar   | json               | ✓       |             |
| `JSON_REPLACE`                         | scalar   | json               | ✓       |             |
| `JSON_SCHEMA_VALID`                    | scalar   | json               | ✓       |             |
| `JSON_SEARCH`                          | scalar   | json               | ✓       |             |
| `JSON_SET`                             | scalar   | json               | ✓       |             |
| `JSON_TABLE`                           | scalar   | json               | ✓       |             |
| `JSON_TYPE`                            | scalar   | json               | ✓       |             |
| `JSON_UNQUOTE`                         | scalar   | json               | ✓       |             |
| `JSON_VALID`                           | scalar   | json               | ✓       |             |
| `JSON_VALUE`                           | scalar   | json               | ✓       | ✓           |
| `KDF`                                  | scalar   | crypto/compression | ✓       |             |
| `LAST_DAY`                             | scalar   | date/time          | ✓       |             |
| `LAST_INSERT_ID`                       | scalar   | information        | ✓       |             |
| `LAST_VALUE`                           | scalar   | information        | ✓       | ✓           |
| `LASTVAL`                              | scalar   | sequence           | ✓       |             |
| `LCASE`                                | scalar   | string             | ✓       | ✓           |
| `LEAST`                                | scalar   | misc               | ✓       | ✓           |
| `LEFT`                                 | scalar   | string             | ✓       | ✓           |
| `LENGTH`                               | scalar   | string             | ✓       | ✓           |
| `LIKE`                                 | scalar   | string             | ✓       |             |
| `LineFromText`                         | scalar   | geo                | ✓       |             |
| `LineFromWKB`                          | scalar   | geo                | ✓       |             |
| `LINESTRING`                           | scalar   | geo                | ✓       |             |
| `LineStringFromText`                   | scalar   | geo                | ✓       |             |
| `LineStringFromWKB`                    | scalar   | geo                | ✓       |             |
| `LN`                                   | scalar   | math               | ✓       | ✓           |
| `LOAD_FILE`                            | scalar   | string             | ✓       |             |
| `LOCALTIME`                            | scalar   | date/time          | ✓       |             |
| `LOCALTIMESTAMP`                       | scalar   | date/time          | ✓       | ✓           |
| `LOCATE`                               | scalar   | string             | ✓       | ✓           |
| `LOG`                                  | scalar   | math               | ✓       | ✓           |
| `LOG10`                                | scalar   | math               | ✓       | ✓           |
| `LOG2`                                 | scalar   | math               | ✓       | ✓           |
| `LOWER`                                | scalar   | string             | ✓       | ✓           |
| `LPAD`                                 | scalar   | string             | ✓       | ✓           |
| `LTRIM`                                | scalar   | string             | ✓       | ✓           |
| `MAKE_SET`                             | scalar   | string             | ✓       |             |
| `MAKEDATE`                             | scalar   | date/time          | ✓       |             |
| `MAKETIME`                             | scalar   | date/time          | ✓       |             |
| `MASTER_GTID_WAIT`                     | scalar   | misc               | ✓       |             |
| `MASTER_POS_WAIT`                      | scalar   | misc               | ✓       |             |
| `MAX`                                  | set      | aggregate          | ✓       | ✓           |
| `MBRContains`                          | scalar   | geo                | ✓       |             |
| `MBRCoveredBy`                         | scalar   | geo                | ✓       |             |
| `MBRDisjoint`                          | scalar   | geo                | ✓       |             |
| `MBREqual`                             | scalar   | geo                | ✓       |             |
| `MBREquals`                            | scalar   | geo                | ✓       |             |
| `MBRIntersects`                        | scalar   | geo                | ✓       |             |
| `MBROverlaps`                          | scalar   | geo                | ✓       |             |
| `MBRTouches`                           | scalar   | geo                | ✓       |             |
| `MBRWithin`                            | scalar   | geo                | ✓       |             |
| `MD5`                                  | scalar   | crypto/compression | ✓       |             |
| `MEDIAN`                               | analytic | window             | ✓       | ✓           |
| `MICROSECOND`                          | scalar   | date/time          | ✓       |             |
| `MID`                                  | scalar   | string             | ✓       | ✓           |
| `MIN`                                  | set      | aggregate          | ✓       | ✓           |
| `MINUTE`                               | scalar   | date/time          | ✓       | ✓           |
| `MLineFromText`                        | scalar   | geo                | ✓       |             |
| `MLineFromWKB`                         | scalar   | geo                | ✓       |             |
| `MOD`                                  | scalar   | math               | ✓       | ✓           |
| `MONTH`                                | scalar   | date/time          | ✓       | ✓           |
| `MONTHNAME`                            | scalar   | date/time          | ✓       |             |
| `MPointFromText`                       | scalar   | geo                | ✓       |             |
| `MPointFromWKB`                        | scalar   | geo                | ✓       |             |
| `MPolyFromText`                        | scalar   | geo                | ✓       |             |
| `MPolyFromWKB`                         | scalar   | geo                | ✓       |             |
| `MULTILINESTRING`                      | scalar   | geo                | ✓       |             |
| `MultiLineStringFromText`              | scalar   | geo                | ✓       |             |
| `MultiLineStringFromWKB`               | scalar   | geo                | ✓       |             |
| `MULTIPOINT`                           | scalar   | geo                | ✓       |             |
| `MultiPointFromText`                   | scalar   | geo                | ✓       |             |
| `MultiPointFromWKB`                    | scalar   | geo                | ✓       |             |
| `MULTIPOLYGON`                         | scalar   | geo                | ✓       |             |
| `MultiPolygonFromText`                 | scalar   | geo                | ✓       |             |
| `MultiPolygonFromWKB`                  | scalar   | geo                | ✓       |             |
| `NAME_CONST`                           | scalar   | misc               | ✓       |             |
| `NATURAL_SORT_KEY`                     | scalar   | string             | ✓       |             |
| `NULLIF`                               | scalar   | control flow       | ✓       | ✓           |
| `NEXTVAL`                              | scalar   | sequence           | ✓       |             |
| `NOW`                                  | scalar   | date/time          | ✓       | ✓           |
| `NTILE`                                | analytic | window             | ✓       | ✓           |
| `NumGeometries`                        | scalar   | geo                | ✓       |             |
| `NumInteriorRings`                     | scalar   | geo                | ✓       |             |
| `NumPoints`                            | scalar   | geo                | ✓       |             |
| `OCT`                                  | scalar   | math               | ✓       |             |
| `OCTET_LENGTH`                         | scalar   | string             | ✓       | ✓           |
| `OLD_PASSWORD`                         | scalar   | crypto/compression | ✓       |             |
| `ORD`                                  | scalar   | string             | ✓       |             |
| `OVERLAPS`                             | scalar   | geo                | ✓       |             |
| `PASSWORD`                             | scalar   | crypto/compression | ✓       |             |
| `PERCENT_RANK`                         | analytic | window             | ✓       | ✓           |
| `PERCENTILE_CONT`                      | analytic | window             | ✓       | ✓           |
| `PERCENTILE_DISC`                      | analytic | window             | ✓       | ✓           |
| `PERIOD_ADD`                           | scalar   | date/time          | ✓       |             |
| `PERIOD_DIFF`                          | scalar   | date/time          | ✓       |             |
| `PI`                                   | scalar   | math               | ✓       | ✓           |
| `POINT`                                | scalar   | geo                | ✓       |             |
| `PointFromText`                        | scalar   | geo                | ✓       |             |
| `PointFromWKB`                         | scalar   | geo                | ✓       |             |
| `PointN`                               | scalar   | geo                | ✓       |             |
| `PointOnSurface`                       | scalar   | geo                | ✓       |             |
| `POLYGON`                              | scalar   | geo                | ✓       |             |
| `PolyFromText`                         | scalar   | geo                | ✓       |             |
| `PolyFromWKB`                          | scalar   | geo                | ✓       |             |
| `PolygonFromText`                      | scalar   | geo                | ✓       |             |
| `PolygonFromWKB`                       | scalar   | geo                | ✓       |             |
| `POSITION`                             | scalar   | string             | ✓       | ✓           |
| `POW`                                  | scalar   | math               | ✓       |             |
| `POWER`                                | scalar   | math               | ✓       | ✓           |
| `QUARTER`                              | scalar   | date/time          | ✓       |             |
| `QUOTE`                                | scalar   | string             | ✓       | +           |
| `RADIANS`                              | scalar   | math               | ✓       | ✓           |
| `RAND`                                 | scalar   | math               | ✓       |             |
| `RANK`                                 | analytic | window             | ✓       | ✓           |
| `REGEXP`                               | scalar   | string             | ✓       |             |
| `REGEXP_INSTR`                         | scalar   | string             | ✓       | ✓           |
| `REGEXP_REPLACE`                       | scalar   | string             | ✓       | ✓           |
| `REGEXP_SUBSTR`                        | scalar   | string             | ✓       | ✓           |
| `RELEASE_LOCK`                         | scalar   | misc               | ✓       |             |
| `REVERSE`                              | scalar   | string             | ✓       | ✓           |
| `RIGHT`                                | scalar   | string             | ✓       | ✓           |
| `RLIKE`                                | scalar   | string             | ✓       |             |
| `RPAD`                                 | scalar   | string             | ✓       | ✓           |
| `ROUND`                                | scalar   | math               | ✓       |             |
| `ROW_COUNT`                            | scalar   | information        | ✓       |             |
| `ROW_NUMBER`                           | analytic | window             | ✓       | ✓           |
| `RTRIM`                                | scalar   | string             | ✓       | ✓           |
| `SCHEMA`                               | scalar   | information        | ✓       |             |
| `SECOND`                               | scalar   | date/time          | ✓       | ✓           |
| `SEC_TO_TIME`                          | scalar   | date/time          | ✓       |             |
| `SETVAL`                               | scalar   | sequence           | ✓       |             |
| `SESSION_USER`                         | scalar   | information        | ✓       |             |
| `sha`                                  | scalar   | crypto/compression | ✓       |             |
| `SHA1`                                 | scalar   | crypto/compression | ✓       |             |
| `SHA2`                                 | scalar   | crypto/compression | ✓       |             |
| `SIGN`                                 | scalar   | math               | ✓       | ✓           |
| `SIN`                                  | scalar   | math               | ✓       | ✓           |
| `SLEEP`                                | scalar   | misc               | ✓       |             |
| `SOUNDEX`                              | scalar   | string             | ✓       | ✓           |
| `SPACE`                                | scalar   | string             | ✓       | ✓           |
| `SPIDER_BG_DIRECT_SQL`                 | scalar   | storage engine     | ✓       |             |
| `SPIDER_COPY_TABLES`                   | scalar   | storage engine     | ✓       |             |
| `SPIDER_DIRECT_SQL`                    | scalar   | storage engine     | ✓       |             |
| `SPIDER_FLUSH_TABLE_MON_CACHE`         | scalar   | storage engine     | ✓       |             |
| `SQRT`                                 | scalar   | math               | ✓       | ✓           |
| `SRID`                                 | scalar   | geo                | ✓       |             |
| `ST_AREA`                              | scalar   | geo                | ✓       |             |
| `ST_AsBinary`                          | scalar   | geo                | ✓       |             |
| `ST_AsGeoJson`                         | scalar   | geo                | ✓       |             |
| `ST_AsText`                            | scalar   | geo                | ✓       |             |
| `ST_AsWKB`                             | scalar   | geo                | ✓       |             |
| `ST_ASWKT`                             | scalar   | geo                | ✓       |             |
| `ST_BOUNDARY`                          | scalar   | geo                | ✓       |             |
| `ST_BUFFER`                            | scalar   | geo                | ✓       |             |
| `ST_CENTROID`                          | scalar   | geo                | ✓       |             |
| `ST_Collect`                           | scalar   | geo                | ✓       |             |
| `ST_CONTAINS`                          | scalar   | geo                | ✓       |             |
| `ST_CONVEXHULL`                        | scalar   | geo                | ✓       |             |
| `ST_CROSSES`                           | scalar   | geo                | ✓       |             |
| `ST_DIFFERENCE`                        | scalar   | geo                | ✓       |             |
| `ST_DIMENSION`                         | scalar   | geo                | ✓       |             |
| `ST_DISJOINT`                          | scalar   | geo                | ✓       |             |
| `ST_DISTANCE`                          | scalar   | geo                | ✓       |             |
| `ST_DISTANCE_SPHERE`                   | scalar   | geo                | ✓       |             |
| `ST_ENDPOINT`                          | scalar   | geo                | ✓       |             |
| `ST_ENVELOPE`                          | scalar   | geo                | ✓       |             |
| `ST_EQUALS`                            | scalar   | geo                | ✓       |             |
| `ST_ExteriorRing`                      | scalar   | geo                | ✓       |             |
| `ST_GeoHash`                           | scalar   | geo                | ✓       |             |
| `ST_GeomCollFromText`                  | scalar   | geo                | ✓       |             |
| `ST_GeomCollFromWKB`                   | scalar   | geo                | ✓       |             |
| `ST_GeometryCollectionFromText`        | scalar   | geo                | ✓       |             |
| `ST_GeometryCollectionFromWKB`         | scalar   | geo                | ✓       |             |
| `ST_GeometryFromText`                  | scalar   | geo                | ✓       |             |
| `ST_GeometryFromWKB`                   | scalar   | geo                | ✓       |             |
| `ST_GEOMETRYN`                         | scalar   | geo                | ✓       |             |
| `ST_GEOMETRYTYPE`                      | scalar   | geo                | ✓       |             |
| `ST_GeomFromGeoJSON`                   | scalar   | geo                | ✓       |             |
| `ST_GeomFromText`                      | scalar   | geo                | ✓       |             |
| `ST_GeomFromWKB`                       | scalar   | geo                | ✓       |             |
| `ST_InteriorRingN`                     | scalar   | geo                | ✓       |             |
| `ST_INTERSECTION`                      | scalar   | geo                | ✓       |             |
| `ST_INTERSECTS`                        | scalar   | geo                | ✓       |             |
| `ST_ISCLOSED`                          | scalar   | geo                | ✓       |             |
| `ST_ISEMPTY`                           | scalar   | geo                | ✓       |             |
| `ST_IsRing`                            | scalar   | geo                | ✓       |             |
| `ST_IsSimple`                          | scalar   | geo                | ✓       |             |
| `ST_IsValid`                           | scalar   | geo                | ✓       |             |
| `ST_LatFromGeoHash`                    | scalar   | geo                | ✓       |             |
| `ST_LongFromGeoHash`                   | scalar   | geo                | ✓       |             |
| `ST_LENGTH`                            | scalar   | geo                | ✓       |             |
| `ST_LineFromText`                      | scalar   | geo                | ✓       |             |
| `ST_LineFromWKB`                       | scalar   | geo                | ✓       |             |
| `ST_LineStringFromText`                | scalar   | geo                | ✓       |             |
| `ST_LineStringFromWKB`                 | scalar   | geo                | ✓       |             |
| `ST_MLineFromText`                     | scalar   | geo                | ✓       |             |
| `ST_MLineFromWKB`                      | scalar   | geo                | ✓       |             |
| `ST_MPointFromText`                    | scalar   | geo                | ✓       |             |
| `ST_MPointFromWKB`                     | scalar   | geo                | ✓       |             |
| `ST_MPolyFromText`                     | scalar   | geo                | ✓       |             |
| `ST_MPolyFromWKB`                      | scalar   | geo                | ✓       |             |
| `ST_MultiLineStringFromText`           | scalar   | geo                | ✓       |             |
| `ST_MultiLineStringFromWKB`            | scalar   | geo                | ✓       |             |
| `ST_MultiPointFromText`                | scalar   | geo                | ✓       |             |
| `ST_MultiPolygonFromText`              | scalar   | geo                | ✓       |             |
| `ST_MultiPolygonFromWKB`               | scalar   | geo                | ✓       |             |
| `ST_MultiPointFromWKB`                 | scalar   | geo                | ✓       |             |
| `ST_NUMGEOMETRIES`                     | scalar   | geo                | ✓       |             |
| `ST_NumInteriorRings`                  | scalar   | geo                | ✓       |             |
| `ST_NUMPOINTS`                         | scalar   | geo                | ✓       |             |
| `ST_OVERLAPS`                          | scalar   | geo                | ✓       |             |
| `ST_PointFromGeoHash`                  | scalar   | geo                | ✓       |             |
| `ST_PointFromText`                     | scalar   | geo                | ✓       |             |
| `ST_PointFromWKB`                      | scalar   | geo                | ✓       |             |
| `ST_POINTN`                            | scalar   | geo                | ✓       |             |
| `ST_POINTONSURFACE`                    | scalar   | geo                | ✓       |             |
| `ST_PolyFromText`                      | scalar   | geo                | ✓       |             |
| `ST_PolyFromWKB`                       | scalar   | geo                | ✓       |             |
| `ST_PolygonFromText`                   | scalar   | geo                | ✓       |             |
| `ST_PolygonFromWKB`                    | scalar   | geo                | ✓       |             |
| `ST_RELATE`                            | scalar   | geo                | ✓       |             |
| `ST_Simplify`                          | scalar   | geo                | ✓       |             |
| `ST_SRID`                              | scalar   | geo                | ✓       |             |
| `ST_STARTPOINT`                        | scalar   | geo                | ✓       |             |
| `ST_SYMDIFFERENCE`                     | scalar   | geo                | ✓       |             |
| `ST_TOUCHES`                           | scalar   | geo                | ✓       |             |
| `ST_UNION`                             | scalar   | geo                | ✓       |             |
| `ST_Validate`                          | scalar   | geo                | ✓       |             |
| `ST_WITHIN`                            | scalar   | geo                | ✓       |             |
| `ST_X`                                 | scalar   | geo                | ✓       |             |
| `ST_Y`                                 | scalar   | geo                | ✓       |             |
| `STARTPOINT`                           | scalar   | geo                | ✓       |             |
| `STD`                                  | set      | aggregate          | ✓       |             |
| `STDDEV`                               | set      | aggregate          | ✓       | ✓           |
| `STDDEV_POP`                           | set      | aggregate          | ✓       | ✓           |
| `STDDEV_SAMP`                          | set      | aggregate          | ✓       | ✓           |
| `STR_TO_DATE`                          | scalar   | date/time          | ✓       |             |
| `STRCMP`                               | scalar   | string             | ✓       |             |
| `SUBDATE`                              | scalar   | date/time          | ✓       |             |
| `SUBSTR`                               | scalar   | string             | ✓       |             |
| `SUBSTRING`                            | scalar   | string             | ✓       |             |
| `SUBSTRING_INDEX`                      | scalar   | string             | ✓       |             |
| `SUBTIME`                              | scalar   | date/time          | ✓       |             |
| `SUM`                                  | set      | aggregate          | ✓       | ✓           |
| `SYS.EXTRACT_SCHEMA_FROM_FILE_NAME`    | scalar   | system             | ✓       |             |
| `SYS.EXTRACT_TABLE_FROM_FILE_NAME`     | scalar   | system             | ✓       |             |
| `SYS.FORMAT_BYTES`                     | scalar   | system             | ✓       |             |
| `SYS.FORMAT_PATH`                      | scalar   | system             | ✓       |             |
| `SYS.FORMAT_STATEMENT`                 | scalar   | system             | ✓       |             |
| `SYS.FORMAT_TIME`                      | scalar   | system             | ✓       |             |
| `SYS.LIST_ADD`                         | scalar   | system             | ✓       |             |
| `SYS.LIST_DROP`                        | scalar   | system             | ✓       |             |
| `SYS.PS_IS_ACCOUNT_ENABLED`            | scalar   | system             | ✓       |             |
| `SYS.PS_IS_CONSUMER_ENABLED`           | scalar   | system             | ✓       |             |
| `SYS.PS_IS_INSTRUMENT_DEFAULT_ENABLED` | scalar   | system             | ✓       |             |
| `SYS.PS_IS_INSTRUMENT_DEFAULT_TIMED`   | scalar   | system             | ✓       |             |
| `SYS.PS_IS_THREAD_INSTRUMENTED`        | scalar   | system             | ✓       |             |
| `SYS.PS_THREAD_ACCOUNT`                | scalar   | system             | ✓       |             |
| `SYS.PS_THREAD_ID`                     | scalar   | system             | ✓       |             |
| `SYS.PS_THREAD_STACK`                  | scalar   | system             | ✓       |             |
| `SYS.PS_THREAD_TRX_INFO`               | scalar   | system             | ✓       |             |
| `SYS.QUOTE_IDENTIFIER`                 | scalar   | system             | ✓       |             |
| `SYS.SYS_GET_CONFIG`                   | scalar   | system             | ✓       |             |
| `SYS.VERSION_MAJOR`                    | scalar   | system             | ✓       |             |
| `SYS.VERSION_MINOR`                    | scalar   | system             | ✓       |             |
| `SYS.VERSION_PATCH`                    | scalar   | system             | ✓       |             |
| `SYS_GUID`                             | scalar   | misc               | ✓       | ✓           |
| `SYSDATE`                              | scalar   | date/time          | ✓       | ✓           |
| `SYSTEM_USER`                          | scalar   | information        | ✓       |             |
| `TAN`                                  | scalar   | math               | ✓       | ✓           |
| `TIMEDIFF`                             | scalar   | date/time          | ✓       |             |
| `TIMESTAMPADD`                         | scalar   | date/time          | ✓       |             |
| `TIMESTAMPDIFF`                        | scalar   | date/time          | ✓       |             |
| `TIME_FORMAT`                          | scalar   | date/time          | ✓       |             |
| `TIME_TO_SEC`                          | scalar   | date/time          | ✓       |             |
| `TO_BASE64`                            | scalar   | string             | ✓       |             |
| `TO_CHAR`                              | scalar   | string             | ✓       |             |
| `TO_DAYS`                              | scalar   | date/time          | ✓       |             |
| `TO_NUMBER`                            | scalar   | math               | ✓       | ✓           |
| `TO_SECONDS`                           | scalar   | date/time          | ✓       |             |
| `TOUCHES`                              | scalar   | geo                | ✓       |             |
| `TRIM`                                 | scalar   | string             | ✓       | ✓           |
| `TRUNC`                                | scalar   | date/time          | ✓       |             |
| `TRUNCATE`                             | scalar   | math               | ✓       |             |
| `UCASE`                                | scalar   | string             | ✓       | ✓           |
| `UNHEX`                                | scalar   | string             | ✓       |             |
| `UNCOMPRESS`                           | scalar   | crypto/compression | ✓       |             |
| `UNCOMPRESSED_LENGTH`                  | scalar   | crypto/compression | ✓       |             |
| `UNIX_TIMESTAMP`                       | scalar   | date/time          | ✓       |             |
| `UPDATEXML`                            | scalar   | string             | ✓       |             |
| `UPPER`                                | scalar   | string             | ✓       | ✓           |
| `USER`                                 | scalar   | information        | ✓       | ✓           |
| `UTC_DATE`                             | scalar   | date/time          | ✓       |             |
| `UTC_TIME`                             | scalar   | date/time          | ✓       |             |
| `UTC_TIMESTAMP`                        | scalar   | date/time          | ✓       |             |
| `UUID`                                 | scalar   | misc               | ✓       |             |
| `UUIDv4`                               | scalar   | misc               | ✓       |             |
| `UUIDv7`                               | scalar   | misc               | ✓       |             |
| `UUID_SHORT`                           | scalar   | misc               | ✓       |             |
| `VAR_POP`                              | set      | aggregate          | ✓       | ✓           |
| `VAR_SAMP`                             | set      | aggregate          | ✓       | ✓           |
| `VARIANCE`                             | set      | aggregate          | ✓       | ✓           |
| `VEC_DISTANCE`                         | scalar   | vector             | ✓       |             |
| `VEC_DISTANCE_COSINE`                  | scalar   | vector             | ✓       |             |
| `VEC_DISTANCE_EUCLIDEAN`               | scalar   | vector             | ✓       |             |
| `VEC_FromText`                         | scalar   | vector             | ✓       |             |
| `VEC_ToText`                           | scalar   | vector             | ✓       |             |
| `VERSION`                              | scalar   | information        | ✓       |             |
| `WEEK`                                 | scalar   | date/time          | ✓       | ✓           |
| `WEEKDAY`                              | scalar   | date/time          | ✓       |             |
| `WEEKOFYEAR`                           | scalar   | date/time          | ✓       |             |
| `WEIGHT_STRING`                        | scalar   | string             | ✓       |             |
| `WITHIN`                               | scalar   | geo                | ✓       |             |
| `WSREP_LAST_SEEN_GTID`                 | scalar   | replication        | ✓       |             |
| `WSREP_LAST_WRITTEN_GTID`              | scalar   | replication        | ✓       |             |
| `WSREP_SYNC_WAIT_UPTO_GTID`            | scalar   | replication        | ✓       |             |
| `X`                                    | scalar   | geo                | ✓       |             |
| `Y`                                    | scalar   | geo                | ✓       |             |
| `YEAR`                                 | scalar   | date/time          | ✓       | ✓           |
| `YEARWEEK`                             | scalar   | date/time          | ✓       |             |

Legend: ✓ built-in, + added by `more-functions` 