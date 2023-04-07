-- Create a new database called 'DatabaseName'
-- Connect to the 'master' database to run this snippet
USE master
GO
-- Create the new database if it does not exist already
IF NOT EXISTS (
    SELECT name
        FROM sys.databases
        WHERE name = N'DatabaseDQL'
)
CREATE DATABASE DatabaseDQL
GO
USE DatabaseDQL


-- Drop the table if it already exists
IF OBJECT_ID('customers', 'U') IS NOT NULL
DROP TABLE customers
GO
-- Create the table customers
CREATE TABLE customers
(
    customerId INT NOT NULL PRIMARY KEY, -- primary key column
    customerName VARCHAR(100) NOT NULL,
	customerTel VARCHAR(50) NOT NULL
);
GO
-- Drop the table if it already exists
IF OBJECT_ID('products ', 'U') IS NOT NULL
DROP TABLE products 
GO
-- Create the table products
CREATE TABLE products (
	productId  INT NOT NULL PRIMARY KEY,
	prodactName VARCHAR(150) NOT NULL,
	category	TEXT,
	price  INT NOT NULL CHECK (price>0)
);
GO

-- Drop the table if it already exists
IF OBJECT_ID('orders', 'U') IS NOT NULL
DROP TABLE orders 
GO
-- Create the table orders
CREATE TABLE orders(
	customerId INT FOREIGN KEY REFERENCES customers(customerId),
	productId INT FOREIGN KEY REFERENCES products(productId),
	quantity INT NOT NULL,
	orderDate DATE NOT NULL,
	totalAmount INT,
	CONSTRAINT PK_order PRIMARY KEY (customerId,productId)
);
GO

-- Insert rows into table 'TableName'
INSERT INTO customers
( -- columns to insert data into
 [customerId], [customerName], [customerTel]
)
VALUES
(1, 'Moussa Sarr', '77 560 80 81'),
(2,'Absatou Ndiaye','78 450 18 13'),
(3,'Abdou Fall','70 659 09 15'),
(4,'Awa Mané','76 998 20 31'),
(5,'Mansour Ciss','77 578 32 14'),
(6,'Fatou Diouf','76 738 28 16')


-- Insert rows into table products
INSERT INTO products
( -- columns to insert data into
 [productId], [prodactName], [category] , [price]
)
VALUES
(1, 'widget', 'application', 100000),
(2, 'gadget', 'application', 80000),
(3, 'ordinateur pc', 'materiels info', 250000),
(4, 'clés usb', 'materiels info', 10000),
(5, 'riz', 'aliment cereales', 800),
(6, 'farine de mil', 'aliment cereales', 1700),
(7, 'jus locaux', 'boisson', 2000),
(8, 'boissons gazeuses', 'boisson', 1500),
(9, 'eau', 'boisson', 1000),
(10, 'lait de corps', 'beauté', 3500)


-- Insert rows into table 'orders'
INSERT INTO orders
([customerId], [productId], [quantity],[orderDate],[totalAmount])
VALUES
(3, 1, 2,'2023-01-22',200000),
(3, 2, 1,'2023-01-22',80000),
(5, 3, 1,'2023-02-11',250000),
(5, 4, 3,'2023-02-11',30000),
(2, 5, 2,'2023-03-01',1600),
(2, 6, 1,'2023-03-01',1700),
(2, 7, 5,'2023-03-01',10000),
(6, 10, 1,'2023-03-01',3500)

INSERT INTO orders
([customerId], [productId], [quantity],[orderDate],[totalAmount])
VALUES
(1, 1, 3,'2023-04-06',300000),
(4, 2, 2,'2023-04-06',160000)


/*ecrivez une requete SQL pour recuperer les noms des clients qui ont passe une commande pour au moins un widget et au moins une gadget, 
ainsi que le cout total des gadgets et des widgets commandes par chaque client.
Le cout de chaque article doit etre calcule en multipliant la quantite par le prix du produit */

