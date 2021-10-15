SELECT * FROM users;

INSERT INTO sushi (name, price, description, rolls_number) VALUES ("Salmon skin roll",12,"Toasted salmon skin, cream cheese, covered with masago and sesame seeds bathed in teriyaki sauce.", 6);
SELECT * from sushi;

INSERT INTO beverages (name, price) VALUES ("Water", 3);
SELECT * from beverages;

INSERT INTO sides (name,price) VALUES ("Edamame", 4);
SELECT * from sides;

SELECT sushi.name, sushi.price, sushi.id, beverages.name, beverages.price, sides.name, sides.price from orders;

select * from orders;


select * from orders WHERE user_id = 2 ORDER BY id DESC LIMIT 1;

delete from orders WHERE user_id = 2 ORDER BY id DESC LIMIT 1;

delete from past_orders WHERE id =5;

INSERT INTO past_orders (user_id, order_id) VALUES (2,1);

SELECT * FROM orders WHERE user_id = 2;
SELECT * FROM past_orders;

DELETE from past_orders where id >0;

SELECT * from past_orders;

UPDATE past_orders SET favorite = 1 WHERE id = 14;

-- Query para ordenes --
SELECT orders.id as order_id, sushi.id as sushi_id, sushi.name as sushi_name, sushi.price as sushi_price, beverages.name as beverage_name, beverages.price as beverage_price, sides.name as side_name, sides.price as side_price, users.id as user_id, users.first_name as user_name FROM orders JOIN sushi ON sushi.id = orders.sushi_id JOIN beverages ON beverages.id = orders.beverage_id JOIN sides ON sides.id = orders.side_id JOIN users ON users.id = orders.user_id WHERE users.id = 2 ORDER BY order_id DESC LIMIT 1;

SELECT orders.id as order_id, sushi.id as sushi_id, sushi.name as sushi_name, sushi.price as sushi_price,beverages.id as beverage_id, beverages.name as beverage_name, beverages.price as beverage_price,sides.id as side_id, sides.name as side_name, sides.price as side_price, users.id as user_id, users.first_name as user_name FROM orders JOIN sushi ON sushi.id = orders.sushi_id JOIN beverages ON beverages.id = orders.beverage_id JOIN sides ON sides.id = orders.side_id JOIN users ON users.id = orders.user_id WHERE users.id = 2 ORDER BY order_id DESC LIMIT 1;

SELECT DISTINCT past_orderst_orders.id as past_order_id, orders.id as order_id, sushi.id as sushi_id, sushi.name as sushi_name, sushi.price as sushi_price, beverages.name as beverage_name, beverages.price as beverage_price, sides.name as side_name, sides.price as side_price, users.id as user_id, users.first_name as user_name  
FROM past_orders 
JOIN users ON past_orders.user_id = users.id 
JOIN orders ON past_orders.order_id = orders.id 
JOIN sushi ON orders.sushi_id = sushi.id 
JOIN beverages ON orders.beverage_id = beverages.id 
JOIN sides ON orders.side_id = sides.id 
WHERE users.id = 2 ORDER BY past_order_id DESC; 



SELECT DISTINCT past_orders.id as past_order_id, sushi.id as sushi_id, sushi.name as sushi_name, sushi.price as sushi_price, beverages.name as beverage_name, beverages.price as beverage_price, sides.name as side_name, sides.price as side_price, users.id as user_id, users.first_name as user_name
FROM past_orders
JOIN users ON past_orders.user_id = users.id 
JOIN sushi ON past_orders.sushi_id = sushi.id
JOIN beverages ON past_orders.beverage_id = beverages.id
JOIN sides ON past_orders.side_id = sides.id
WHERE users.id = 2 ORDER BY past_orders.id DESC;


SELECT DISTINCT past_orders.id as past_order_id, sushi.id as sushi_id, sushi.name as sushi_name, sushi.price as sushi_price, beverages.name as beverage_name, beverages.price as beverage_price, sides.name as side_name, sides.price as side_price, users.id as user_id, users.first_name as user_name FROM past_orders JOIN users ON past_orders.user_id = users.id  JOIN sushi ON past_orders.sushi_id = sushi.id JOIN beverages ON past_orders.beverage_id = beverages.id JOIN sides ON past_orders.side_id = sides.id WHERE users.id = 2 ORDER BY past_orders.id DESC;


UPDATE users SET first_name = "Vale", last_name = "Romero", email = "valellope@gmail.com", address = "4608", city = "doraville", state  = "california", zipcode = "30360" WHERE id = 2;