from loguru import logger
import psycopg2
from psycopg2.extras import execute_values


class PSQLConnect:
    """PostgreSQL Database class."""

    def __init__(self, host='localhost', username='postgres', password='postgres', port='5432', dbname='postgres'):
        self.conn = None
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.dbname = dbname

    def __str__(self):
        return f'{self.host} {self.username} {self.password} {self.port} {self.dbname}'

    def __del__(self):
        self.close_connection()

    def connect(self):
        """Connect to a Postgres database."""
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    user=self.username,
                    password=self.password,
                    port=self.port,
                    dbname=self.dbname
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

    def check_table_exists(self, table_name):
        """Check if a table exists."""
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT EXISTS (SELECT FROM pg_tables WHERE schemaname = 'public' AND tablename = '{table_name}');")
        result = cursor.fetchone()
        cursor.close()
        return result

    def create_table(self, table_name, columns):
        """Create a table."""
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});")
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

    def insert_table(self, table_name, columns):
        """Insert a table."""
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ();")
        self.conn.commit()
        cursor.close()

    def insert_table_with_params(self, table_name, columns, params):
        """Insert a table with parameters."""
        self.open_connection()
        cursor = self.conn.cursor()
        execute_values(cursor, f"INSERT INTO {table_name} ({columns}) VALUES %s", params)
        self.conn.commit()
        cursor.close()

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


