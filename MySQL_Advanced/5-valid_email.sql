-- Creates a trigger that resets valid_email only when the email has been changed
-- The check runs before the update so the new row can be modified
DROP TRIGGER IF EXISTS reset_valid_email;
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
SET NEW.valid_email = IF(NEW.email <> OLD.email, 0, NEW.valid_email);
