# MySQL Advanced

Advanced MySQL concepts: table constraints, indexes, stored procedures and functions, views and triggers.

All scripts are executed on Ubuntu 20.04 LTS using MySQL 8.0.

## Tasks

| File | Description |
| ---- | ----------- |
| `0-uniq_users.sql` | Creates a table `users` with `id` (auto increment, primary key), `email` (unique, not null) and `name` |
| `1-country_users.sql` | Same `users` table plus `country`, an enumeration (`US`, `CO`, `TN`), not null, defaulting to `US` |
| `2-fans.sql` | Ranks band origins by total number of fans (`origin`, `nb_fans`) from `metal_bands` |
| `3-glam_rock.sql` | Lists Glam rock bands ranked by lifespan (`band_name`, `lifespan`) up to 2024 |
| `4-store.sql` | Trigger that decreases an item's quantity in `items` after a new row is inserted in `orders` |
| `5-valid_email.sql` | Trigger that resets `valid_email` in `users` only when `email` is changed |
| `6-bonus.sql` | Stored procedure `AddBonus` that adds a correction, creating the project if needed |
| `7-average_score.sql` | Stored procedure `ComputeAverageScoreForUser` that computes and stores a student's average score |
| `8-index_my_names.sql` | Creates index `idx_name_first` on the first letter of `names.name` |
| `9-index_name_score.sql` | Creates index `idx_name_first_score` on the first letter of `name` and `score` |
| `10-div.sql` | Function `SafeDiv(a, b)` that returns `a / b`, or 0 if `b` is 0 |
| `11-need_meeting.sql` | View `need_meeting` listing students with a score under 80 and no meeting in the last month |
