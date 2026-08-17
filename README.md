# 📘 Python Exercises BA

This repository contains Python practice exercises and small programs for learning core programming concepts. Most of the material follows the chapter structure of Tony Gaddis' *Starting Out with Python*, with additional practice for data analysis using **pandas** and **matplotlib**.

The chapter exercises are generally small, standalone programs designed to practice one concept at a time. The `pd_exercises` directory is separate from the book chapters and contains notebook-based pandas exercises using the Titanic dataset.

---

## 📂 Repository Structure

```text
Python_Exercises_BA/
├── Chapter_02/                 # Variables, input/output, and calculations
├── Chapter_03/                 # Decision structures
├── Chapter_04/                 # Repetition structures and loops
├── Chapter_05/                 # Functions
├── Chapter_06/                 # Files and exceptions
│   ├── numbers.txt
│   └── random.txt
├── Chapter_07/                 # Lists and tuples
├── Chapter_08/                 # Strings and text-processing exercises
│   └── text.txt
├── Chapter_09/                 # Dictionaries and sets
│   ├── sample.txt
│   └── text.txt
├── pd_exercises/
│   ├── pd_exercises.ipynb      # pandas and matplotlib exercises
│   └── Titanic-Dataset.csv     # Dataset used by the notebook
├── requirements.txt
└── README.md
```

In addition to the numbered exercises, some chapter folders contain extra practice programs such as `compound_interest.py`, `average_steps_taken.py`, and data-processing examples.

---

## 🐼 Pandas Exercises

The `pd_exercises` directory contains additional data-analysis practice that is independent of the chapter exercises.

`pd_exercises.ipynb` loads `Titanic-Dataset.csv` and includes exercises covering topics such as:

- inspecting DataFrame rows, columns, and data types;
- filtering and sorting data;
- calculating minimum, maximum, mean, and mode values;
- grouping and aggregating data;
- querying DataFrames;
- creating charts with matplotlib.

Because the notebook reads `Titanic-Dataset.csv` using a relative path, keep the CSV file in the same directory as the notebook when running it.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/rtelesko/Python_Exercises_BA.git
cd Python_Exercises_BA
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Or on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

The requirements include packages used by exercises in the repository, including **pandas**, **matplotlib**, **SymPy**, and **deep-translator**. Many of the basic chapter exercises only use Python's standard library.

---

## ▶️ Running the Exercises

### Run a chapter exercise

From the project root:

```bash
python "Chapter_02/Exercise 2-1.py"
```

Or move into a chapter directory first:

```bash
cd Chapter_03
python "Exercise 3-5.py"
```

Some exercises use files stored in their chapter directory. For those programs, it is safest to run the script from that directory so relative file paths resolve correctly. For example:

```bash
cd Chapter_06
python "Exercise 6-1.py"
```

### Run the pandas notebook

Open `pd_exercises/pd_exercises.ipynb` in an environment with Jupyter notebook support, such as JupyterLab, Jupyter Notebook, or VS Code.

When starting Jupyter from the command line, you can work from the pandas exercise directory:

```bash
cd pd_exercises
jupyter notebook pd_exercises.ipynb
```

> Jupyter itself is not listed in `requirements.txt`, so install it separately if your development environment does not already provide notebook support.

---

## 🎯 Purpose

This repository is intended for:

- practicing Python fundamentals chapter by chapter;
- experimenting with short, focused programming exercises;
- reviewing examples involving files, collections, functions, and control flow;
- practicing introductory data analysis with pandas and matplotlib.

The programs are learning exercises rather than a single application, so files can usually be explored and run independently.

---

## 📖 Reference

- Tony Gaddis, *Starting Out with Python*, Pearson Education

---

## 🤝 Contributing

This repository is primarily intended for personal and educational use. Corrections, improvements, and additional practice exercises are welcome.

---

## 📝 License / Educational Use

The repository is intended for educational and personal learning purposes. Exercise solutions and examples should be used as study material alongside the original learning resources.
