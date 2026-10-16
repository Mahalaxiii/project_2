Project 3: Bank Account Management System - README
Overview
The Bank Account Management System is a robust command-line application developed in Python as part of the Machine Learning training curriculum minor projects. It simulates core banking operations, allowing users to securely manage accounts, execute deposits and withdrawals, check balances, track transaction histories, and persist records across sessions.

Main Features Implemented
Create Account: Register new bank accounts with unique account holder details, account numbers, and initial deposits.

Deposit Money: Add funds securely to a specified account with transaction validation and error handling for invalid amounts.

Withdraw Money: Withdraw funds while ensuring sufficient balance availability and preventing overdrafts.

Check Balance: Real-time retrieval and display of current account balances.

Maintain Transaction History: Comprehensive logging of all deposits and withdrawals with timestamps.

Data Persistence: Automatically saves and loads account records and transaction logs to ensure data integrity across program runs.

Classes Used
Following object-oriented programming (OOP) principles, the project implements the following core classes:

Account (Base Class): Encapsulates core account attributes (account_number, holder_name, balance) and provides shared methods for depositing, withdrawing, and checking balances.

SavingsAccount (Derived Class): Inherits from Account and implements specific rules or interest calculations relevant to savings accounts.

Transaction (Helper Class): Represents individual transaction records, storing details such as transaction type, amount, and timestamp.

BankSystem (Management Class): Manages the collection of accounts, handles user interactions, orchestrates menu navigation, and handles file reading and writing for data persistence.

How the Project Works
Initialization: Upon launching, the application loads existing account data from stored text or CSV files into memory.

Menu-Driven Interface: The program presents an interactive console menu where users can select operations such as creating an account, depositing money, withdrawing money, checking balances, or viewing transaction histories.

Validation & Exception Handling: User inputs are validated to catch invalid entries (such as string inputs for numeric amounts or selecting non-existent account numbers). Custom exception handling ensures smooth execution without crashing.

Persistence: Every successful transaction or new account creation updates the internal records and saves the updated state to persistent storage files.

How to Run the Project
Prerequisites
Python 3.8 or higher installed on your system.

Standard Python libraries (no external dependencies required).

Execution Steps
Clone the repository or download all project files into a local directory.

Open your terminal or command prompt and navigate to the project root directory:

Bash
cd bank-account-management-system
Run the main application script:

Bash
python main.py
Follow the on-screen prompts in the interactive console to test and operate the system.
