"""
Task 3: Data Analysis with Pandas
- Load and inspect a CSV dataset
- Clean missing or incorrect data
- Apply filtering, grouping and aggregation
- Explain insights in simple words
"""

import pandas as pd

# ---------------------------------------------------------------
# Create a sample CSV file (student marks).
# It has some missing values and some wrong values on purpose.
# ---------------------------------------------------------------
data = """Name,Class,Maths,Science,English
Aman,A,85,78,90
Riya,A,92,88,85
Karan,B,70,65,
Sneha,B,88,91,94
Rahul,A,550,60,58
Pooja,B,76,,80
Vikas,C,95,89,91
Neha,C,62,70,absent
Isha,C,81,84,79
Dev,A,67,72,70
"""
with open("students.csv", "w") as f:
    f.write(data)

subjects = ["Maths", "Science", "English"]

# ---------------------------------------------------------------
# 1. Load and inspect
# ---------------------------------------------------------------
df = pd.read_csv("students.csv")

print("=== 1. Load and inspect ===")
print("\nFirst 5 rows:")
print(df.head())
print("\nShape (rows, columns):", df.shape)
print("\nData types:")
print(df.dtypes)
print("\nMissing values per column:")
print(df.isnull().sum())

# ---------------------------------------------------------------
# 2. Clean missing or incorrect data
# ---------------------------------------------------------------
print("\n=== 2. Cleaning the data ===")

for col in subjects:
    # text like 'absent' becomes NaN (missing)
    df[col] = pd.to_numeric(df[col], errors="coerce")
    # marks must be between 0 and 100, anything else is wrong
    wrong = (df[col] < 0) | (df[col] > 100)
    if wrong.any():
        print(f"Wrong values found in {col}:", df.loc[wrong, "Name"].tolist())
    df.loc[wrong, col] = None

print("\nMissing values after fixing wrong data:")
print(df[subjects].isnull().sum())

# fill every missing mark with the average of that subject
for col in subjects:
    df[col] = df[col].fillna(df[col].mean()).round(1)

print("\nMissing values left:", int(df.isnull().sum().sum()))

df["Total"] = df[subjects].sum(axis=1).round(1)
df["Average"] = (df["Total"] / 3).round(1)

# ---------------------------------------------------------------
# 3. Filtering, grouping and aggregation
# ---------------------------------------------------------------
print("\n=== 3. Filtering, grouping and aggregation ===")

print("\nStudents with Average above 80:")
above80 = df[df["Average"] > 80]
print(above80[["Name", "Class", "Average"]].to_string(index=False))

print("\nAverage marks by Class:")
by_class = df.groupby("Class")[subjects].mean().round(1)
print(by_class)

print("\nSubject-wise average, highest and lowest marks:")
print(df[subjects].agg(["mean", "max", "min"]).round(1))

print("\nStudents sorted by Total (highest first):")
ranked = df.sort_values("Total", ascending=False)
print(ranked[["Name", "Class", "Total", "Average"]].to_string(index=False))

# ---------------------------------------------------------------
# 4. Insights in simple words
# ---------------------------------------------------------------
print("\n=== 4. Insights in simple words ===")

best_subject = df[subjects].mean().idxmax()
weak_subject = df[subjects].mean().idxmin()
best_class = df.groupby("Class")["Average"].mean().idxmax()
topper = ranked.iloc[0]
lowest = ranked.iloc[-1]

print(f"1. The class has {len(df)} students. After cleaning, no marks are missing.")
print(f"2. Students did best in {best_subject} and weakest in {weak_subject}.")
print(f"3. Class {best_class} has the highest average marks.")
print(f"4. {len(above80)} out of {len(df)} students scored an average above 80.")
print(f"5. The topper is {topper['Name']} (average {topper['Average']}).")
print(f"6. {lowest['Name']} scored the lowest (average {lowest['Average']}) and may need extra help.")

df.to_csv("students_result.csv", index=False)
print("\nCleaned data saved to students_result.csv")
