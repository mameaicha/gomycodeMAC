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



INSERT  into customers values
(1,'DIOP Malick','m.diop@gmail.com','rue 10 angle 12 Dakar') ,
(2,'KANE Aïcha','kaneaicha@gmail.com','pikine tali bou bess'),
(3,'Fall Nafi','nafifall92@yahoo.fr','hlm grand medine'),
(4,'CISS Mamour','maciss@gmail.com','tivaoune peulh')


INSERT  into products values
(1, 'parfun dove', 3500),
(2, 'confiture mangue', 2000),
(3, 'savon', 2500),
(4, 'chaussure', 6000),
(5, 'tapis ', 10000),
(6, 'ballon ', 8000)



INSERT  into orders values
(1,3,1,1,'31-12-2022'),
(2,3,4,2,'31-12-2022'),
(3,4,6,1,'20-01-2023'),
(4,1,3,3,'22-01-2023'),
(5,2,2,5,'28-02-2023')