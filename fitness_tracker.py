
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ==========================================
#          FITNESS TRACKER CLASS
# ==========================================

class FitnessTracker:

    def __init__(self):
        
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

        
        self.file = os.path.join(
            self.base_dir, "fitness_activities.csv"
        )
        self.chart_folder = os.path.join(
            self.base_dir, "Charts"
        )
        self.report_file = os.path.join(
            self.base_dir, "fitness_report.csv"
        )
        self.weekly_report_file = os.path.join(
            self.base_dir, "weekly_report.csv"
        )

        
        os.makedirs(self.chart_folder, exist_ok=True)

        try:
            self.data = pd.read_csv(self.file)
            self.clean_data()

            print("\nCSV File Loaded Successfully!")
            print(f"Charts Folder: {self.chart_folder}")

        except FileNotFoundError:
            print("\nError: fitness_activities.csv file not found!")
            print(f"Expected location: {self.file}")
            raise SystemExit

    # ======================================
    # CLEAN DATA
    # ======================================

    def clean_data(self):
        required_columns = [
            "Date",
            "Activity Type",
            "Duration (Minutes)",
            "Calories Burned"
        ]

        missing = [
            col for col in required_columns
            if col not in self.data.columns
        ]

        if missing:
            raise ValueError(
                f"Missing required CSV columns: {missing}"
            )

        self.data["Date"] = pd.to_datetime(
            self.data["Date"], errors="coerce"
        )

        self.data["Duration (Minutes)"] = pd.to_numeric(
            self.data["Duration (Minutes)"],
            errors="coerce"
        )

        self.data["Calories Burned"] = pd.to_numeric(
            self.data["Calories Burned"],
            errors="coerce"
        )

        self.data.dropna(
            subset=required_columns,
            inplace=True
        )

        self.data = self.data[
            (self.data["Duration (Minutes)"] > 0) &
            (self.data["Calories Burned"] > 0)
        ]

        self.data.reset_index(drop=True, inplace=True)

    # ======================================
    # SAVE DATA
    # ======================================

    def save_data(self):
        self.data.to_csv(
            self.file,
            index=False,
            date_format="%Y-%m-%d"
        )

    # ======================================
    # 1. LOG NEW ACTIVITY
    # ======================================

    def log_activity(self):
        print("\n========== LOG NEW ACTIVITY ==========")

        activity = input("Enter Activity Type: ").strip()

        try:
            duration = float(
                input("Enter Duration (Minutes): ")
            )

            calories = float(
                input("Enter Calories Burned: ")
            )

            if not activity:
                print("Activity Type cannot be empty!")
                return

            if duration <= 0 or calories <= 0:
                print(
                    "Duration and Calories must be positive!"
                )
                return

            new_activity = {
                "Date": pd.Timestamp.today().normalize(),
                "Activity Type": activity.title(),
                "Duration (Minutes)": duration,
                "Calories Burned": calories
            }

            self.data.loc[len(self.data)] = new_activity

            self.save_data()

            print("\nActivity Added Successfully!")
            print("CSV File Updated Successfully!")

        except ValueError:
            print("Please Enter Valid Numbers!")

    # ======================================
    # 2. CALCULATE FITNESS METRICS
    # ======================================

    def calculate_metrics(self):
        print("\n========== FITNESS METRICS ==========")

        if self.data.empty:
            print("No Data Available!")
            return

        duration = np.array(
            self.data["Duration (Minutes)"]
        )

        calories = np.array(
            self.data["Calories Burned"]
        )

        print("\nTotal Activities      :", len(self.data))
        print(
            "Total Duration        :",
            round(np.sum(duration), 2),
            "Minutes"
        )
        print(
            "Total Calories Burned :",
            round(np.sum(calories), 2)
        )
        print(
            "Average Duration      :",
            round(np.mean(duration), 2)
        )
        print(
            "Average Calories      :",
            round(np.mean(calories), 2)
        )

        total_duration = np.sum(duration)
        total_calories = np.sum(calories)

        print(
            "Calories Per Minute   :",
            round(total_calories / total_duration, 2)
        )

        daily = (
            self.data.groupby("Date")["Calories Burned"]
            .sum()
            .sort_index()
        )

        if len(daily) >= 2 and daily.iloc[0] != 0:
            improvement = (
                (daily.iloc[-1] - daily.iloc[0])
                / daily.iloc[0]
            ) * 100

            print(
                "Percentage Improvement:",
                round(improvement, 2),
                "%"
            )

        print("\nActivity Frequency:")
        print(self.data["Activity Type"].value_counts())

    # ======================================
    # 3. FILTER ACTIVITIES
    # ======================================

    def filter_activities(self):
        print("\n========== FILTER ACTIVITIES ==========")
        print("1. Filter By Activity Type")
        print("2. Filter By Date Range")
        print("3. Go Back")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            activity = input(
                "Enter Activity Type: "
            ).strip()

            result = self.data[
                self.data["Activity Type"].str.lower()
                == activity.lower()
            ]

            print("\nFiltered Activities:")

            if result.empty:
                print("No matching activities found!")
            else:
                print(result.to_string(index=False))

        elif choice == "2":
            try:
                start = pd.to_datetime(
                    input("Enter Start Date (YYYY-MM-DD): ")
                ).normalize()

                end = pd.to_datetime(
                    input("Enter End Date (YYYY-MM-DD): ")
                ).normalize()

                if start > end:
                    print(
                        "Start Date cannot be after End Date!"
                    )
                    return

                result = self.data[
                    (self.data["Date"] >= start) &
                    (
                        self.data["Date"]
                        < end + pd.Timedelta(days=1)
                    )
                ]

                print("\nFiltered Activities:")

                if result.empty:
                    print(
                        "No activities found in this date range!"
                    )
                else:
                    print(result.to_string(index=False))

            except (ValueError, TypeError):
                print("Invalid Date Format!")

        elif choice == "3":
            return

        else:
            print("Invalid Choice!")

    # ======================================
    # 4. GENERATE FITNESS REPORT
    # ======================================

    def generate_report(self):
        print("\n========== FITNESS REPORT ==========")

        if self.data.empty:
            print("No Data Available!")
            return

        report = self.data.groupby("Activity Type").agg(
            Total_Activities=("Activity Type", "count"),
            Total_Duration=("Duration (Minutes)", "sum"),
            Total_Calories=("Calories Burned", "sum")
        ).reset_index()

        print("\nActivity Wise Report:")
        print(report.to_string(index=False))

        weekly = self.data.copy()

        weekly["Week"] = (
            weekly["Date"].dt.to_period("W").astype(str)
        )

        weekly_report = weekly.groupby("Week").agg(
            Total_Activities=("Activity Type", "count"),
            Total_Duration=("Duration (Minutes)", "sum"),
            Total_Calories=("Calories Burned", "sum")
        ).reset_index()

        print("\nWeekly Fitness Report:")
        print(weekly_report.to_string(index=False))

        report.to_csv(
            self.report_file,
            index=False
        )

        weekly_report.to_csv(
            self.weekly_report_file,
            index=False
        )

        print("\nReports Saved Successfully!")
        print(f"1. {self.report_file}")
        print(f"2. {self.weekly_report_file}")

    # ======================================
    # HELPER: SAVE AND SHOW CHART
    # ======================================

    def save_and_show_chart(self, filename):
        path = os.path.join(
            self.chart_folder, filename
        )

        try:
            plt.tight_layout()

            # Save chart before displaying it
            plt.savefig(
                path,
                dpi=300,
                bbox_inches="tight"
            )

            print("\nChart Saved Successfully!")
            print(f"Location: {path}")

            plt.show()

        except Exception as error:
            print(f"Error saving chart: {error}")

        finally:
            plt.close()

    # ======================================
    # 5. VISUALIZE PROGRESS
    # ======================================

    def visualize_progress(self):
        if self.data.empty:
            print("No Data Available!")
            return

        while True:
            print("\n========== CHART MENU ==========")
            print("1. Bar Chart")
            print("2. Line Graph")
            print("3. Pie Chart")
            print("4. Heatmap")
            print("5. Generate All Charts")
            print("6. Go Back")

            choice = input(
                "\nWhich Chart Do You Want To Generate? "
            )

            # ----------------------------------
            # BAR CHART
            # ----------------------------------

            if choice == "1":
                chart = self.data.groupby(
                    "Activity Type"
                )["Duration (Minutes)"].sum()

                plt.figure(figsize=(9, 5))

                chart.plot(kind="bar")

                plt.title("Duration by Activity")
                plt.xlabel("Activity Type")
                plt.ylabel("Duration (Minutes)")
                plt.xticks(rotation=30)

                self.save_and_show_chart(
                    "bar_chart.png"
                )

            # ----------------------------------
            # LINE GRAPH
            # ----------------------------------

            elif choice == "2":
                chart = (
                    self.data.groupby("Date")[
                        "Calories Burned"
                    ].sum().sort_index()
                )

                plt.figure(figsize=(10, 5))

                chart.plot(
                    kind="line",
                    marker="o"
                )

                plt.title("Daily Calories Burned")
                plt.xlabel("Date")
                plt.ylabel("Calories")
                plt.xticks(rotation=45)

                self.save_and_show_chart(
                    "line_chart.png"
                )

            # ----------------------------------
            # PIE CHART
            # ----------------------------------

            elif choice == "3":
                chart = self.data[
                    "Activity Type"
                ].value_counts()

                plt.figure(figsize=(7, 7))

                plt.pie(
                    chart,
                    labels=chart.index,
                    autopct="%1.1f%%",
                    startangle=90
                )

                plt.title("Activity Distribution")

                self.save_and_show_chart(
                    "pie_chart.png"
                )

            # ----------------------------------
            # HEATMAP
            # ----------------------------------

            elif choice == "4":
                correlation = self.data[
                    [
                        "Duration (Minutes)",
                        "Calories Burned"
                    ]
                ].corr()

                plt.figure(figsize=(7, 5))

                sns.heatmap(
                    correlation,
                    annot=True,
                    cmap="coolwarm",
                    linewidths=0.5
                )

                plt.title("Fitness Data Heatmap")

                self.save_and_show_chart(
                    "heatmap.png"
                )

            # ----------------------------------
            # GENERATE ALL CHARTS
            # ----------------------------------

            elif choice == "5":
                print("\nGenerating All Charts...")

                # Bar Chart
                chart = self.data.groupby(
                    "Activity Type"
                )["Duration (Minutes)"].sum()

                plt.figure(figsize=(9, 5))

                chart.plot(
                    kind="bar",
                    title="Duration by Activity"
                )

                plt.xlabel("Activity Type")
                plt.ylabel("Duration (Minutes)")
                plt.xticks(rotation=30)

                self.save_and_show_chart(
                    "bar_chart.png"
                )

                # Line Graph
                daily = (
                    self.data.groupby("Date")[
                        "Calories Burned"
                    ].sum().sort_index()
                )

                plt.figure(figsize=(10, 5))

                daily.plot(
                    kind="line",
                    marker="o",
                    title="Daily Calories Burned"
                )

                plt.xlabel("Date")
                plt.ylabel("Calories")
                plt.xticks(rotation=45)

                self.save_and_show_chart(
                    "line_chart.png"
                )

                # Pie Chart
                activity = self.data[
                    "Activity Type"
                ].value_counts()

                plt.figure(figsize=(7, 7))

                plt.pie(
                    activity,
                    labels=activity.index,
                    autopct="%1.1f%%",
                    startangle=90
                )

                plt.title("Activity Distribution")

                self.save_and_show_chart(
                    "pie_chart.png"
                )

                # Heatmap
                correlation = self.data[
                    [
                        "Duration (Minutes)",
                        "Calories Burned"
                    ]
                ].corr()

                plt.figure(figsize=(7, 5))

                sns.heatmap(
                    correlation,
                    annot=True,
                    cmap="coolwarm",
                    linewidths=0.5
                )

                plt.title("Fitness Data Heatmap")

                self.save_and_show_chart(
                    "heatmap.png"
                )

                print(
                    "\nAll Charts Generated Successfully!"
                )
                print(
                    f"Charts Folder: {self.chart_folder}"
                )

            # ----------------------------------
            # GO BACK
            # ----------------------------------

            elif choice == "6":
                break

            else:
                print(
                    "Invalid Choice! Please Try Again."
                )

    # ======================================
    # 6. SHOW ALL ACTIVITIES
    # ======================================

    def show_all_activities(self):
        print("\n========== ALL ACTIVITIES ==========")

        if self.data.empty:
            print("No Activities Found!")
        else:
            print(self.data.to_string(index=False))

    # ======================================
    # 7. MAIN MENU
    # ======================================

    def main_menu(self):
        while True:
            print("\n========================================")
            print("       PERSONAL FITNESS TRACKER")
            print("========================================")
            print("1. Log New Activity")
            print("2. Calculate Fitness Metrics")
            print("3. Filter Activities")
            print("4. Generate Fitness Report")
            print("5. Visualize Progress")
            print("6. Show All Activities")
            print("7. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.log_activity()

            elif choice == "2":
                self.calculate_metrics()

            elif choice == "3":
                self.filter_activities()

            elif choice == "4":
                self.generate_report()

            elif choice == "5":
                self.visualize_progress()

            elif choice == "6":
                self.show_all_activities()

            elif choice == "7":
                print("\n========================================")
                print("Thank You for Using Fitness Tracker!")
                print("Stay Healthy, Stay Fit!")
                print("Program Exited Successfully.")
                print("========================================")
                break

            else:
                print(
                    "\nInvalid Choice! Please Enter 1 to 7."
                )


# ==========================================
#             MAIN PROGRAM
# ==========================================

if __name__ == "__main__":
    tracker = FitnessTracker()
    tracker.main_menu()
