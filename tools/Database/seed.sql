CREATE TABLE IF NOT EXISTS users(
	id SERIAL PRIMARY KEY,
	name character varying(255) UNIQUE NOT NULL,
	email character varying(255) NOT NULL,
	password character varying(255) UNIQUE NOT NULL
);

INSERT INTO users(id, name, email, password) VALUES (1, 'juana', 'juana@udea.edu.co', 'pass123');
INSERT INTO users(id, name, email, password) VALUES (2, 'pablo', 'pablo@udea.edu.co', 'pass456');