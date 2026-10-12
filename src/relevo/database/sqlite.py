import sqlite3
from typing import Any

class SQLiteNotConnectedException(Exception):
  def __init__(self):
    super().__init__("SQLite connection not estabilished")


class SQLite:
  connection: sqlite3.Connection | None = None

  @staticmethod
  def connect(path: str) -> None:
    SQLite.connection = sqlite3.connect(database=path, autocommit=True, check_same_thread=False)
    SQLite.connection.row_factory = SQLite.__dict_factory

  @staticmethod
  def __dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
      d[col[0]] = row[idx]
    return d

  def query(self, sql: str, params: dict[str, Any] | tuple = ()) -> list[dict]:
    """Execute a query and return the results.

    Args:
        sql: The SQL query string.
        params: Query parameters as dict or tuple.

    Returns:
        A list of sqlite3.Row objects.
    """
    if not SQLite.connection:
      raise SQLiteNotConnectedException()

    cursor = SQLite.connection.execute(sql, params)
    return cursor.fetchall()
