 <h1 align="center">🏃 Personal Fitness Tracker</h1>

<p align="center">
  A Python-Based Fitness Activity Tracking and Analysis System
</p>

---

## 📖 1. Project Overview

The Personal Fitness Tracker is a Python-based application that allows users to maintain a digital record of their physical activities.

It processes fitness data stored in a CSV file and provides meaningful insights into workout habits.

The application uses:
- **Pandas** and **NumPy** for data processing and numerical calculations.
- **Matplotlib** and **Seaborn** for data visualization.
- **CSV** for storing fitness activity records.

Users can record new activities, calculate fitness metrics, filter activity records, generate reports, visualize progress, and automatically save charts as PNG images.

## 🎯 2. Project Objectives

The main objectives of this project are:

1. **Fitness Activity Tracking:** Maintain structured records of daily workouts and physical activities.
2. **Data Management:** Read, update, and manage fitness records using CSV files.
3. **Data Cleaning:** Identify and remove invalid or incomplete records.
4. **Fitness Metric Calculation:** Calculate total activities, workout duration, calories burned, and average values.
5. **Activity Filtering:** Retrieve records by activity type or date range.
6. **Report Generation:** Generate summarized fitness reports.
7. **Data Visualization:** Represent fitness information through different graphical charts.
8. **Automatic Chart Saving:** Save generated visualizations as PNG images.
9. **Programming Skills Development:** Apply Python programming, data analysis, and visualization concepts.

## ✨ 3. Features

### 3.1 Log New Activity
- Record activity type.
- Enter workout duration in minutes.
- Enter calories burned.
- Automatically assign the current date.
- Save new records to the CSV file.

### 3.2 Calculate Fitness Metrics
- Calculate total recorded activities.
- Calculate total workout duration.
- Calculate total calories burned.
- Calculate average workout duration.
- Calculate average calories burned.

### 3.3 Filter Activities
- Filter records by activity type.
- Filter records by a specified date range.
- Display matching records in a readable table.

### 3.4 Generate Fitness Report
- Summarize fitness activity data.
- Display activity-wise information.
- Review workout duration and calories burned.

### 3.5 Visualize Progress
- Generate a bar chart for activity duration.
- Generate a line chart for daily calories burned.
- Generate a pie chart for activity distribution.
- Generate a heatmap for numerical correlation.
- Automatically save charts in the `Charts/` directory.

### 3.6 Show All Activities

Display all valid activity records available in the dataset.

### 3.7 Exit Application

Exit the application through the main menu.

## 🧰 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading, cleaning, filtering, and analysis |
| NumPy | Numerical calculations and statistics |
| Matplotlib | Bar, line, and pie charts |
| Seaborn | Heatmap visualization |
| CSV | Persistent storage of fitness records |

## 💻 5. System Requirements

- **Operating System:** Windows, Linux, or macOS
- **Python:** Python 3.10 or compatible Python 3 version
- **Code Editor:** Visual Studio Code, PyCharm, or any Python-compatible editor
- **Required Libraries:** Pandas, NumPy, Matplotlib, and Seaborn
- **Dataset:** `fitness_activities.csv`

## 📁 6. Project Structure

```text
Personal-Fitness-Tracker/
│
├── fitness_tracker.py
├── fitness_activities.csv
├── fitness_report.csv
├── weekly_report.csv
├── README.md
├── output.png
│
└── Charts/
    ├── bar_chart.png
    ├── line_chart.png
    ├── pie_chart.png
    └── heatmap.png
```

### File Descriptions

| File / Folder | Description |
|---|---|
| `fitness_tracker.py` | Main Python application |
| `fitness_activities.csv` | Stores fitness activity records |
| `fitness_report.csv` | Stores generated fitness reports |
| `weekly_report.csv` | Stores weekly fitness summaries |
| `README.md` | Project documentation |
| `output.png` | Output screenshot |
| `Charts/` | Stores generated chart images |

