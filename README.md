# 📧 Email Extractor Automation

A Python automation script developed as part of the **CodeAlpha Python Programming Internship**.

This project automatically scans a text file, extracts email addresses using a regular expression, removes duplicate email addresses, and saves the results into a separate text file.

## 🚀 Features

* Reads text from an input file
* Automatically detects email addresses
* Uses Regular Expressions (`re`)
* Removes duplicate email addresses
* Sorts extracted email addresses
* Saves results to an output file
* Handles missing files
* Handles unexpected errors
* Displays the number of emails extracted

## 🛠️ Technologies Used

* Python 3
* Regular Expressions (`re`)
* File Handling
* Functions
* Lists
* Sets
* Exception Handling

## 📁 Project Structure

```text
CodeAlpha_EmailExtractor/
│
├── main.py
├── input.txt
├── emails.txt
└── README.md
```

## ▶️ How to Run

### 1. Open the project in VS Code

Open the `CodeAlpha_EmailExtractor` folder.

### 2. Open the terminal

Go to:

**Terminal → New Terminal**

### 3. Run the program

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

## 💻 How It Works

The program reads all the content from `input.txt`.

It then uses a regular expression to identify email addresses.

The extracted emails are converted into a set to remove duplicates and then sorted alphabetically.

Finally, the unique email addresses are saved into `emails.txt`.

## 📄 Example Input

```text
Welcome to CodeAlpha Python Internship.

For technical support, contact support@codealpha.com.

You can contact John at john@gmail.com
or Priya at priya@yahoo.com.

For project-related queries:
project@codealpha.com
```

## 📄 Example Output

```text
admin@example.com
hr@example.com
john@gmail.com
priya@yahoo.com
project@codealpha.com
support@codealpha.com
```

## 🎯 Learning Objectives

This project demonstrates practical Python concepts including:

* File handling
* Regular expressions
* Functions
* Lists
* Sets
* Sorting
* Exception handling
* Automation
* Text processing

## 🏢 Internship

Developed as part of the **CodeAlpha Python Programming Internship**.

**Task:** Task Automation with Python Scripts

## 👨‍💻 Author

**Dasari Dinesh**

GitHub: https://github.com/ddasari217-ops/CodeAlpha_EmailExtractor

LinkedIn: https://github.com/ddasari217-ops/CodeAlpha_EmailExtractor
