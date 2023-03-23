-- creation des tables
use DDLCheckpoint
CREATE TABLE customers (
	customer_id  INT NOT NULL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	email VARCHAR(30) NOT NULL,
	address VARCHAR(60) NOT NULL,
);


CREATE TABLE products (
	product_id  INT NOT NULL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	price DECIMAL(30) NOT NULL CHECK (price>0),
);

CREATE TABLE orders(
	order_id  INT NOT NULL PRIMARY KEY,
	customer_id INT FOREIGN KEY REFERENCES customers(customer_id),
	product_id INT FOREIGN KEY REFERENCES products(product_id),
	quantity INT NOT NULL,
	order_date DATE NOT NULL,
);


