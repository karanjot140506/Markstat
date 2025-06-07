import numpy as np

# Sample data: rows = students, columns = subjects
marks = np.array([
    [80, 85, 90],
    [75, 80, 85],
    [90, 92, 88],
    [34, 45, 40],
    [60, 50, 55]
])

# 1) Average score per student
avg_per_student = np.mean(marks, axis=1)
print("Average marks per student:")
print(avg_per_student)

# 2) Average score per subject
avg_per_subject = np.mean(marks, axis=0)
print("\nAverage marks per subject:")
print(avg_per_subject)

# 3) Highest & Lowest score
highest = np.max(marks)
lowest = np.min(marks)
print(f"\nHighest score: {highest}")
print(f"Lowest score: {lowest}")

# 4) Pass/Fail count (pass if all subjects ≥ 40)
passes = np.sum(np.all(marks >= 40, axis=1))
fails = marks.shape[0] - passes
print(f"\nTotal Passed Students: {passes}")
print(f"Total Failed Students: {fails}")

# 5) Total and percentage per student
total_marks = np.sum(marks, axis=1)
percentages = (total_marks / (marks.shape[1] * 100)) * 100
print("\nTotal and Percentage per Student:")
for i in range(len(total_marks)):
    print(f"Student {i+1}: Total = {total_marks[i]}, Percentage = {percentages[i]:.2f}%")
