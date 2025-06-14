-- pc_schema_p.sql

DROP table if exists Product;
CREATE table Product(maker varchar(1), model integer, type varchar(10));

DROP table if exists PC;
CREATE table PC(model integer, speed float, ram integer, hd integer, price integer);

DROP table if exists Laptop;
CREATE table Laptop(model integer, speed float, ram integer, hd integer, screen float, price integer);

DROP table if exists Printer;
CREATE table Printer(model integer, color boolean, type varchar(10), price integer);

start transaction;
insert into Product values('A', 1001, 'pc');
insert into Product values('A', 1002, 'pc');
insert into Product values('A', 1003, 'pc');
insert into Product values('A', 2004, 'laptop');
insert into Product values('A', 2005, 'laptop');
insert into Product values('A', 2006, 'laptop');
insert into Product values('B', 1004, 'pc');
insert into Product values('B', 1005, 'pc');
insert into Product values('B', 1006, 'pc');
insert into Product values('B', 2007, 'laptop');
insert into Product values('C', 1007, 'pc');
insert into Product values('D', 1008, 'pc');
insert into Product values('D', 1009, 'pc');
insert into Product values('D', 1010, 'pc');
insert into Product values('D', 3004, 'printer');
insert into Product values('D', 3005, 'printer');
insert into Product values('E', 1011, 'pc');
insert into Product values('E', 1012, 'pc');
insert into Product values('E', 1013, 'pc');
insert into Product values('E', 2001, 'laptop');
insert into Product values('E', 2002, 'laptop');
insert into Product values('E', 2003, 'laptop');
insert into Product values('E', 3001, 'printer');
insert into Product values('E', 3002, 'printer');
insert into Product values('E', 3003, 'printer');
insert into Product values('F', 2008, 'laptop');
insert into Product values('F', 2009, 'laptop');
insert into Product values('G', 2010, 'laptop');
insert into Product values('H', 3006, 'printer');
insert into Product values('H', 3007, 'printer');

insert into PC values(1001, 2.66, 1024, 250, 2114);
insert into PC values(1002, 2.10, 512, 250, 995);
insert into PC values(1003, 1.42, 512, 80, 478);
insert into PC values(1004, 2.80, 1024, 250, 649);
insert into PC values(1005, 3.20, 512, 250, 630);
insert into PC values(1006, 3.20, 1024, 320, 1049);
insert into PC values(1007, 2.20, 1024, 200, 510);
insert into PC values(1008, 2.20, 2048, 250, 770);
insert into PC values(1009, 2.00, 1024, 250, 650);
insert into PC values(1010, 2.80, 2048, 300, 770);
insert into PC values(1011, 1.86, 2048, 160, 959);
insert into PC values(1012, 2.80, 1024, 160, 649);
insert into PC values(1013, 3.06, 512, 80, 529);

insert into Laptop values(2001, 2.00, 2048, 240, 20.1, 3673);
insert into Laptop values(2002, 1.73, 1024, 80, 17.0, 949);
insert into Laptop values(2003, 1.80, 512, 60, 15.4, 549);
insert into Laptop values(2004, 2.00, 512, 60, 13.3, 1150);
insert into Laptop values(2005, 2.16, 1024, 120, 17.0, 2500);
insert into Laptop values(2006, 2.00, 2048, 80, 15.4, 1700);
insert into Laptop values(2007, 1.83, 1024, 120, 13.3, 1249);
insert into Laptop values(2008, 1.60, 1024, 100, 15.4, 900);
insert into Laptop values(2009, 1.60, 512, 80, 14.1, 680);
insert into Laptop values(2010, 2.00, 2048, 160, 15.4, 2300);

insert into Printer values(3001, 'true', 'ink-jet', 99);
insert into Printer values(3002, 'false', 'laser', 239);
insert into Printer values(3003, 'true', 'laser',899);
insert into Printer values(3004, 'true', 'ink-jet', 120);
insert into Printer values(3005, 'false', 'laser', 120);
insert into Printer values(3006, 'true', 'ink-jet',100);
insert into Printer values(3007, 'true', 'laser', 200);

commit;

SELECT
	NULL AS maker,
	PC.model,
	PC.speed AS GHz,
	PC.hd AS GB,
	NULL::FLOAT AS screen_size,
	NULL::BOOLEAN AS color_printer,
	'(a) PC under $1000' AS Product_Type,
	NULL AS price
FROM PC
JOIN Product ON PC.model = Product.model
WHERE PC.price < 1000

UNION

SELECT
	NULL AS maker,
	PC.model,
	PC.speed AS GHz,
	NULL::INTEGER AS GB,
	NULL::FLOAT AS screen_size,
	NULL::BOOLEAN AS color_printer,
	'(h) Model and Price of fastest PC',
	PC.Price
FROM PC
JOIN Product ON PC.model = Product.model
WHERE PC.speed = (
	SELECT MAX(speed) FROM PC
)

UNION

SELECT
	Product.maker,
	PC.model AS model,
	NULL::FLOAT AS GHz,
	NULL::INTEGER AS GB,
	NULL::FLOAT AS screen_size,
	NULL::BOOLEAN AS color_printer,
	'(d) PC Price & model manufacturer B' AS Product_Type,
	PC.Price
FROM PC
JOIN Product ON PC.model = Product.model
WHERE Product.maker = 'B'

UNION

