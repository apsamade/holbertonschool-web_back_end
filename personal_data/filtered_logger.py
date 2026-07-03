#!/usr/bin/env python3
"""Module for obfuscating personally identifiable information in log lines."""
import logging
import os
import re
from typing import List

import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Return the log message with the given fields obfuscated."""
    return re.sub(rf'({"|".join(fields)})=[^{separator}]*',
                  rf'\1={redaction}', message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class that obfuscates PII fields in log records."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the formatter with the list of fields to redact."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record, obfuscating the configured PII fields."""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def get_logger() -> logging.Logger:
    """Return a logger for user data that redacts PII fields when logging."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Return a connector to the secure database using env credentials."""
    return mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME"),
    )


def main() -> None:
    """Retrieve every row of the users table and log it with PII redacted."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    columns = [column[0] for column in cursor.description]
    logger = get_logger()
    for row in cursor:
        message = "; ".join(f"{col}={val}" for col, val in zip(columns, row))
        logger.info(message + ";")
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
