# Instagram Data Parsing & Analysis

## Overview

This project parses **raw Instagram-style text data**, converts it into **structured JSON**, and performs **basic data analysis** such as:

* User with maximum posts
* User with maximum followers
* Count of page categories

---

## Project Structure

```
DATA_SCIENCE/
│
├── COB/
│   ├── initialdata.txt      # Raw scraped data
│   ├── finaldata.txt        # Cleaned raw data
│   ├── Parsing_data.py      # Convert text → JSON
│   ├── Q_A.py               # Analysis on JSON data
│   ├── s.json               # Generated structured dataset
│
└── README.md
```

---

## Step 1 — Parsing Raw Data

`Parsing_data.py`:

* Reads `finaldata.txt`
* Splits profile blocks
* Extracts:

  * username
  * posts
  * followers
  * following
  * name
  * type_of_page
  * bio
* Converts to dictionary
* Saves to `s.json`

Run:

```bash
python Parsing_data.py
```

Output:

```
s.json
```

---

## Step 2 — Data Analysis

`Q_A.py` performs:

### 1. Maximum Posts

Finds user with highest posts

### 2. Maximum Followers

Finds most followed account

### 3. Category Count

Finds:

* unique page types
* number of categories

Run:

```bash
python Q_A.py
```

---

## Example Output

```
User with maximum posts:
{...}

User with maximum followers:
{...}

All type of categories:
{'Media', 'Community', 'Developer'}

Total categories:
12
```

---

## Data Format (JSON)

Each record:

```json
{
  "username": "",
  "no_of_posts": 0,
  "no_of_followers": 0,
  "no_of_following": 0,
  "name": "",
  "type_of_page": "",
  "bio": ""
}
```

---

## Features

* Text → Structured JSON
* Handles K / M followers
* Supports emojis
* Category extraction
* Max value analysis

---

## Requirements

* Python 3.x
* json (built-in)

---

## How It Works

Raw Text → Parse → Dictionary → JSON → Analysis

---

## Use Cases

* Instagram data analysis
* Social media insights
* Data science practice
* Text parsing project

---
