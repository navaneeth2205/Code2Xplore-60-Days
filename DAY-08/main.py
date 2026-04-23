import random
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def generate_data(n):
    records = []

    for i in range(1, n + 1):
        marks = random.randint(0, 100)
        attendance = random.randint(0, 100)
        assignment = random.randint(0, 50)

        # combining marks + assignment and using log(attendance+1)
        perf_index = (marks * 0.6 + assignment * 0.4) * math.log(attendance + 1)

        records.append((i, marks, attendance, assignment, perf_index))

    return records


def classify_students(records):
    categories = {"At Risk": [], "Average": [], "Good": [], "Top Performer": []}

    for rec in records:
        sid = rec[0]
        marks = rec[1]
        attendance = rec[2]

        if marks < 40 or attendance < 50:
            categories["At Risk"].append(sid)
        elif marks > 90 and attendance > 80:
            categories["Top Performer"].append(sid)
        elif 71 <= marks <= 90:
            categories["Good"].append(sid)
        else:
            categories["Average"].append(sid)

    return categories


def analyze_data(df_data):
    marks_list = df_data["Marks"].to_list()

    mean_val = float(np.mean(marks_list))
    median_val = float(np.median(marks_list))
    std_val = float(np.std(marks_list))

    # manual mean
    total_val = 0
    for val in marks_list:
        total_val += val
    manual_mean = total_val / len(marks_list)

    # correlation
    corr_val = float(np.corrcoef(df_data["Marks"], df_data["Attendance"])[0][1])

    # normalization
    min_val = min(marks_list)
    max_val = max(marks_list)

    norm_vals = [
        (val - min_val) / (max_val - min_val) if max_val != min_val else 0
        for val in marks_list
    ]

    df_data.loc[:, "Norm"] = norm_vals

    return mean_val, median_val, std_val, manual_mean, corr_val


# -------- main --------

roll_digit = int(input("Enter last digit of roll number: "))

if not (0 <= roll_digit <= 9):
    print("Invalid input")
    exit()

if roll_digit == 0:
    roll_digit = 10

total_students = 10
data = generate_data(total_students)

df = pd.DataFrame(data, columns=["ID", "Marks", "Attendance", "Assignment", "PI"])

# 🔹 added set usage (requirement)
unique_ids = set(df["ID"])

df_subset = df.head(roll_digit).copy()

categories = classify_students(data)

mean_val, median_val, std_val, manual_mean, corr_val = analyze_data(df_subset)

summary = (mean_val, std_val, int(df_subset["Marks"].max()))


# -------- pattern detection --------

low_att_count = sum(1 for val in df_subset["Attendance"] if val < 50)
top_count = len(categories["Top Performer"])

# 🔹 updated logic to include top_count
if std_val < 15 and low_att_count <= 3:
    status = "Stable Academic System"
elif low_att_count > 3:
    status = "Critical Attention Required"
elif top_count >= 2:
    status = "Moderate Performance"
else:
    status = "Moderate Performance"


# -------- output --------

print("\n--- Filtered Student Data ---")
print(df_subset)

print("\nCategories:", categories)

print("\nMean:", round(mean_val, 2))
print("Manual Mean:", round(manual_mean, 2))
print("Median:", round(median_val, 2))
print("Std Dev:", round(std_val, 2))
print("Correlation:", round(corr_val, 4))

print("\nSummary Tuple:", summary)
print("System Status:", status)

print("\nTotal Unique Students:", len(unique_ids))  # showing set usage


# -------- visualization --------

sorted_marks = sorted(df_subset["Marks"])
student_index = list(range(1, len(sorted_marks) + 1))

plt.plot(student_index, sorted_marks, marker='o')

plt.title("Marks Trend")
plt.xlabel("Student Index")
plt.ylabel("Marks")

plt.grid(True)

plt.show()