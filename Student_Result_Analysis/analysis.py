import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/student_data.csv")

print("\nStudent Dataset")
print(df)

# Check missing values
print("\nMissing Values")
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing values
df.fillna(0, inplace=True)

# Create Total and Average
df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

# Grade function
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Average"].apply(grade)

print("\nUpdated Dataset")
print(df)

# Top performer
top_student = df[df["Average"] == df["Average"].max()]

print("\nTop Performer")
print(top_student[["Name", "Average"]])

# Attendance vs Average
plt.figure(figsize=(8,5))
sns.scatterplot(x=df["Attendance"], y=df["Average"])
plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance")
plt.ylabel("Average Marks")
plt.savefig("visuals/attendance_vs_average.png")

# Subject Wise Average
subject_avg = df[["Math","Science","English"]].mean()

plt.figure(figsize=(8,5))
subject_avg.plot(kind='bar')
plt.title("Subject Wise Average Marks")
plt.ylabel("Marks")
plt.savefig("visuals/subject_average.png")

# Grade Distribution
plt.figure(figsize=(6,4))
sns.countplot(x=df["Grade"])
plt.title("Grade Distribution")
plt.savefig("visuals/grade_distribution.png")

# Save final report
df.to_csv("reports/final_student_report.csv", index=False)

print("\nAnalysis Completed Successfully")
