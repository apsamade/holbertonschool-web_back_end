-- Creates an index idx_name_first_score on the table names
-- Only the first letter of name and the score are indexed
CREATE INDEX idx_name_first_score ON names (name(1), score);
