CREATE DATABASE IF NOT EXISTS cocinamama;

USE cocinamama;

CREATE TABLE users
(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(255),
	email VARCHAR(255),
	password VARCHAR(255),
	phone VARCHAR(255),
	photo VARCHAR(255),
	CONSTRAINT pk_users PRIMARY KEY (id)
);

CREATE TABLE addresses
(
	id INT NOT NULL AUTO_INCREMENT,
	city VARCHAR(200),
	province VARCHAR(200),
	district VARCHAR(200),
	address VARCHAR(200),
	latitude FLOAT,
	longitude FLOAT,
	user_id INT,
	CONSTRAINT pk_address PRIMARY KEY (id),
	CONSTRAINT fk_address_users FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE publications
(
	id INT NOT NULL AUTO_INCREMENT,
	title VARCHAR(255),
	description VARCHAR(255),
	datepublish datetime,
	photo VARCHAR(255),
	CONSTRAINT pk_publications PRIMARY KEY (id)
);

CREATE TABLE publicationsdetails
(
	id INT NOT NULL AUTO_INCREMENT,
	title VARCHAR(255),
	description VARCHAR(255),
	price FLOAT,
	photo VARCHAR(255),
	publication_id INT,
	CONSTRAINT pk_publicationsdetails PRIMARY KEY (id),
	CONSTRAINT fk_publicationsdetails_publications FOREIGN KEY (publication_id) REFERENCES publications(id)
);

CREATE TABLE orders
(
	id INT NOT NULL AUTO_INCREMENT,
	user_id INT NOT NULL,
	registerdate datetime,
	totalamount FLOAT,
	address_id INT,
	payment VARCHAR(255),
	state VARCHAR(255),
	descriptionstate VARCHAR(800),
	photo VARCHAR(255),
	comment VARCHAR(800),
	star INT,
	CONSTRAINT pk_orders PRIMARY KEY (id),
	CONSTRAINT fk_orders_users FOREIGN KEY (user_id) REFERENCES users(id),
	CONSTRAINT fk_orders_addresses FOREIGN KEY (address_id) REFERENCES addresses(id)
);

CREATE TABLE ordersdetails
(
	id INT NOT NULL AUTO_INCREMENT,
	order_id INT NOT NULL,
	publicationdetail_id INT NOT NULL,
	typeorder VARCHAR(50),
	price FLOAT,
	amount INT,
	CONSTRAINT pk_ordersdetails PRIMARY KEY (id),
	CONSTRAINT fk_ordersdetails_orders FOREIGN KEY (order_id) REFERENCES orders(id),
	CONSTRAINT fk_ordersdetails_publicationsdetails FOREIGN KEY (publicationdetail_id) REFERENCES publicationsdetails(id)
);