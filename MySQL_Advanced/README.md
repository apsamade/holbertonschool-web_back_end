# MySQL Advanced

Advanced MySQL concepts: table constraints, indexes, stored procedures and functions, views and triggers.

All scripts are executed on Ubuntu 20.04 LTS using MySQL 8.0.

## Tasks

| File | Description |
| ---- | ----------- |
| `0-uniq_users.sql` | Creates a table `users` with `id` (auto increment, primary key), `email` (unique, not null) and `name` |
| `1-country_users.sql` | Same `users` table plus `country`, an enumeration (`US`, `CO`, `TN`), not null, defaulting to `US` |
