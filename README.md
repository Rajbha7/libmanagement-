# 📚 Library Management System (Python)

A modular, desktop-based **Library Management System** built strictly in Python. The system handles book inventories, student member profiles, borrow and return transaction workflows, and provides graphical data visualizations of student interests across literary categories using scientific and analytical Python libraries.

---

## 📌 Project Overview

This mini project serves as an end-to-end institutional library management solution featuring:
- **Books Cataloging:** Track book titles, authors, categories, ISBNs, and real-time inventory availability.
- **Students Management:** Maintain records of registered student members and their borrowing histories.
- **Borrow & Return Tracking:** Log checkouts, expected return dates, actual return dates, and return statuses.
- **Student Interest Analytics:** Analyze reading patterns and category popularity (e.g., Science, Technology, Fiction, History) using statistical summaries and visual charts.
- **Interactive Visuals & Desktop GUI:** User-friendly Tkinter-based control panel complemented by an animated Turtle graphics splash screen.

---

## 🛠️ Technology Stack & Libraries

The project is built entirely in **Python** and leverages the following core libraries:

| Library | Role in Project |
| :--- | :--- |
| **`tkinter`** | Primary Graphical User Interface (GUI) for desktop screens, dashboards, forms, and record tables. |
| **`turtle`** | Vector-graphics animated splash screen and visual library logo greeting users upon application launch. |
| **`pandas`** | Tabular data manipulation, CSV read/write operations, merging records, and category-level aggregation. |
| **`numpy`** | Numerical computing, statistical calculations (percentages, durations, distribution metrics, arrays). |
| **`matplotlib`** | Data visualization engine for plotting category interest bar charts, pie charts, and borrowing trends. |

---

## 📂 Project Folder Structure

```text
library-management-system/
│
├── assets/                         # Application branding and media
│   └── images/                     # UI icons and logo imagery
│
├── data/                           # Persistent flat-file storage (CSV datasets)
│   ├── books.csv                   # Book records (ID, Title, Author, Category, Copies)
│   ├── students.csv                # Student records (ID, Name, Dept, Contact)
│   └── borrow_records.csv          # Issue & Return transaction logs
│
├── exports/                        # Directory for exported charts and summary reports
│
├── src/                            # Application source code
│   ├── analytics/                  # Data processing & visualization logic
│   │   ├── __init__.py
│   │   ├── chart_generator.py      # Matplotlib visual plot generators
│   │   └── data_processor.py       # Pandas and NumPy aggregation & calculation functions
│   │
│   ├── gui/                        # Tkinter graphical interface components
│   │   ├── __init__.py
│   │   ├── analytics_view.py       # Visual dashboard view for interest charts
│   │   ├── book_view.py            # Book catalog interface (Add, Search, Update, Delete)
│   │   ├── main_window.py          # Central navigation window and action menu
│   │   ├── student_view.py         # Student directory interface (Register, Edit, View)
│   │   └── transaction_view.py     # Issue (Borrow) and Return processing forms
│   │
│   ├── models/                     # Core business logic and storage handlers
│   │   ├── __init__.py
│   │   ├── book_manager.py         # Book CRUD logic & stock checks
│   │   ├── borrow_manager.py       # Borrow/Return validation & transaction handler
│   │   └── student_manager.py      # Student profile CRUD logic
│   │
│   ├── splash/                     # Animated introductory screens
│   │   ├── __init__.py
│   │   └── turtle_splash.py        # Turtle-based animated opening screen
│   │
│   └── __init__.py
│
├── main.py                         # Application main entry point
├── requirements.txt                # Python package dependencies
└── README.md                       # Project documentation & execution guide
```

---

## 📊 Data Schema Specifications

The project maintains data in three relational CSV datasets within the `data/` directory:

### 1. `books.csv`
- `book_id` *(int / string)*: Unique identifier for each book title.
- `title` *(string)*: Name of the book.
- `author` *(string)*: Author(s) of the book.
- `category` *(string)*: Genre or academic category (e.g., *Computer Science, Mathematics, Fiction, History, Physics*).
- `total_copies` *(int)*: Total quantity owned by the library.
- `available_copies` *(int)*: Current quantity on shelf ready for checkout.

### 2. `students.csv`
- `student_id` *(string)*: Unique student roll number or institutional ID.
- `name` *(string)*: Full student name.
- `department` *(string)*: Academic department (e.g., *CSE, Mechanical, Arts, Business*).
- `email` *(string)*: Student contact email.
- `phone` *(string)*: Contact phone number.

### 3. `borrow_records.csv`
- `record_id` *(int / string)*: Unique transaction identifier.
- `student_id` *(string)*: Foreign key referencing `students.csv`.
- `book_id` *(string)*: Foreign key referencing `books.csv`.
- `borrow_date` *(YYYY-MM-DD)*: Date the book was issued.
- `due_date` *(YYYY-MM-DD)*: Scheduled return deadline.
- `return_date` *(YYYY-MM-DD / empty)*: Date returned (or left empty if currently borrowed).
- `status` *(string)*: Current state (`BORROWED` or `RETURNED`).

---

## 📈 Analytical Charts & Visualizations

The analytics module (`chart_generator.py`) generates insightful visualizations using **Matplotlib**:
1. **Category Popularity Breakdown:**
   - **Pie Chart / Donut Chart:** Percentage share of total checkouts distributed across categories (e.g., 40% Computer Science, 25% Fiction, 20% Mathematics, 15% History).
2. **Student Department vs. Category Preferences:**
   - **Grouped Bar Chart:** Demonstrates which student departments borrow which genres of books.
3. **Borrow vs. Return Activity:**
   - **Bar Plot / Line Trend:** Visualizes active borrowings versus timely returns.

---

## 🚀 Setup & Execution Guide

### 1. Prerequisites
- **Python 3.8+** installed on your system.
- Standard libraries `tkinter` and `turtle` are packaged with official Python distributions on Windows/macOS.

### 2. Installation of Dependencies
Clone or download the project workspace, open a terminal in the project root, and install the required external libraries:

```bash
pip install pandas numpy matplotlib
```

*(Alternatively, via `requirements.txt`: `pip install -r requirements.txt`)*

### 3. Running the Project
Once implementation files are coded, launch the project using:

```bash
python main.py
```

### 4. Operational Flow
1. **Splash Screen:** `turtle_splash.py` opens with an animated vector logo and welcoming typography.
2. **Main Dashboard:** `main_window.py` displays the primary GUI with navigation buttons.
3. **Data Operations:** Users can manage books, register students, and record borrow/return actions.
4. **Analytics View:** Generates real-time charts based on the latest records in the CSV files.

---

## 🔒 Current Phase

> **Phase 1 Complete:** Folder structure and system documentation established.
> **Status:** Architecture defined. Implementation of source code modules will commence upon approval.

