import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\jahanavi gorli\Downloads\student.xlsx")

df_copy = df.copy()

print("First Five Records")
print(df.head())

print("\nMissing Values Count")
print(df.isnull().sum())

df.loc[0, 'CGPA'] = None
df.loc[3, 'Attendance'] = None
df.loc[5, 'CGPA'] = None
df.loc[8, 'Attendance'] = None
df.loc[10, 'CGPA'] = None

print("\nMissing Values After Introduction")
print(df.isnull().sum())

mean_df = df.copy()
mean_df['CGPA'] = mean_df['CGPA'].fillna(mean_df['CGPA'].mean())
mean_df['Attendance'] = mean_df['Attendance'].fillna(mean_df['Attendance'].mean())

median_df = df.copy()
median_df['CGPA'] = median_df['CGPA'].fillna(median_df['CGPA'].median())
median_df['Attendance'] = median_df['Attendance'].fillna(median_df['Attendance'].median())

mode_df = df.copy()
mode_df['CGPA'] = mode_df['CGPA'].fillna(mode_df['CGPA'].mode()[0])
mode_df['Attendance'] = mode_df['Attendance'].fillna(mode_df['Attendance'].mode()[0])

print("\nMean Replacement")
print(mean_df)

print("\nMedian Replacement")
print(median_df)

print("\nMode Replacement")
print(mode_df)

plt.hist(mean_df['CGPA'])
plt.title("Histogram of CGPA")
plt.xlabel("CGPA")
plt.ylabel("Frequency")
plt.show()

print("\nMinimum CGPA:", mean_df['CGPA'].min())
print("Maximum CGPA:", mean_df['CGPA'].max())
print("Mean CGPA:", mean_df['CGPA'].mean())
print("Median CGPA:", mean_df['CGPA'].median())

plt.plot(mean_df['Attendance'], mean_df['CGPA'])
plt.title("Attendance vs CGPA")
plt.xlabel("Attendance")
plt.ylabel("CGPA")
plt.show()

mean_df.loc[0, 'CGPA'] = 20

plt.boxplot(mean_df['CGPA'])
plt.title("Box Plot of CGPA")
plt.show()

plt.scatter(mean_df['Attendance'], mean_df['CGPA'])
plt.title("Scatter Plot of Attendance vs CGPA")
plt.xlabel("Attendance")
plt.ylabel("CGPA")
plt.show()