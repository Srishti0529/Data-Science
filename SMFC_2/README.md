# JSON Data Cleaning Program

## 📌 Project Description

This Python program **cleans social network data stored in a JSON file**.
It removes invalid users, duplicate entries, and inactive records, then saves the cleaned data into a new JSON file.

The program performs **data cleaning operations** such as:

* Removing users with missing names
* Removing duplicate friends
* Removing inactive users
* Removing duplicate pages
* Saving cleaned data to a new file

---

# 📁 Files Used

```text
project
│
├── codebook.json
├── cleaned_codebook_data.json
└── app .py
```

---

# 📄 Input JSON Structure

The JSON file contains:

### Users

Each user has:

* id → unique ID
* name → user name
* friends → list of friend IDs
* liked_pages → list of liked pages

### Pages

Each page has:

* id → page ID
* name → page name

---

# ⚙️ Function: clean_data(data)

This function cleans the JSON data.

## 1. Remove Users with Missing Names

Users having empty names are removed.

Example removed:

```text
{ "id": 3, "name": "", "friends": [1], "liked_pages": [101, 103] }
```

---

## 2. Remove Duplicate Friends

Duplicate friend IDs are removed.

Example:

```text
Before: [2, 2]
After : [2]
```

---

## 3. Remove Inactive Users

Users having:

* no friends
* no liked pages

are removed.

Example removed:

```text
{ "id": 5, "name": "Amit", "friends": [], "liked_pages": [] }
```

---

## 4. Remove Duplicate Pages

Duplicate page IDs are removed.

Example:

```text
{ "id": 104, "name": "Web Dev Hub" }
{ "id": 104, "name": "Web Development" }
```

Only one is kept.

---

# 🔄 Program Flow

```text
Load JSON → Clean Users → Remove Duplicates → Remove Inactive → Save Cleaned JSON
```

---

# ▶️ How to Run

Step 1: Place input file

```text
codebook.json
```

Step 2: Run program

```bash
python main.py
```

---

# 📤 Output

Program creates a new file:

```text
cleaned_codebook_data.json
```

Console output:

```text
Data cleaned successfully!
```

---

# 🧠 Concepts Used

* JSON handling
* File handling
* Data cleaning
* List comprehension
* Dictionary usage
* Removing duplicates
* Filtering data

---

# 🎯 Cleaning Operations Summary

| Operation                | Description           |
| ------------------------ | --------------------- |
| Remove empty names       | Deletes invalid users |
| Remove duplicate friends | Unique friend IDs     |
| Remove inactive users    | No friends & pages    |
| Remove duplicate pages   | Unique page IDs       |

---

# ✅ Final Result

The cleaned JSON file contains:

* Valid users only
* Unique friend lists
* No inactive users
* No duplicate pages

This program demonstrates **real-world JSON data cleaning using Python**.
