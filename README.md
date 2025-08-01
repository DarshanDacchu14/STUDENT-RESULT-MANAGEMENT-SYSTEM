# STUDENT-RESULT-MANAGEMENT-SYSTEM
As an alternative to traditional paper-based result systems, we developed a Student Result Management System (SRMS) — a web-based application designed to allow students to conveniently access their academic results online.
The application is built using Python with the Flask web framework and utilizes SQLite, a lightweight file-based database, to manage and store student details and result data.

How SRMS Works:
When students access the website, they are first directed to a login page where they must provide:
 • Their USN (University Seat Number) as the login ID,
 • Their Date of Birth as the password,
 • A CAPTCHA code to ensure human verification.

Upon successful authentication, students are presented with their academic results, including:
 • Subject-wise marks,
 • Breakdown of internal and external scores,
 • Total marks,
 • Corresponding grades.

Technical Stack:
 • Frontend: Developed using HTML, CSS, and Bootstrap to create a responsive and user-friendly interface.
 • Backend: Powered by Python with Flask, which handles server-side operations.
 • Database: Data is stored securely using SQLite, a simple yet effective database system.
 • Security Features: Added layers of security through CAPTCHA validation and Date of Birth verification during login.
