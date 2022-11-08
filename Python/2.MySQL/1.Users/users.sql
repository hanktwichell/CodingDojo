use users;

INSERT INTO users (id, first_name, last_name, email)
VALUES(1, 'Hank', 'Twichell', 'ht@gmail.com');

INSERT INTO users (id, first_name, last_name, email)
VALUES(2, 'John', 'Twichell', 'jt@gmail.com');

INSERT INTO users (id, first_name, last_name, email)
VALUES(3, 'Jane', 'Doe', 'jd@gmail.com');

SELECT * 
FROM users;

SELECT * 
FROM users;

SELECT *
FROM users
WHERE email = 'ht@gmail.com';

SELECT *
FROM users
WHERE id = 3;

UPDATE users SET
last_name = 'Pancakes'
WHERE id = 3;

DELETE FROM users
WHERE id = 2;

SELECT *
FROM users
ORDER BY first_name ASC;

SELECT *
FROM users
ORDER BY first_name DESC;


