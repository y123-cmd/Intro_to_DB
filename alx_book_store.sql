<<<<<<< HEAD
-- Create database
CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;

-- Create Authors table
CREATE TABLE IF NOT EXISTS Authors (
=======

CREATE DATABASE alx_book_store;


USE alx_book_store;

CREATE TABLE Authors (
>>>>>>> origin/main
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);

<<<<<<< HEAD
-- Create Books table
CREATE TABLE IF NOT EXISTS Books (
=======

CREATE TABLE Books (
>>>>>>> origin/main
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id INT,
    price DOUBLE NOT NULL,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

<<<<<<< HEAD
-- Create Customers table
CREATE TABLE IF NOT EXISTS Customers (
=======
CREATE TABLE Customers (
>>>>>>> origin/main
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL,
    address TEXT
);

<<<<<<< HEAD
-- Create Orders table
CREATE TABLE IF NOT EXISTS Orders (
=======
CREATE TABLE Orders (
>>>>>>> origin/main
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

<<<<<<< HEAD
-- Create Order_Details table
CREATE TABLE IF NOT EXISTS Order_Details (
=======

CREATE TABLE Order_Details (
>>>>>>> origin/main
    orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity DOUBLE NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

