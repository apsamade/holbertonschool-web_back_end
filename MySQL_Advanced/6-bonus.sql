-- Creates a stored procedure AddBonus that adds a new correction for a student
-- The project is created if no project with this name exists yet
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM projects WHERE name = project_name) THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, (SELECT id FROM projects WHERE name = project_name LIMIT 1), score);
END$$
DELIMITER ;
