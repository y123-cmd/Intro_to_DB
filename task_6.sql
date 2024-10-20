USE alx_book_store;

DROP TABLE IF EXISTS Customers;

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255),
    email VARCHAR(255),
    address VARCHAR(255)
);

INSERT INTO Customers (customer_id, customer_name, email, address) VALUES 
(2, 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness Ave.'),
(3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness Ave.'),
(4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness Ave.');

SELECT * FROM Customers;

