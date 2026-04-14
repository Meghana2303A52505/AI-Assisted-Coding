
-- Users Table
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Products Table
CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL,
    category VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Orders Table
CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(12, 2),
    status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- OrderDetails Table
CREATE TABLE OrderDetails (
    order_detail_id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE RESTRICT
);

-- ============================================
-- QUERIES
-- ============================================

-- 1. Retrieve all orders placed by a specific user
SELECT 
    o.order_id, 
    o.order_date, 
    o.total_amount, 
    o.status
FROM Orders o
JOIN Users u ON o.user_id = u.user_id
WHERE u.username = 'john_doe'
ORDER BY o.order_date DESC;

-- 2. Find the most purchased product
SELECT 
    p.product_id,
    p.product_name,
    SUM(od.quantity) AS total_quantity_sold
FROM Products p
JOIN OrderDetails od ON p.product_id = od.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity_sold DESC
LIMIT 1;

-- 3. Calculate total revenue in a given month
SELECT 
    SUM(od.quantity * od.unit_price) AS total_revenue
FROM OrderDetails od
JOIN Orders o ON od.order_id = o.order_id
WHERE EXTRACT(MONTH FROM o.order_date) = 12
  AND EXTRACT(YEAR FROM o.order_date) = 2024;

-- ============================================
-- OPTIMIZATION & INDEXES
-- ============================================

-- Index for faster user lookups
CREATE INDEX idx_users_username ON Users(username);
CREATE INDEX idx_users_email ON Users(email);

-- Index for order queries by user
CREATE INDEX idx_orders_user_id ON Orders(user_id);
CREATE INDEX idx_orders_order_date ON Orders(order_date);

-- Index for order details queries
CREATE INDEX idx_orderdetails_order_id ON OrderDetails(order_id);
CREATE INDEX idx_orderdetails_product_id ON OrderDetails(product_id);

-- Index for product category searches
CREATE INDEX idx_products_category ON Products(category);

