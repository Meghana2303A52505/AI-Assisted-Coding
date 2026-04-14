-- University Course Registration System - Normalized Database Schema (3NF)

-- Students Table
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    enrollment_date DATE NOT NULL
);

-- Faculty Table
CREATE TABLE Faculty (
    faculty_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department VARCHAR(50) NOT NULL
);

-- Courses Table
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    course_code VARCHAR(20) UNIQUE NOT NULL,
    credits INT NOT NULL,
    faculty_id INT NOT NULL,
    FOREIGN KEY (faculty_id) REFERENCES Faculty(faculty_id) ON DELETE RESTRICT
);

-- Registrations Table (Junction table for many-to-many relationship)
CREATE TABLE Registrations (
    registration_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    registration_date DATE NOT NULL,
    grade VARCHAR(2),
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE,
    UNIQUE(student_id, course_id)
);

-- Query 1: List all students enrolled in a specific course
SELECT s.student_id, s.first_name, s.last_name, s.email, c.course_name
FROM Students s
JOIN Registrations r ON s.student_id = r.student_id
JOIN Courses c ON r.course_id = c.course_id
WHERE c.course_id = 1;

-- Query 2: Find faculty members teaching more than 2 courses
SELECT f.faculty_id, f.first_name, f.last_name, COUNT(c.course_id) AS course_count
FROM Faculty f
JOIN Courses c ON f.faculty_id = c.faculty_id
GROUP BY f.faculty_id, f.first_name, f.last_name
HAVING COUNT(c.course_id) > 2;

-- Query 3: Retrieve courses with the highest number of registrations
SELECT c.course_id, c.course_name, COUNT(r.registration_id) AS enrollment_count
FROM Courses c
LEFT JOIN Registrations r ON c.course_id = r.course_id
GROUP BY c.course_id, c.course_name
ORDER BY enrollment_count DESC;