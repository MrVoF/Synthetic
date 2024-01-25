import psycopg2
from loguru import logger


class PSQLConnect:
    """Класс подключения к серверу PostgreSQL."""

    def __init__(self, host='localhost', port='5432', database='postgres', schema='public', username='postgres',
                 password='postgres'):
        self.conn = None
        self.host = host
        self.port = port
        self.database = database
        self.schema = schema
        self.username = username
        self.password = password

    def __str__(self):
        return f"{self.host} {self.port} {self.database} {self.schema} {self.username} {self.password}"

    def __del__(self):
        self.close_connection()

    def connect(self):
        """Подключение к серверу PostgreSQL."""
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    port=self.port,
                    database=self.database,
                    user=self.username,
                    password=self.password,
                    options=f"-c search_path={self.schema}"
                )
            except psycopg2.DatabaseError as e:
                logger.error(e)
                raise e
            else:
                logger.opt(colors=True).success("Подключение к серверу \"<blue>{host}</blue>\" установлено.",
                                                host=self.host)

    def open_connection(self):
        if self.conn is None:
            self.connect()

    def close_connection(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
            logger.opt(colors=True).success("Подключение к серверу \"<blue>{host}</blue>\" закрыто.", host=self.host)

    def check_database_exists(self, database):
        """Проверка существует ли база данных"""
        self.open_connection()
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"SELECT EXISTS (SELECT FROM pg_database WHERE datname = \"{database}\");")
        except psycopg2.DatabaseError as e:
            logger.error(e)
        else:
            logger.opt(colors=True).success("База данных \"<blue>{database}</blue>\" существует.", database=database)

        result = cursor.fetchone()
        cursor.close()
        return result

    def create_database(self, database):
        """Создание базы данных."""
        self.open_connection()
        cursor = self.conn.cursor()
        if not self.check_database_exists(database):
            try:
                cursor.execute(f"CREATE DATABASE \"{database}\";")
            except psycopg2.DatabaseError as e:
                logger.error(e)
            else:
                logger.opt(colors=True).success("База данных \"<blue>{database}</blue>\" создана.", database=database)

            self.conn.commit()
        cursor.close()

    def drop_database(self, database):
        """Удаление базы данных."""
        self.open_connection()
        cursor = self.conn.cursor()
        if not self.check_database_exists(database):
            try:
                cursor.execute(f"DROP DATABASE IF EXISTS \"{database}\";")
            except psycopg2.DatabaseError as e:
                logger.error(e)
            else:
                logger.opt(colors=True).success("База данных \"<blue>{database}</blue>\" удалена.", database=database)

            self.conn.commit()
        cursor.close()

    def create_schema(self, schema):
        """Создание схемы."""
        self.open_connection()
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"CREATE SCHEMA IF NOT EXISTS \"{schema}\";")
        except psycopg2.DatabaseError as e:
            logger.error(e)
        else:
            logger.opt(colors=True).success("Схема \"<blue>{schema}</blue>\" создана.", schema=schema)

        self.conn.commit()
        cursor.close()

    def check_schema_exists(self, schema):
        """Проверка существует ли схема."""
        self.open_connection()
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                f"SELECT EXISTS (SELECT FROM information_schema.schemata WHERE schema = \"{schema}\");")
        except psycopg2.DatabaseError as e:
            logger.error(e)
        else:
            logger.opt(colors=True).success("Схема \"<blue>{schema}</blue>\" существует.", schema=schema)

        result = cursor.fetchone()
        cursor.close()
        return result

    def drop_schema(self, schema):
        """Удаление схемы."""
        self.open_connection()
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"DROP SCHEMA IF EXISTS \"{schema}\" CASCADE;")
        except psycopg2.DatabaseError as e:
            logger.error(e)
        else:
            logger.opt(colors=True).success("Схема \"<blue>{schema}</blue>\" удалена.", schema=schema)

        self.conn.commit()
        cursor.close()

    def create_table(self, table, columns):
        """Создание таблицы."""
        rows = ''
        for column in columns:
            rows += '"' + column['name'] + '" ' + column['type'] + ', '

        rows = rows[:-2]
        self.open_connection()
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"CREATE TABLE IF NOT EXISTS \"{table}\" ({rows});")
        except psycopg2.errors.SyntaxError as e:
            logger.error("Ошибка в синтаксисе запроса, проверьте корректность типов в yml файле.")
        else:
            logger.opt(colors=True).success("Таблица \"<blue>{table}</blue>\" создана успешно.", table=table)

        self.conn.commit()
        cursor.close()

    def insert_table(self, table, columns, values):
        """Запись в таблицу."""
        self.open_connection()
        cursor = self.conn.cursor()
        query = f"INSERT INTO \"{table}\" ({columns}) VALUES ({values});"
        try:
            cursor.execute(query)
        except psycopg2.errors.SyntaxError as e:
            logger.error(e)
        else:
            logger.opt(colors=True).success("Запись \"<blue>{query}</blue>\" добавлена.", query=query)

        self.conn.commit()
        cursor.close()

    def drop_table(self, table):
        """Удаление таблицы."""
        self.open_connection()
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"DROP TABLE IF EXISTS \"{table}\";")
        except psycopg2.DatabaseError as e:
            logger.error(e)
        else:
            logger.opt(colors=True).success("Таблица \"<blue>{table}</blue>\" удалена.", table=table)

        self.conn.commit()
        cursor.close()

    def truncate_table(self, table):
        """Очистка таблицы."""
        self.open_connection()
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"TRUNCATE TABLE \"{table}\";")
        except psycopg2.DatabaseError as e:
            logger.error(e)
        else:
            logger.opt(colors=True).success("Таблица \"<blue>{table}</blue>\" очищена.", table=table)

        self.conn.commit()
        cursor.close()

    def read_table(self, table):
        """Чтение данных из таблицы."""
        self.open_connection()
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"SELECT * FROM \"{table}\";")
        except psycopg2.DatabaseError as e:
            logger.error(e)
        else:
            logger.opt(colors=True).success("Таблица \"<blue>{table}</blue>\" считана.", table=table)

        result = cursor.fetchall()
        cursor.close()
        return result

    def execute_query(self, query):
        """Выполнение запроса."""
        self.open_connection()
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
        except psycopg2.DatabaseError as e:
            logger.error(e)
        else:
            logger.opt(colors=True).success("Запрос \"<blue>{query}</blue>\" выполнен.", query=query)

        cursor.close()
