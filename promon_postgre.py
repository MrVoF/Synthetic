from loguru import logger
import psycopg2


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

    def executemany_write_query_with_params(self, query, params):
        """Execute many a write query with parameters."""
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.executemany(query, params)
        self.conn.commit()
        cursor.close()

    def execute_query_with_params(self, query, params):
        """Execute a query with parameters."""
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        cursor.close()

    def execute_query_with_params_and_fetchone(self, query, params):
        """Execute a query with parameters and fetch one."""
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        return result

    def execute_query_with_params_and_fetchall(self, query, params):
        """Execute a query with parameters and fetch all."""
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result

    def execute_query_with_params_and_fetchmany(self, query, params):
        """Execute a query with parameters and fetch many."""
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchmany()
        cursor.close()
        return result
