/* Procedimiento Almacenado 'get_authors' */
DELIMITER $$
CREATE PROCEDURE `get_authors`()
BEGIN
    SELECT * FROM authors ORDER BY last_name ASC, first_name DESC;
END$$
DELIMITER ;
/* Procedimiento Almacenado 'get_authors' */

/* Procedimiento Almacenado 'get_posts' */
DELIMITER $$
CREATE PROCEDURE `get_posts`()
BEGIN
    SELECT * FROM posts ORDER BY title ASC;
END$$
DELIMITER ;
/* Procedimiento Almacenado 'get_posts' */

CALL get_authors();
CALL get_posts();
