-- ============================================
-- Library Management System Database Design
-- ============================================

-- 1. AUTHORS TABLE
CREATE TABLE Authors (
    author_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    country VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. BOOKS TABLE
CREATE TABLE Books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    total_copies INT DEFAULT 1,
    available_copies INT DEFAULT 1,
    publication_year INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id) ON DELETE CASCADE
);

-- 3. MEMBERS TABLE
CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    phone VARCHAR(20),
    membership_date DATE NOT NULL,
    status VARCHAR(50) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. LOANS TABLE
CREATE TABLE Loans (
    loan_id SERIAL PRIMARY KEY,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    loan_date DATE NOT NULL DEFAULT CURRENT_DATE,
    due_date DATE NOT NULL,
    return_date DATE,
    status VARCHAR(50) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (book_id) REFERENCES Books(book_id) ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES Members(member_id) ON DELETE CASCADE
);

-- ============================================
-- INDEXING STRATEGY
-- ============================================

CREATE INDEX idx_books_author_id ON Books(author_id);
CREATE INDEX idx_loans_member_id ON Loans(member_id);
CREATE INDEX idx_loans_book_id ON Loans(book_id);
CREATE INDEX idx_loans_status ON Loans(status);
CREATE INDEX idx_loans_loan_date ON Loans(loan_date);
CREATE INDEX idx_loans_due_date ON Loans(due_date);
CREATE INDEX idx_authors_country ON Authors(country);

-- ============================================
-- QUERIES FOR LIBRARY SYSTEM
-- ============================================

-- Query 1: Retrieve all books currently issued
SELECT 
    b.book_id,
    b.title,
    a.name AS author,
    m.name AS member,
    l.loan_date,
    l.due_date
FROM Books b
INNER JOIN Authors a ON b.author_id = a.author_id
INNER JOIN Loans l ON b.book_id = l.book_id
INNER JOIN Members m ON l.member_id = m.member_id
WHERE l.status = 'active' AND l.return_date IS NULL;

-- Query 2: Find overdue books (loan date older than 30 days)
SELECT 
    b.book_id,
    b.title,
    m.name AS member,
    m.email,
    l.due_date,
    CURRENT_DATE - l.due_date AS days_overdue
FROM Books b
INNER JOIN Loans l ON b.book_id = l.book_id
INNER JOIN Members m ON l.member_id = m.member_id
WHERE l.return_date IS NULL 
    AND CURRENT_DATE > l.due_date
ORDER BY l.due_date ASC;

-- Query 3: Count number of books loaned by each member
SELECT 
    m.member_id,
    m.name,
    COUNT(l.loan_id) AS total_books_loaned,
    COUNT(CASE WHEN l.status = 'active' THEN 1 END) AS currently_issued
FROM Members m
LEFT JOIN Loans l ON m.member_id = l.member_id
GROUP BY m.member_id, m.name
ORDER BY total_books_loaned DESC;

-- ============================================
-- QUERY OPTIMIZATION - TASK 4
-- ============================================

-- ❌ ORIGINAL QUERY (Subquery - Slower)
-- SELECT * FROM Books 
-- WHERE author_id IN (
--     SELECT author_id FROM Authors WHERE country='UK'
-- );

-- ✅ OPTIMIZED QUERY (Using JOIN - Faster)
SELECT DISTINCT
    b.book_id,
    b.title,
    b.isbn,
    b.total_copies,
    b.available_copies,
    b.publication_year,
    a.author_id,
    a.name AS author_name,
    a.country
FROM Books b
INNER JOIN Authors a ON b.author_id = a.author_id
WHERE a.country = 'UK';

-- ✅ EXPLANATION:
-- Why JOIN is faster than IN subquery:
-- 1. Single table scan: JOIN processes Authors and Books in one pass
-- 2. No redundant lookups: IN subquery scans Authors table, then filters Books for each result
-- 3. Query optimizer: Modern DBs optimize JOINs better than IN with subqueries
-- 4. Index utilization: JOINs leverage foreign key indexes more efficiently
-- 5. Memory efficiency: No intermediate result set stored for large author lists

-- Performance comparison for large datasets:
-- - Subquery: O(n*m) where n=Authors rows, m=Books rows
-- - JOIN: O(n+m) with proper indexing