SELECT c.customerName, p.price*o.quantity as 'montantTotal'
FROM customers c
INNER JOIN orders o on c.customerId = o.customerId 
INNER JOIN products p on   o.productId = p.productId
WHERE  p.prodactName IN ('Widget', 'Gadget')

/* 2. Écrire une requête pour récupérer les noms des clients qui ont passé une commande pour au moins un widget, 
ainsi que le coût total des widgets commandés par chaque client.*/

SELECT c.customerName as 'noms des clients', 
o.totalAmount as 'cout total'
FROM customers c
INNER JOIN orders o on c.customerId = o.customerId 
INNER JOIN products p on   o.productId = p.productId
WHERE  p.prodactName ='Widget'

/* Écrire une requête pour récupérer les noms des clients qui ont passé une commande pour au moins un gadget,
ainsi que le coût total des gadgets commandés par chaque client.*/

SELECT c.customerName as 'noms des clients', 
o.totalAmount as 'cout total'
FROM customers c
INNER JOIN orders o on c.customerId = o.customerId 
INNER JOIN products p on   o.productId = p.productId
WHERE  p.prodactName ='gadget'

/*Ecrivez une requête pour récupérer les noms des clients qui ont passé une commande pour au moins un doohickey, 
ainsi que le coût total des doohickeys commandés par chaque client.*/

SELECT c.customerName as 'noms des clients', 
o.totalAmount as 'cout total'
FROM customers c
INNER JOIN orders o on c.customerId = o.customerId 
INNER JOIN products p on   o.productId = p.productId
WHERE  p.prodactName ='doohickey'

/*Écrivez une requête pour récupérer le nombre total de widgets et de gadgets commandés par chaque client,
ainsi que le coût total des commandes.*/


SELECT c.customerName as 'noms des clients',
SUM(o.quantity) as 'nombre total commande '
FROM customers c
LEFT JOIN orders o on c.customerId = o.customerId 
INNER JOIN products p on   o.productId = p.productId
WHERE  p.prodactName IN ('Widget', 'Gadget')
GROUP BY c.customerName

/* Ecrivez une requête pour récupérer les noms des produits qui ont été commandés par au moins un client,
   ainsi que la quantité totale de chaque produit commandé.*/

SELECT p.prodactName as 'produits commandes', 
sum(o.quantity) as 'quantite total'
FROM products p
INNER join orders o on  p.productId= o.productId 
GROUP BY p.prodactName
   
/*Écrire une requête pour récupérer les noms des clients qui ont passé le plus grand nombre de commandes,
ainsi que le nombre total de commandes passées par chaque client.*/

SELECT c.customerName as 'noms des clients',
COUNT(o.customerId) as 'nombre total de commande '
FROM customers c
INNER JOIN orders o on c.customerId = o.customerId 
GROUP BY c.customerName

SELECT c.customerName as 'noms des clients',
COUNT(o.customerId) as 'nombre total de commande '
FROM customers c
INNER JOIN orders o on c.customerId = o.customerId 
GROUP BY c.customerName
HAVING COUNT(o.customerId) > 1


/*Ecrivez une requête pour récupérer les noms des produits les plus commandés,
ainsi que la quantité totale de chaque produit commandé.*/

SELECT p.prodactName as 'produits commandes', 
sum(o.quantity)as 'quantite total'
FROM products p
INNER join orders o on  p.productId= o.productId 
GROUP BY p.prodactName
HAVING sum(o.quantity) > 1

 /*Ecrivez une requête pour récupérer les noms des clients qui ont passé une commande chaque jour de la semaine,
  ainsi que le nombre total de commandes passées par chaque client.*/

SELECT  c.customerName as 'noms des clients',
DATENAME(WEEK, o.orderDate) as 'semaine de la commande',
DATENAME(WEEKDAY, o.orderDate) as 'jour de la commande'
FROM customers c
INNER JOIN orders o on c.customerId = o.customerId 



SELECT c.customerName as 'noms des clients',
COUNT(o.customerId) as 'nombre total de commande '
FROM customers c
INNER JOIN orders o on c.customerId = o.customerId 
GROUP BY c.customerName