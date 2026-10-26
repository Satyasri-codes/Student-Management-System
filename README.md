# Student Management System

A Python-based Student Management System that helps manage student records through a simple menu-driven interface.

## Features

- Add new students
- View all student records
- Search students by roll number, name, or branch
- Update student details
- Delete student records with confirmation
- Validate user input and prevent duplicate roll numbers
- Store student records in a text file
- Load valid records when the program starts
- Display total students, average age, oldest and youngest age, and branch-wise student count
- Handle invalid inputs and missing files

## Technologies Used

- Python
- Lists and Dictionaries
- Functions and Loops
- Exception Handling
- File Handling
- Input Validation

## Project Files

- `student_management2.py` — Main Python program
- `students.txt` — Stores student records
- `README.md` — Project documentation

## How to Run

1. Install Python.
2. Download or clone this repository.
3. Open the project folder in VS Code or a terminal.
4. Run:

   ```bash
   python student_management2.py
   ```

5. Choose an option from the menu and follow the prompts.

## Student Record Format

Each student record is stored on a separate line in `students.txt`:

`roll_number,name,age,branch`

Example:

`130,ravi,20,cse`

## Validation

The program checks roll numbers, names, ages, and branches. Invalid records and duplicate roll numbers found while loading the file are skipped.

## Learning Outcomes

This project demonstrates practical Python programming, data validation, file persistence, and basic CRUD operations (Create, Read, Update, Delete).
