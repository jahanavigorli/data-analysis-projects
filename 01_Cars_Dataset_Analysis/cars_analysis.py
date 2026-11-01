import pandas as pd

import os
import pandas as pd

file_path = os.path.join(os.path.dirname(__file__), "CARS.xlsx")
df = pd.read_excel(file_path)

print("\n1. First 5 Rows")
print(df.head())

print("\n2. Last 5 Rows")
print(df.tail())

print("\n3. Number of Rows and Columns")
print(df.shape)

print("\n4. Column Names")
print(df.columns)

print("\n5. Data Types")
print(df.dtypes)

print("\n6. Brand and Model")
print(df[['Brand', 'Model']])

print("\n7. Price (Lakhs)")
print(df['Price (Lakhs)'])

print("\n8. First 8 Rows")
print(df.head(8))

print("\n9. Petrol Cars")
print(df[df['Fuel_Type'] == 'Petrol'][['Brand', 'Model']])

print("\n10. Diesel Cars")
print(df[df['Fuel_Type'] == 'Diesel'][['Brand', 'Model']])

print("\n11. Cars with Price > 10 Lakhs")
print(df[df['Price (Lakhs)'] > 10][['Brand', 'Model']])

print("\n12. Cars with Mileage > 20 kmpl")
print(df[df['Mileage (kmpl)'] > 20][['Brand', 'Model']])

print("\n13. Automatic Cars")
print(df[df['Transmission'] == 'Automatic'][['Brand', 'Model']])

print("\n14. Average Price")
print(df['Price (Lakhs)'].mean())

print("\n15. Maximum Mileage")
print(df['Mileage (kmpl)'].max())

print("\n16. Minimum Price")
print(df['Price (Lakhs)'].min())

print("\n17. Average Mileage")
print(df['Mileage (kmpl)'].mean())

print("\n18. Fuel Type Count")
print(df['Fuel_Type'].value_counts())

print("\n19. Sorted by Price (Ascending)")
print(df.sort_values(by='Price (Lakhs)')[['Brand', 'Model', 'Price (Lakhs)']])

print("\n20. Sorted by Mileage (Descending)")
print(df.sort_values(by='Mileage (kmpl)', ascending=False)[['Brand', 'Model', 'Mileage (kmpl)']])

print("\n21. Top 5 Most Expensive Cars")
top5 = df.sort_values(by='Price (Lakhs)', ascending=False).head(5)
print(top5[['Brand', 'Model']])
