from loguru import logger
import psycopg2
from psycopg2.extras import execute_values


class PSQLConnect:
    """PostgreSQL Database class."""

    def __init__(self, host='localhost', port='5432', dbname='postgres', schema='public', username='postgres',
                 password='postgres'):
        self.conn = None
        self.host = host
        self.port = port
        self.dbname = dbname
        self.schema = schema
        self.username = username
        self.password = password

    def __str__(self):
        return f'{self.host} {self.port} {self.dbname} {self.username} {self.password}'

    def __del__(self):
        self.close_connection()

    def connect(self):
        """Connect to a Postgres database."""
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    port=self.port,
                    dbname=self.dbname,
                    user=self.username,
                    password=self.password,
                    options=f"-c search_path={self.schema}"
                )
            except psycopg2.DatabaseError as e:
                logger.error(e)
                raise e
            finally:
                logger.info('Connection opened successfully.')

    def open_connection(self):
        if self.conn is None:
            self.connect()

    def close_connection(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
            logger.info('Connection closed successfully.')

    def check_database_exists(self, dbname):
        """Check if a database exists."""
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT EXISTS (SELECT FROM pg_database WHERE datname = '{dbname}');")
        result = cursor.fetchone()
        cursor.close()
        return result

    def create_database(self, dbname):
        """Create a database if it doesn't exist."""
        self.open_connection()
        cursor = self.conn.cursor()
        if not self.check_database_exists(dbname):
            cursor.execute(f"CREATE DATABASE {dbname};")
            self.conn.commit()
        cursor.close()

    def drop_database(self, dbname):
        """Drop a database if it exists."""
        self.open_connection()
        cursor = self.conn.cursor()
        if not self.check_database_exists(dbname):
            cursor.execute(f"DROP DATABASE IF EXISTS {dbname};")
            self.conn.commit()
        cursor.close()

    def create_schema(self, schema_name):
        """Create a schema if it doesn't exist."""
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema_name};")
        self.conn.commit()
        cursor.close()

    def check_schema_exists(self, schema_name):
        """Check if a schema exists."""
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT EXISTS (SELECT FROM information_schema.schemata WHERE schema_name = '{schema_name}');")
        result = cursor.fetchone()
        cursor.close()
        return result

    def drop_schema(self, schema_name):
        """Drop a schema if it exists."""
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(f"DROP SCHEMA IF EXISTS {schema_name} CASCADE;")
        self.conn.commit()
        cursor.close()

    def create_table(self, table_name, columns):
        """Create a table."""
        rows = ''
        for column in columns:
            rows += column['name'] + ' ' + column['type'] + ', '

        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({rows[:-2]});")
        self.conn.commit()
        cursor.close()

    def create_table_with_params(self, table_name, columns, params):
        """Create a table with parameters."""
        self.open_connection()
        cursor = self.conn.cursor()
        execute_values(cursor, f"CREATE TABLE IF NOT EXISTS {table_name} ({columns}) VALUES %s", params)
        self.conn.commit()
        cursor.close()

    def insert_table(self, table_name, columns, values):
        """Insert a table."""
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values});")
        self.conn.commit()
        cursor.close()

    def insert_table_with_params(self, table_name, columns, params):
        """Insert a table with parameters."""
        self.open_connection()
        cursor = self.conn.cursor()
        execute_values(cursor, f"INSERT INTO {table_name} ({columns}) VALUES %s", params)
        self.conn.commit()
        cursor.close()

    def drop_table(self, table_name):
        """Drop a table."""
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
        self.conn.commit()
        cursor.close()

    def truncate_table(self, table_name):
        """Truncate a table."""
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(f"TRUNCATE TABLE {table_name};")
        self.conn.commit()
        cursor.close()

    def read_table(self, table_name):
        """Read a table."""
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name};")
        result = cursor.fetchall()
        cursor.close()
        return result

    def execute_query(self, query):
        """Execute a query."""
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(query)
        cursor.close()

    def execute_read_query(self, query):
        """Execute a read query."""
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def execute_write_query(self, query):
        """Execute a write query."""
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        cursor.close()

    def execute_write_query_with_params(self, query, params):
        """Execute a write query with parameters."""
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        cursor.close()
