-- Drop tables if exist
DROP TABLE IF EXISTS appointment;
DROP TABLE IF EXISTS patient;
DROP TABLE IF EXISTS doctor;

-- Doctor Table
CREATE TABLE doctor (
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    specialization TEXT,
    email TEXT
);

-- Patient Table
CREATE TABLE patient (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    dob TEXT,
    gender TEXT
);

-- Appointment Table
CREATE TABLE appointment (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_id INTEGER,
    patient_id INTEGER,
    app_date TEXT,
    app_time TEXT,

    FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id),
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id)
);
INSERT INTO doctor(name, specialization) VALUES ('Dr. Ravi', 'Cardiology');
INSERT INTO patient(name) VALUES ('Meghana');

INSERT INTO appointment(doctor_id, patient_id, app_date)
VALUES (1, 1, '2026-04-14');
-- Appointments of doctor
SELECT * FROM appointment WHERE doctor_id = 1;

-- Patient history
SELECT * FROM appointment WHERE patient_id = 1;

-- Count patients per doctor
SELECT doctor_id, COUNT(patient_id)
FROM appointment
GROUP BY doctor_id;