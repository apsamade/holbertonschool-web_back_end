-- Creates a view need_meeting listing students that need a meeting
-- Score strictly under 80 AND no last_meeting or last_meeting more than 1 month ago
CREATE OR REPLACE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < ADDDATE(CURDATE(), INTERVAL -1 MONTH));
