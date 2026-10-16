-- Creates a stored procedure ComputeAverageScoreForUser
-- Computes and stores the average score of a student in users.average_score
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    UPDATE users
    SET average_score = (
        SELECT IFNULL(AVG(corrections.score), 0)
        FROM corrections
        WHERE corrections.user_id = user_id
    )
    WHERE users.id = user_id;
END$$
DELIMITER ;
