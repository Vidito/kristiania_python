# 🏦 Task 3: Bank Account Management System (Python)

## 📌 Task
Implement a **Bank Account Management System** in Python.

---

## 📂 Classes and Methods

### 1. `Menu` Class
- **Property**
  - `options`: A list containing all the menu options.
- **Methods**
  - `__init__()` → Initializes the list of menu options.
  - `add_option()` → Adds an option to the menu.
  - `get_input()` → Displays the menu and gets the user’s choice.

---

### 2. `BankAccount` Class
- **Property**
  - `balance`: Represents the account balance.
- **Methods**
  - `__init__()` → Initializes the balance.
  - `deposit()` → Deposits money into the account.
  - `withdraw()` → Withdraws money from the account.
  - `add_interest()` → Adds interest to the current balance.
  - `get_balance()` → Returns the current balance.

---

## 📋 Menu Layout
Your program’s menu should appear as follows:

- **1 Open a new account** 
- **2 Deposit money into your account**
- **3 Withdraw money from your account** 
- **4 Add interests to your account** 
- **5 Get the current balance of your account** 
- **6 Quit**
