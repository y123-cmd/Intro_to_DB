-- Create table 'books'
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(255),
    author_id INT,
    price DECIMAL(10, 2)
);

-- Create table 'authors'
CREATE TABLE authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(255)
);

-- Create table 'customers'
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255),
    email VARCHAR(255)
);

-- Create table 'orders'
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE
);

-- Create table 'order_details'
CREATE TABLE order_details (
    order_detail_id INT PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity INT
);
