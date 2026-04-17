# Pandas

## 📌 What is Pandas?

Pandas is a **Python library** used for **data manipulation and analysis**. It provides fast, flexible, and easy-to-use data structures for working with structured data.

Pandas is mainly used for:

* Data cleaning
* Data analysis
* Data transformation
* Handling missing values
* Working with CSV/Excel/JSON files

---

# Key Features of Pandas

* Fast and efficient data handling
* Built-in data structures
* Handles missing data
* Data alignment and indexing
* Grouping and aggregation
* File input/output support
* Time series functionality

---

# Core Data Structures

## 1. Series

A **one-dimensional labeled array**.

Example structure:

```
0   10
1   20
2   30
```

Features:

* Single column
* Has index
* Can store any data type

---

## 2. DataFrame

A **two-dimensional labeled data structure** (rows and columns).

Example:

```
Name    Age
A       20
B       25
C       30
```

Features:

* Multiple columns
* Different data types
* Most commonly used structure

---

# Pandas Import

```
import pandas as pd
```

---

# Creating Data Structures

### Series

* From list
* From dictionary
* From array

### DataFrame

* From dictionary
* From list of lists
* From CSV file
* From Excel file

---

# Reading Data

Pandas can read:

* CSV
* Excel
* JSON
* SQL
* Text files

Common methods:

```
read_csv()
read_excel()
read_json()
```

---

# Writing Data

Pandas can write data to:

* CSV
* Excel
* JSON

Methods:

```
to_csv()
to_excel()
to_json()
```

---

# Data Inspection

Used to understand dataset:

* head() → first rows
* tail() → last rows
* info() → dataset info
* describe() → statistics
* shape → rows & columns
* columns → column names

---

# Selecting Data

Selection methods:

* Single column
* Multiple columns
* Rows using index
* Rows using condition

Indexing methods:

* loc → label based
* iloc → index based

---

# Data Cleaning

Pandas helps in cleaning data:

Handling missing values:

* dropna()
* fillna()

Removing duplicates:

* drop_duplicates()

Renaming columns:

* rename()

Changing data type:

* astype()

---

# Filtering Data

Filtering using conditions:

* Equal
* Greater than
* Less than
* Multiple conditions

Used for selecting specific rows.

---

# Sorting Data

Sorting methods:

* sort_values()
* sort_index()

Sorting can be:

* Ascending
* Descending

---

# Grouping Data

Grouping is used to summarize data.

Method:

```
groupby()
```

Operations:

* sum()
* mean()
* count()
* min()
* max()

---

# Merging Data

Combining datasets:

* merge()
* concat()
* join()

Used for combining multiple DataFrames.

---

# Handling Columns

Column operations:

* Add column
* Delete column
* Rename column
* Modify column

---

# Indexing

Index represents row labels.

Operations:

* set_index()
* reset_index()
* rename index

---

# Pandas vs NumPy

| Feature        | Pandas        | NumPy               |
| -------------- | ------------- | ------------------- |
| Data type      | Table         | Array               |
| Structure      | DataFrame     | ndarray             |
| Use            | Data analysis | Numerical computing |
| Missing values | Supported     | Limited             |

---

# Advantages of Pandas

* Easy data manipulation
* Works with large datasets
* Powerful grouping
* Flexible indexing
* File handling support
* Integrates with NumPy & Matplotlib

---

# Applications

Pandas is used in:

* Data Science
* Machine Learning
* Data Analysis
* Data Cleaning
* Financial analysis
* Business analytics

---

# Summary

Pandas is a powerful Python library used for **data analysis and manipulation**.
It provides **Series** and **DataFrame** as core structures and supports data cleaning, filtering, grouping, merging, and file handling.
