#  Palindrome Checker using Pushdown Automaton (PDA)

## Project Overview

This project is a **Palindrome Checker** implemented using the concept of a **Pushdown Automaton (PDA)**. The application is built with **Flask (Python web framework)** and demonstrates how a PDA uses a **stack** to verify whether a given string is a palindrome.

The project is developed as part of an **Automata Theory** course to practically implement PDA behavior.

---

## Objective

* To understand and implement **Pushdown Automaton (PDA)** concepts
* To check whether a string is a **palindrome** using stack operations
* To apply automata theory concepts in a **real-world web application**

---

## Features

* Web-based interface using **Flask**
* PDA-based palindrome validation
* Uses **stack push and pop operations**
* Rejects strings shorter than **8 characters**
* Handles **even and odd length strings**
* Displays **Accepted / Rejected** messages with reasons

---

## How PDA Logic Works

1. The input string is divided into two halves.
2. The **first half** of the string is pushed onto a stack.
3. If the string length is odd, the middle character is skipped.
4. The **second half** is compared with stack elements by popping.
5. If all characters match and the stack is empty → **Accepted**
6. Otherwise → **Rejected**

This simulates a **Pushdown Automaton** using a stack.

---

## Technologies Used

* **Python**
* **Flask**
* **HTML (for frontend)**
* **Pushdown Automaton (PDA) concept**
* **Stack Data Structure**

---

## Project Structure

```
Palindrome-PDA/
│
├── app.py
├── templates/
│   └── index.html
└── README.md
```

---

## How to Run the Project

1. Install Flask:

```bash
pip install flask
```

2. Run the application:

```bash
python app.py
```

3. Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## Example

**Input:**

```
abccbaab
```

**Output:**

```
Accepted: This string is a palindrome according to PDA rules.
```

---

## Automata Theory Concepts Used

* Pushdown Automaton (PDA)
* Stack operations
* Palindrome language recognition
* Deterministic behavior simulation


