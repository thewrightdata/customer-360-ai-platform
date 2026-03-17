CREATE TABLE customers (
    customer_id INT,
    name STRING,
    signup_date DATE,
    plan STRING
);

CREATE TABLE transactions (
    transaction_id INT,
    customer_id INT,
    amount FLOAT,
    date DATE
);

CREATE TABLE events (
    event_id INT,
    customer_id INT,
    event_type STRING,
    timestamp TIMESTAMP
);