SELECT
	Product.maker,
	PC.model AS model,
	NULL::FLOAT AS GHz,
	NULL::INTEGER AS GB,
	NULL::FLOAT AS screen_size,
	NULL::BOOLEAN AS color_printer,
	'(j) Manufacturer with 3 or more PCs' AS Product_Type,
	NULL AS Price
FROM PC
JOIN Product ON PC.model = Product.model
WHERE PC.model > 2

UNION

SELECT
	Product.maker,
	NULL::INTEGER AS model,
	NULL::FLOAT AS GHz,
	NULL::INTEGER AS GB,
	NULL::FLOAT AS screen_size,
	NULL::BOOLEAN AS color_printer,
	'(k) MAX Price PC for each Manufacturer' AS Product_Type,
	MAX(PC.Price) AS Price
FROM PC
JOIN Product ON PC.model = Product.model
GROUP BY Product.maker

UNION

SELECT
	Product.maker,
	NULL::INTEGER AS model,
	NULL::FLOAT AS GHz,
	AVG(PC.hd) AS GB,
	NULL::FLOAT AS screen_size,
	NULL::BOOLEAN AS color_printer,
	'(l) Average HD size for PCs by printer manufacturer' AS Product_Type,
	MAX(PC.Price) AS Price
FROM PC
JOIN Product ON PC.model = Product.model
WHERE Product.maker IN (
    SELECT DISTINCT Product.maker
    FROM Product
    JOIN Printer ON Product.model = Printer.model
)
GROUP BY Product.maker

UNION

SELECT
	Product.maker,
	NULL::INTEGER AS model,
	NULL::FLOAT AS GHz,
	NULL::INTEGER AS GB,
	NULL::FLOAT AS screen_size,
	NULL::BOOLEAN AS color_printer,
	'(b) Printer manufacturers' AS Product_Type,
	NULL AS price
FROM Printer
JOIN Product ON Printer.model = Product.model
WHERE Product.type = 'printer'

UNION

SELECT
	Product.maker,
	Printer.model AS model,
	NULL::FLOAT AS GHz,
	NULL::INTEGER AS GB,
	NULL::FLOAT AS screen_size,
	NULL::BOOLEAN AS color_printer,
	'(d) Printer Price & model manufacturer B' AS Product_Type,
	Printer.Price
FROM Printer
JOIN Product ON Printer.model = Product.model
WHERE Product.maker = 'B'

UNION

SELECT
	Product.maker,
	NULL::INTEGER AS model,
	NULL::FLOAT AS GHz,
	NULL::INTEGER AS GB,
	NULL::FLOAT AS screen_size,
	Printer.color AS color_printer,
	'(g) Maker of cheapest color printer' AS Product_Type,
	Printer.price AS Price
	FROM Printer
	JOIN Product ON Printer.model = Product.model
	WHERE Printer.color = 'TRUE'
  		AND Printer.price = (
    		SELECT MIN(price)
    		FROM Printer
    		WHERE color = 'TRUE'
	)

UNION

SELECT 
	Product.maker,
	NULL::INTEGER AS model,
	NULL::FLOAT AS GHz,
	Laptop.hd AS GB,
	NULL::FLOAT AS screen_size,
	NULL::BOOLEAN AS color_printer,
	'(c) Laptop > 29gb' AS Product_Type,
	NULL AS price
FROM Laptop
JOIN Product ON Laptop.model = Product.model
WHERE Laptop.hd > 29

UNION

SELECT
	Product.maker,
	NULL::INTEGER AS model,
	NULL::FLOAT AS GHz,
	NULL::INTEGER AS GB,
	NULL::FLOAT AS screen_size,
	NULL::BOOLEAN AS color_printer,
	'(e) Laptop and not PC' AS Product_Type,
	NULL AS Price
FROM Laptop
JOIN Product ON Laptop.model = Product.model
WHERE product.type = 'laptop'
AND Product.maker NOT IN (
    SELECT Product.maker
    FROM Product
    WHERE Product.type = 'pc'
)

UNION

SELECT
	Product.maker,
	Laptop.model AS model,
	NULL::FLOAT AS GHz,
	NULL::INTEGER AS GB,
	NULL::FLOAT AS screen_size,
	NULL::BOOLEAN AS color_printer,
	'(d) Laptop Price & model manufacturer B' AS Product_Type,
	Laptop.Price
FROM Laptop
JOIN Product ON Laptop.model = Product.model
WHERE Product.maker = 'B'

UNION

SELECT
	NULL AS maker,
	NULL::INTEGER AS model,
	Laptop.speed AS GHz,
	NULL::INTEGER AS GB,
	NULL::FLOAT AS screen_size,
	NULL::BOOLEAN AS color_printer,
	'(f) Laptop slower than PCs' AS Product_Type,
	NULL AS Price
FROM Laptop
JOIN Product ON Laptop.model = Product.model
WHERE Laptop.speed < (
	SELECT MIN(speed) FROM PC
)

UNION

SELECT
	Product.maker,
	NULL::INTEGER AS model,
	NULL::FLOAT AS GHz,
	NULL::INTEGER AS GB,
	AVG(Laptop.screen) AS screen_size,
	NULL::BOOLEAN AS color_printer,
	'(i) Average screen size' AS Product_Type,
	NULL AS Price
FROM Laptop
JOIN Product ON Laptop.model = Product.model
GROUP BY Product.maker;
	
	
	