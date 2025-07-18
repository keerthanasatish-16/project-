import pandas as pd 
import numpy as np

data = {
    'Student':['A','B','C','D','E'],
    'Study Hours':[3.5,5.0,2.0,4.0,6.0],
    'Sleep Hours':[6,7,5,6,8],
    'Attendance (%)':[80,60,50,85,95],
    'Marks':[65,70,50,88,67],
    }
df=pd.DataFrame(data)
print("First few rows")
print(df.info())

print("\n DataFrameInfo:")
print(df.describe())

print("\nAverage Marks:")
print(np.max(df['Marks']))

print("\n Max study hours:")
print(np.max(df['Study Hours']))

print("\n Minimum Attendance")
print(np.min(df['Attendance (%)']))

print("\n Correlation Matrix:")
print(df.corr(numeric_only=True))

print("\n Students sorted by Marks (highest to lowest):")
print(df.sort_values(by='Marks', ascending=False))

print("\n Standard Deviation of marks:")
print(np.std(df['Marks']))

print("\n Students with attendance bleow 70 %:")
print(df[df['Attendance (%)'] < 70])

def get_grades(marks):
    if marks >=85:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >=50:
        return 'C'
    else:
        return 'D'
    df['Grade']= df['Marks'].apply(get_grade)
    print("\n Data with Grades")
    print(df)
