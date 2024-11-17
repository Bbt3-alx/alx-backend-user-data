#!/usr/bin/env python3
"""
Regex-ing: with a function that return the log message
"""


from typing import List
import re
import logging
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """A function that returns the log message obfuscated"""
    pattern = f"({'|'.join(fields)})=([^'{separator}']+)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR
        )
        return super().format(record)


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    # Create and configure the logger
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Create a StreamHandler with RedactingFormatter as its formatter
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(handler)

    return logger


def get_db() -> MySQLConnection:
    # Fetch environment variables with default values
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    # Connect to the database
    connection = mysql.connector.connect(
        user=username, password=password, host=host, database=database
    )
    return connection
