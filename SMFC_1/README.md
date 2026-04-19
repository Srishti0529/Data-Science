# JSON Social Network Viewer 

## 📌 Project Description

This Python program reads data from a **JSON file** and displays **users, their friends, and liked pages**.
It simulates a small **social network** where users are connected and follow different pages.

The program:

* Loads JSON data from file
* Reads users and pages
* Displays user connections
* Displays liked pages

---

# 📁 Files Used

```
project
│
├── app.py
└── codebook_data.json
```

---

# 📄 JSON Data Structure

The JSON file contains two sections:

### 1. users

Each user has:

* id → unique user ID
* name → user name
* friends → list of friend IDs
* liked_pages → pages liked by user

Example:

```
{
"id": 1,
"name": "Amit",
"friends": [2,3],
"liked_pages": [101]
}
```

---

### 2. pages

Each page has:

* id → page ID
* name → page name

Example:

```
{
"id":101,
"name":"Python Developers"
}
```

---

# ⚙️ Functions

## 1. load_data(filename)

Purpose:
Loads JSON data from file.

Working:

* Opens file
* Reads JSON
* Converts to Python dictionary
* Returns data

---

## 2. display_users(data)

Purpose:
Displays users and their connections.

Shows:

* User name
* User ID
* Friends list
* Liked pages
* Page details

---

# 🔄 Program Flow

1. Load JSON file
2. Store data in variable
3. Display users
4. Display pages

Flow:

```
Load JSON → Parse Data → Display Users → Display Pages
```

---

# ▶️ How to Run

Step 1: Save JSON file as

```
codebook_data.json
```

Step 2: Run program

```
python app.py
```

---

# 📤 Output Example

```
Users and Their Connections:

Amit (ID: 1) - Friends: [2, 3] - Liked Pages: [101]
Priya (ID: 2) - Friends: [1, 4] - Liked Pages: [102]
Rahul (ID: 3) - Friends: [1] - Liked Pages: [101, 103]
Sara (ID: 4) - Friends: [2] - Liked Pages: [104]

Pages:

101: Python Developers
102: Data Science Enthusiasts
103: AI & ML Community
104: Web Dev Hub
```

---

# 🎯 Concepts Used

* JSON handling
* File handling
* Python dictionary
* Functions
* Loops
* Data parsing
* Nested data structures

---

# 🧠 What This Project Demonstrates

* Reading JSON file
* Accessing nested data
* Displaying structured output
* Simulating social network data
* Working with lists inside dictionaries

---

# ✅ Conclusion

This program demonstrates how to **load and process JSON data** in Python.
It reads users and pages from a JSON file and displays their **connections and liked pages**, simulating a basic social networking structure.
