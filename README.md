# ELEVATE-LABS-INTERNSHIP
# 📊 Netflix Data Analysis Project

This project is part of the **Elevate Labs Data Analyst Internship** and focuses on analyzing Netflix titles using Python and pandas. It includes two major tasks: **Data Cleaning & Preprocessing** and **Exploratory Data Analysis (EDA)**.

---

## 🧩 Task 1 - Data Cleaning and Preprocessing

### 🎯 Objective
Clean and prepare a raw dataset using Python (Pandas) by handling nulls, duplicates, and inconsistent formats.

### 🧹 Steps Performed
- Removed duplicate entries
- Filled missing values in `director`, `cast`, and `country`
- Dropped rows with missing values in `title` and `type`
- Converted `date_added` to datetime format
- Renamed columns to lowercase with underscores
- Standardized inconsistent values in `country`, `rating`, and `type`
- Cleaned and exported to `netflix_cleaned.csv`

### 🛠 Tools Used
- Python 3
- Pandas library

---

## 📊 Task 2 - Exploratory Data Analysis (EDA)

### 🎯 Objective
Uncover insights about Netflix’s content library using visualizations and data analysis techniques.

### 📈 Visualizations & Insights
- ✅ Distribution of Movies vs TV Shows
- 🌍 Top 10 countries contributing the most content
- 📅 Number of shows added per year
- 🎭 Top 10 most common genres
- ⏱️ Duration breakdown between minutes and seasons

### 📊 Charts Used
- Count Plots (`seaborn.countplot`)
- Bar Charts (`matplotlib.pyplot`, `seaborn.barplot`)

### 📦 Libraries Used
- pandas
- matplotlib
- seaborn
- collections (Counter)

---

