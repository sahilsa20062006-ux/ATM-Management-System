# ATM Management System

A command-line ATM Management System built entirely in Python. This project was developed to practice and solidify core Object-Oriented Programming (OOP) concepts, specifically focusing on encapsulation, state management, and user input validation.

## Features

* **PIN Management:** Securely create and change a 4-digit PIN.
* **Balance Inquiry:** Check current account balance securely.
* **Cash Withdrawal:** Withdraw funds with built-in balance and validation checks.
* **Cash Deposit:** Add funds to the account seamlessly.
* **Transaction History:** View a log of all deposits and withdrawals made during the session.

## Technologies Used

* **Language:** Python 3.x
* **Concepts:** Object-Oriented Programming (Classes, Objects, Methods, Encapsulation, Private Attributes)

## Key Learnings

Building this application reinforced several foundational programming principles:
* Implementing private variables (`__pin`, `__balance`, `__transactions`) to prevent unintended external modification.
* Utilizing `try-except` blocks and string methods (`.isdigit()`) to handle unexpected user inputs without crashing the application.
* Designing a continuous, user-friendly interactive terminal menu.
