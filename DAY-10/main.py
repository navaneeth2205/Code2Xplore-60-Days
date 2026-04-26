import random
import math
import numpy as np
import pandas as pd
import copy


def create_data(n):
    data = []
    for i in range(1, n + 1):
        record = {
            "id": i,
            "marks": random.randint(40, 100),
            "attendance": random.randint(50, 100),
            "scores": [random.randint(10, 25), random.randint(10, 25)]
        }
        data.append(record)
    return data


def apply_changes(data):
    for i in range(len(data)):
        if i % rule_value == 0:
            m = data[i]["marks"]
            data[i]["marks"] = int(m + math.sqrt(m))
            data[i]["scores"][0] += 2
            data[i]["attendance"] -= 5
    return data


def analyze(df):
    marks = df["marks"].tolist()

    mean_val = np.mean(marks)
    median_val = np.median(marks)
    std_val = np.std(marks)

    total = 0
    for x in marks:
        total += x
    manual_mean = total / len(marks)

    unique_count = len(set(marks))

    min_m = min(marks)
    max_m = max(marks)
    norm = [(x - min_m) / (max_m - min_m) if max_m != min_m else 0 for x in marks]
    df["norm"] = norm

    return mean_val, median_val, std_val, manual_mean, unique_count


def detect_drift(orig_mean, new_mean):
    return abs(orig_mean - new_mean)


# main

roll_input = input("Enter your full roll number: ")

num_str = ""
for ch in roll_input:
    if ch.isdigit():
        num_str += ch

if num_str == "":
    print("Invalid input")
    exit()

roll_number = int(num_str)
rule_value = roll_number % 3

if rule_value == 0:
    rule_value = 1

n = random.randint(10, 15)
data = create_data(n)

df_original = pd.DataFrame(data)

backup = copy.deepcopy(data)

shallow_copy = data.copy()
deep_copy = copy.deepcopy(data)

apply_changes(shallow_copy)
apply_changes(deep_copy)

df_shallow = pd.DataFrame(shallow_copy)
df_deep = pd.DataFrame(deep_copy)

orig_mean, _, orig_std, _, _ = analyze(df_original)
sh_mean, _, sh_std, _, _ = analyze(df_shallow)
dp_mean, _, dp_std, _, _ = analyze(df_deep)

drift_val = detect_drift(orig_mean, sh_mean)
drift_deep = detect_drift(orig_mean, dp_mean)

copy_failure = False
if backup != data:
    copy_failure = True

threshold = 5

if drift_val < threshold:
    drift_status = "Stable Data"
elif drift_val < threshold * 2:
    drift_status = "Minor Drift"
else:
    drift_status = "Critical Drift"

if copy_failure:
    final_status = f"{drift_status} (Copy Failure Detected)"
else:
    final_status = f"{drift_status} (Data Safe)"


print("\n--- Original Data ---")
print(df_original)

print("\n--- Shallow Copy Result ---")
print(df_shallow)

print("\n--- Deep Copy Result ---")
print(df_deep)

print(f"\nDrift Value: {round(drift_val, 2)}")

summary = (orig_mean, drift_val, sh_std)
print("Summary Tuple:", summary)

print("Final Status:", final_status)

print("\nExplanation:")
print("Shallow copy shares inner lists, so changes affected original data.")
print("Deep copy creates separate data, so original remains unchanged.")