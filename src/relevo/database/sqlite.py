import sqlite3

def __dict_factory(cursor, row):
  d = {}
  for idx, col in enumerate(cursor.description):
    d[col[0]] = row[idx]
  return d


class SQLiteNotConnectedException(Exception):
  def __init__(self):
    super().__init__("SQLite connection not estabilished")


class SQLite:
  connection: sqlite3.Connection | None = None

  @staticmethod
  def connect(path: str) -> None:
    SQLite.connection = sqlite3.connect(database=path, autocommit=True)
    SQLite.connection.row_factory = __dict_factory

  def query(self, sql: str, params: tuple[Any, ...] = ()) -> list[dict]:
    """Execute a query and return the results.

    Args:
        sql: The SQL query string.
        params: Query parameters tuple.

    Returns:
        A list of sqlite3.Row objects.
    """
    if not SQLite.connection:
      raise SQLiteNotConnectedException()

    cursor = SQLite.connection.execute(sql, params)
    return cursor.fetchall()
