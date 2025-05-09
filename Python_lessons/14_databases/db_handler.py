from mysql import connector
import psycopg2
import sqlite3
from psycopg2.extensions import cursor as Psycopg2Cursor


class DataBaseHandler:

    def __init__(self, config):
        self.db_name = config.db_name
        self.config = config
        self.connection = None
        self.cursor: Psycopg2Cursor = None

    def _get_connection_params(self):
        if self.db_name == "mysql" or self.db_name == "postgres":
            return {
                "host": self.config.server,
                "database": self.config.database,
                "user": self.config.username,
                "password": self.config.password,
                "port": self.config.port,
            }
        elif self.db_name == "sqlite":
            return {"database": self.config.database}
        else:
            raise ValueError("Поддерживаются только MySql, Postgres и Sqlite")

    def connect(self):
        params = self._get_connection_params()
        if self.db_name == "mysql":
            self.connection = connector.connect(**params)
        elif self.db_name == "postgres":
            self.connection = psycopg2.connect(**params)
        elif self.db_name == "sqlite":
            self.connection = sqlite3.connect(params["database"])
        self.cursor = self.connection.cursor()

    def get_all_users(self, fetchone=False):
        self.cursor.execute("SELECT * FROM users")
        if fetchone:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()

    def add_user(self, name, age):
        self.cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        self.connection.commit()

    def delete_user(self, id):
        self.cursor.execute("DELETE FROM users WHERE id = ?", (id,))
        self.connection.commit()

    def select_all(self, table):
        self.cursor.execute(f"SELECT * FROM {table}")
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()