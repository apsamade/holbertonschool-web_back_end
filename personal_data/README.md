# Personal Data

Project on handling Personally Identifiable Information (PII): obfuscating PII
in logs, encrypting passwords, and authenticating to a database using
environment variables.

## Files

| File | Description |
| ---- | ----------- |
| `filtered_logger.py` | `filter_datum` obfuscates fields with a regex; `RedactingFormatter` is a logging formatter that redacts configured PII fields; `get_logger` builds a `user_data` logger; `PII_FIELDS` lists the fields to hide. |

## Learning objectives

- Examples of Personally Identifiable Information (PII).
- Implement a log filter that obfuscates PII fields.
- Encrypt a password and check the validity of an input password.
- Authenticate to a database using environment variables.
