
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv('sales_data (1).csv')

# Total sales per product
df['Total'] = df['Quantity'] * df['Price']
grouped = df.groupby('Product')['Total'].sum()

print("Sales Summary:")
print(grouped)

# Plot graph
grouped.plot(kind='bar')
plt.title("Total Sales by Product")
plt.ylabel("Sales Amount")
plt.show()
