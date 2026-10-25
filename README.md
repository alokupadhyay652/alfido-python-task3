# alfido-python-task3

Alfido Tech Python Developer Internship - Task 3: Data Analysis with Pandas

## About
A simple data analysis project using Pandas. It loads student marks from a CSV file, cleans missing and wrong data, applies filtering, grouping and aggregation, and explains the results in simple words.

## What it does
1. Load and inspect: reads the CSV with pd.read_csv() and shows the first rows, shape, data types and missing values.
2. Clean the data: converts text like "absent" to missing values, finds impossible marks (above 100), and fills all missing marks with the subject average.
3. Filtering: shows students whose average is above 80.
4. Grouping and aggregation: average marks by class, and mean, max and min for each subject.
5. Sorting: ranks students by total marks.
6. Insights: prints a short summary in simple words.
7. Saves the cleaned data to students_result.csv.

## How to run
```
pip install pandas
python task3_pandas.py
```

## Insight summary
- Students did best in English and weakest in Science.
- Class C has the highest average marks.
- 5 out of 10 students scored an average above 80.
- Vikas is the topper with an average of 91.7.
- Rahul scored the lowest (average 65.9) and may need extra help.

## Concepts used
read_csv, head, shape, dtypes, isnull, to_numeric, fillna, filtering, groupby, agg, sort_values, to_csv.

## Repository
https://github.com/alokupadhyay652/alfido-python-task3

## Document
https://drive.google.com/file/d/1hI05Pr4updjp1ZCsj66-CGEiLLNG649u/view?usp=drivesdk
