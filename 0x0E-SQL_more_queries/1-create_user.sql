-- 1-create_user.sql
-- Write a script that creates the MySQL server user user_0d_1
CREATE USER 'user_0d_1'@'localhost' IF NOT EXISTS IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