**Note:** Report files and chart images are generated when their respective application features are executed. The `Charts/` folder can be created automatically by the Python program.

## 🗂️ 7. Dataset Information

The application requires a CSV file named `fitness_activities.csv`.

### 7.1 Required Columns

| Column | Description | Example |
|---|---|---|
| Date | Date of the activity | 2026-10-20 |
| Activity Type | Type of physical activity | Running |
| Duration (Minutes) | Workout duration | 30 |
| Calories Burned | Calories burned | 300 |

### 7.2 Sample Dataset

```csv
Date,Activity Type,Duration (Minutes),Calories Burned
2026-10-20,Running,30,300
2026-10-21,Yoga,40,160
2026-10-22,Cycling,45,360
2026-10-23,Walking,35,140
2026-10-24,Running,25,260
```

These rows are examples. Users can replace them with their actual fitness data.

## 📦 8. Installation

### Step 1: Verify Python Installation

Open Command Prompt or the VS Code terminal.

```bash
python --version
```

### Step 2: Install Required Libraries

```bash
python -m pip install pandas numpy matplotlib seaborn
```

### Step 3: Verify the Dataset

Ensure that `fitness_activities.csv` contains all four required columns and is located in the project directory.

## ▶️ 9. How to Run the Project

1. Save the Python code as `fitness_tracker.py`.
2. Place the CSV dataset in the project directory.
3. Open the project folder in Visual Studio Code or a terminal.
4. Install all required libraries.
5. Run the following command:

```bash
python fitness_tracker.py
```

6. Select an option from the main menu.
7. Follow the instructions displayed in the terminal.

## ⚙️ 10. Application Modules

| Module | Description |
|---|---|
| Data Loading | Reads fitness records from the CSV file |
| Data Cleaning | Converts data types and removes invalid records |
| Activity Logging | Adds new fitness activities |
| Metrics Calculation | Calculates totals and averages |
| Activity Filtering | Filters records by activity type or date range |
| Report Generation | Generates summarized fitness information |
| Data Visualization | Generates charts using Matplotlib and Seaborn |
| Chart Saving | Saves chart images in the `Charts/` folder |
| Activity Display | Shows all available valid records |

## 📊 11. Charts and Visualizations

The Personal Fitness Tracker generates four different types of charts using Matplotlib and Seaborn to analyze and visualize fitness activities.

### 11.1 Bar Chart

**File:** `Charts/bar_chart.png`

**Purpose:**
- Compares total workout duration for different activity types.
- Helps identify which activity takes the most workout time.
- Displays activity-wise workout duration using vertical bars.

**Interpretation:**

The bar chart provides a clear comparison of workout duration across different physical activities such as Running, Walking, Yoga, and Cycling.

### 11.2 Line Chart

**File:** `Charts/line_chart.png`

**Purpose:**
- Displays daily calories burned over time.
- Shows changes in calorie-burning performance.
- Helps identify workout progress and daily activity patterns.

**Interpretation:**

The line chart connects daily calorie values to show how calorie expenditure changes over time. It helps users understand their fitness activity trends.

### 11.3 Pie Chart

**File:** `Charts/pie_chart.png`

**Purpose:**
- Displays the distribution of different activity types.
- Shows the percentage of each activity in the dataset.
- Helps identify the most frequently recorded activity.

**Interpretation:**

The pie chart represents each activity type as a separate slice. Larger slices indicate a higher proportion of recorded activities.

### 11.4 Heatmap

**File:** `Charts/heatmap.png`

**Purpose:**
- Displays the correlation between numerical fitness variables.
- Analyzes the relationship between workout duration and calories burned.
- Uses different colors to represent correlation values.

**Interpretation:**

The heatmap helps identify the strength and direction of relationships between numerical fitness measurements.

Correlation indicates an association between numerical variables; it does not prove causation.

### 11.5 Automatic Chart Saving

When the user selects **Visualize Progress**, the application generates the selected charts and saves them as PNG images in the `Charts/` directory.

