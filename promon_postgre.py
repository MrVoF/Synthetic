import psycopg2
from psycopg2.extras import execute_values
from loguru import logger


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
        return f'{self.host} {self.port} {self.dbname} {self.schema} {self.username} {self.password}'

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
            else:
                logger.success("Подключение к серверу PostgreSQL прошло успешно.")

    def open_connection(self):
        if self.conn is None:
            self.connect()

    def close_connection(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
            logger.success("Подключение к серверу PostgreSQL закрыто.")

    def check_database_exists(self, dbname):
        """Check if a database exists."""
        self.open_connection()
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"SELECT EXISTS (SELECT FROM pg_database WHERE datname = '{dbname}');")
        except psycopg2.DatabaseError as e:
            logger.error(e)
        else:
            logger.success("База данных существует.")

        result = cursor.fetchone()
        cursor.close()
        return result

    def create_database(self, dbname):
        """Create a database if it doesn't exist."""
        self.open_connection()
        cursor = self.conn.cursor()
        if not self.check_database_exists(dbname):
            try:
                cursor.execute(f"CREATE DATABASE '{dbname}';")
            except psycopg2.DatabaseError as e:
                logger.error(e)
            else:
                logger.success(f"База данных '{dbname}' создана.")

            self.conn.commit()
        cursor.close()

    def drop_database(self, dbname):
        """Drop a database if it exists."""
        self.open_connection()
        cursor = self.conn.cursor()
        if not self.check_database_exists(dbname):
            try:
                cursor.execute(f"DROP DATABASE IF EXISTS '{dbname}';")
            except psycopg2.DatabaseError as e:
                logger.error(e)
            else:
                logger.success(f"База данных '{dbname}' удалена.")

            self.conn.commit()
        cursor.close()

    def create_schema(self, schema_name):
        """Create a schema if it doesn't exist."""
        self.open_connection()
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"CREATE SCHEMA IF NOT EXISTS '{schema_name}';")
        except psycopg2.DatabaseError as e:
            logger.error(e)
        else:
            logger.success(f"Схема '{schema_name}' создана.")

        self.conn.commit()
        cursor.close()

    def check_schema_exists(self, schema_name):
        """Check if a schema exists."""
        self.open_connection()
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                f"SELECT EXISTS (SELECT FROM information_schema.schemata WHERE schema_name = '{schema_name}');")
        except psycopg2.DatabaseError as e:
            logger.error(e)
        else:
            logger.success("Схема существует.")

        result = cursor.fetchone()
        cursor.close()
        return result

    def drop_schema(self, schema_name):
        """Drop a schema if it exists."""
        self.open_connection()
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"DROP SCHEMA IF EXISTS '{schema_name}' CASCADE;")
        except psycopg2.DatabaseError as e:
            logger.error(e)
        else:
            logger.success(f"Схема '{schema_name}' удалена.")

        self.conn.commit()
        cursor.close()

    def create_table(self, table_name, columns):
        """Create a table."""
        rows = ''
        for column in columns:
            rows += '"' + column['name'] + '" ' + column['type'] + ', '

        rows = rows[:-2]
        self.open_connection()
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"CREATE TABLE IF NOT EXISTS \"{table_name}\" ({rows});")
        except psycopg2.errors.SyntaxError as e:
            logger.error("Ошибка в синтаксисе запроса, проверьте корректность типов в yml файле.")
        else:
            logger.success("Таблица создана успешно.")
        self.conn.commit()
        cursor.close()

    def create_table_with_params(self, table_name, columns, params):
        """Create a table with parameters."""
        self.open_connection()
        cursor = self.conn.cursor()
        try:
            execute_values(cursor, f"CREATE TABLE IF NOT EXISTS \"{table_name}\" ({columns}) VALUES %s", params)
        except psycopg2.errors.SyntaxError as e:
            logger.error("Ошибка в синтаксисе запроса, проверьте корректность типов в yml файле.")
        else:
            logger.success(f"Таблица \"{table_name}\" создана успешно.")

        self.conn.commit()
        cursor.close()

    def insert_table(self, table_name, columns, values):
        """Insert a table."""
        self.open_connection()
        cursor = self.conn.cursor()
        query = f"INSERT INTO \"{table_name}\" ({columns}) VALUES ({values});"
        try:
            cursor.execute(query)
        except psycopg2.errors.SyntaxError as e:
            logger.error(e)
        else:
            logger.opt(colors=True).success("Запись '<blue>{query}</blue>' добавлена.", query=query)

        self.conn.commit()
        cursor.close()

    def insert_table_with_params(self, table_name, columns, params):
        """Insert a table with parameters."""
        self.open_connection()
        cursor = self.conn.cursor()
        try:
            execute_values(cursor, f"INSERT INTO \"{table_name}\" ({columns}) VALUES %s", params)
        except psycopg2.errors.SyntaxError as e:
            logger.error(e)
        else:
            logger.success("Запись добавлена.")

        self.conn.commit()
        cursor.close()

    def drop_table(self, table_name):
        """Drop a table."""
        self.open_connection()
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"DROP TABLE IF EXISTS \"{table_name}\";")
        except psycopg2.DatabaseError as e:
            logger.error(e)
        else:
            logger.success(f"Таблица \"{table_name}\" удалена.")

        self.conn.commit()
        cursor.close()

    def truncate_table(self, table_name):
        """Truncate a table."""
        self.open_connection()
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"TRUNCATE TABLE \"{table_name}\";")
        except psycopg2.DatabaseError as e:
            logger.error(e)
        else:
            logger.success(f"Таблица \"{table_name}\" очищена.")

        self.conn.commit()
        cursor.close()

    def read_table(self, table_name):
        """Read a table."""
        self.open_connection()
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"SELECT * FROM \"{table_name}\";")
        except psycopg2.DatabaseError as e:
            logger.error(e)
        else:
            logger.success(f"Таблица \"{table_name}\" считана.")

        result = cursor.fetchall()
        cursor.close()
        return result

    def execute_query(self, query):
        """Execute a query."""
        self.open_connection()
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
        except psycopg2.DatabaseError as e:
            logger.error(e)
        else:
            logger.success("Запрос выполнен.")

        cursor.close()
