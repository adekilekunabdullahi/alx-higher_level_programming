-- Change the database's default character set and collation
ALTER DATABASE hbtn_0c_0
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- Change the character set and collation for the 'name' field in 'first_table'
ALTER TABLE first_table
  MODIFY name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