**Generated Files:**

```text
Charts/
├── bar_chart.png
├── line_chart.png
├── pie_chart.png
└── heatmap.png
```

## 🧹 12. Data Validation and Cleaning

The application performs data validation to improve dataset reliability.

- Converts dates into a standard datetime format.
- Converts duration and calories into numeric values.
- Removes rows containing missing required values.
- Removes invalid dates and non-numeric measurements.
- Removes records with non-positive duration or calories.
- Rejects empty activity names when logging new activities.
- Rejects non-positive duration or calories entered by the user.

**Note:** Data cleaning may remove records from the in-memory dataset. The cleaned dataset is not necessarily written back to the CSV file unless the application explicitly saves it.

## 🛠️ 13. Troubleshooting

### Problem 1: CSV File Not Found

Place `fitness_activities.csv` in the correct project directory and verify the filename.

### Problem 2: Missing Required Columns

Check that the dataset contains all four required column names.

### Problem 3: Required Module Not Found

Install the dependencies:

```bash
python -m pip install pandas numpy matplotlib seaborn
```

### Problem 4: Charts Are Not Saving

- Select the chart visualization option.
- Verify that the chart-saving function is called.
- Check write permissions.
- Confirm that the `Charts/` folder exists.

### Problem 5: No Records Are Displayed

Check whether the CSV file contains valid records. Invalid or incomplete rows may be removed during data cleaning.

## 👩‍💻 14. Author

**Name:** Krisha Savaliya

**Project Title:** Personal Fitness Tracker

---

# 📤 15. Expected Output

The following examples illustrate the expected terminal output. Exact values depend on the contents of `fitness_activities.csv`.

### 15.1 Main Menu

```text
========================================
       PERSONAL FITNESS TRACKER
========================================
1. Log New Activity
2. Calculate Fitness Metrics
3. Filter Activities
4. Generate Fitness Report
5. Visualize Progress
6. Show All Activities
7. Exit

Enter your choice:
```

### 15.2 Calculate Fitness Metrics

For the five sample dataset rows:

```text
========== FITNESS METRICS ==========

Total Activities      : 5
Total Duration        : 175 Minutes
Total Calories Burned : 1220
Average Duration      : 35.0
Average Calories      : 244.0
```

### 15.3 Filter Activities by Type

Example: Selecting `Running`.

```text
========== FILTER ACTIVITIES ==========

1. Filter By Activity Type
2. Filter By Date Range
3. Go Back

Enter your choice: 1
Enter Activity Type: Running

Filtered Activities:

      Date Activity Type  Duration (Minutes)  Calories Burned
2026-10-20       Running                  30              300
2026-10-24       Running                  25              260
```

### 15.4 Generate Fitness Report

```text
========== FITNESS REPORT ==========

Total Activities      : 5
Total Duration        : 175
Total Calories Burned : 1220
```

### 15.5 Visualize Progress and Save Charts

```text
========== VISUALIZE PROGRESS ==========

1. Bar Chart
2. Line Chart
3. Pie Chart
4. Heatmap
5. Generate All Charts
6. Go Back

Enter your choice: 5

Generating All Charts...

All Charts Displayed and Saved Successfully!
Charts folder: Personal-Fitness-Tracker/Charts
```

### 15.6 Saved Chart Files

After successful chart generation:

```text
Charts/
├── bar_chart.png
├── line_chart.png
├── pie_chart.png
└── heatmap.png
```

### 15.7 Exit Application

```text
========================================
Thank You for Using Fitness Tracker!
Stay Healthy, Stay Fit!
Program Exited Successfully.
========================================
```

---

## 🎉 16. Conclusion

The Personal Fitness Tracker is a useful Python-based project that demonstrates practical applications of data management, data cleaning, numerical calculations, and data visualization.

It helps users maintain fitness records, analyze workout performance, generate reports, and visualize fitness progress through graphical representations.

**Stay Healthy, Stay Fit!** 🏃