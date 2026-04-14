-- Library Management System Database Schema

-- Books Table
CREATE TABLE Books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    publisher VARCHAR(255),
    publication_year INT,
    total_copies INT NOT NULL DEFAULT 1,
    available_copies INT NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Members Table
CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    phone VARCHAR(15),
    membership_date DATE NOT NULL,
    membership_status VARCHAR(20) DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Loans Table
CREATE TABLE Loans (
    loan_id SERIAL PRIMARY KEY,
    book_id INT NOT NULL REFERENCES Books(book_id) ON DELETE CASCADE,
    member_id INT NOT NULL REFERENCES Members(member_id) ON DELETE CASCADE,
    loan_date DATE NOT NULL DEFAULT CURRENT_DATE,
    due_date DATE NOT NULL,
    return_date DATE,
    status VARCHAR(20) DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexing Strategy
CREATE INDEX idx_loans_member_id ON Loans(member_id);
CREATE INDEX idx_loans_book_id ON Loans(book_id);
CREATE INDEX idx_loans_status ON Loans(status);
CREATE INDEX idx_loans_due_date ON Loans(due_date);
CREATE INDEX idx_loans_return_date ON Loans(return_date);
CREATE INDEX idx_books_isbn ON Books(isbn);
CREATE INDEX idx_members_email ON Members(email);

-- ============================================
-- QUERIES FOR LIBRARY SYSTEM
-- ============================================

-- 1. Retrieve all books currently issued
SELECT 
    b.book_id,
    b.title,
    b.author,
    b.isbn,
    m.first_name,
    m.last_name,
    m.email,
    l.loan_date,
    l.due_date,
    l.status
FROM Loans l
INNER JOIN Books b ON l.book_id = b.book_id
INNER JOIN Members m ON l.member_id = m.member_id
WHERE l.status = 'Active' AND l.return_date IS NULL
ORDER BY l.due_date ASC;

-- 2. Find overdue books (loan date older than 30 days)
SELECT 
    b.book_id,
    b.title,
    b.author,
    m.first_name,
    m.last_name,
    m.email,
    l.loan_date,
    l.due_date,
    CURRENT_DATE - l.due_date AS days_overdue
FROM Loans l
INNER JOIN Books b ON l.book_id = b.book_id
INNER JOIN Members m ON l.member_id = m.member_id
WHERE l.status = 'Active' 
    AND l.return_date IS NULL 
    AND (CURRENT_DATE - l.loan_date) > 30
ORDER BY days_overdue DESC;

-- 3. Count number of books loaned by each member
SELECT 
    m.member_id,
    m.first_name,
    m.last_name,
    m.email,
    COUNT(l.loan_id) AS total_books_loaned,
    COUNT(CASE WHEN l.status = 'Active' THEN 1 END) AS currently_loaned,
    COUNT(CASE WHEN l.status = 'Returned' THEN 1 END) AS books_returned
FROM Members m
LEFT JOIN Loans l ON m.member_id = l.member_id
GROUP BY m.member_id, m.first_name, m.last_name, m.email
ORDER BY total_books_loaned DESC;