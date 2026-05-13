# ==============================
# NUMPY ARRAY OPERATIONS
# ==============================

import numpy as np
import pandas as pd

# 1. Create a 1D NumPy Array
temperatures_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])

print("Week 1 Temperatures:")
print(temperatures_w1)

# 2. Inspection and Properties
print("\n--- Inspection ---")
print("Shape:", temperatures_w1.shape)
print("Data Type:", temperatures_w1.dtype)
print("Number of Elements:", temperatures_w1.size)

# 3. Array Operations

# Celsius to Fahrenheit
fahrenheit = (temperatures_w1 * 9/5) + 32

print("\nTemperatures in Fahrenheit:")
print(fahrenheit)

# Maximum, Minimum, Mean
print("\n--- Statistics ---")
print("Maximum Temperature:", np.max(temperatures_w1))
print("Minimum Temperature:", np.min(temperatures_w1))
print("Mean Temperature:", np.mean(temperatures_w1))

# 4. Array Slicing and Indexing

# First three days
print("\nFirst Three Days:")
print(temperatures_w1[:3])

# Weekend (last two days)
print("\nWeekend Temperatures:")
print(temperatures_w1[-2:])

# Middle three days
print("\nMiddle Three Days:")
print(temperatures_w1[2:5])

# 5. Create a 2D Array

temperatures = np.array([
    [22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9],   # Week 1
    [19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1]    # Week 2
])

print("\n2D Temperature Array:")
print(temperatures)

# 6. Inspect and Slice the 2D Array

print("\n--- 2D Array Inspection ---")
print("Shape:", temperatures.shape)
print("Data Type:", temperatures.dtype)
print("Total Elements:", temperatures.size)

# Extract temperatures for each week
print("\nWeek 1 Temperatures:")
print(temperatures[0])

print("\nWeek 2 Temperatures:")
print(temperatures[1])

# Weekend temperatures for both weeks
print("\nWeekend Temperatures (Both Weeks):")
print(temperatures[:, -2:])


# ==============================
# PANDAS SERIES
# ==============================

# 1. Creating Pandas Series

marks = pd.Series(
    [95, 92, 89, 85, 80],
    index=['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Rank5']
)

print("\nMarks Series:")
print(marks)

# 2. Indexing and Slicing

# Integer index position
print("\nMark of 1st Rank Student:")
print(marks[0])

# loc accessor
print("\nTop 3 Ranks using loc:")
print(marks.loc[['Rank1', 'Rank2', 'Rank3']])

# iloc accessor
print("\n3rd Ranked Student using iloc:")
print(marks.iloc[2])

# Boolean Mask
print("\nMarks Greater Than 90:")
print(marks[marks > 90])

# 3. Manipulating Series

# Modify Rank1 mark
marks['Rank1'] = 100

print("\nAfter Modifying Rank1:")
print(marks)

# Remove last rank
marks = marks.drop('Rank5')

print("\nAfter Removing Rank5:")
print(marks)

# Compute CGPA
cgpa = marks / 10

print("\nCGPA:")
print(cgpa)


# ==============================
# PANDAS DATAFRAME
# ==============================

# 1. Creating Pandas DataFrame

transactions = pd.DataFrame({
    'TransactionID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'ProductCategory': [
        'Electronics', 'Clothing', 'Electronics', 'Furniture',
        'Clothing', 'Electronics', 'Furniture', 'Clothing',
        'Furniture', 'Electronics'
    ],
    'Region': [
        'North', 'South', 'North', 'East', 'West',
        'North', 'East', 'West', 'South', 'North'
    ],
    'Amount': [200, 150, 300, 450, 200, 250, 300, 180, 350, 400]
})

print("\nTransactions DataFrame:")
print(transactions)

# 2. Data Exploration

print("\nHead:")
print(transactions.head())

print("\nTail:")
print(transactions.tail())

print("\nShape:")
print(transactions.shape)

print("\nColumn Names:")
print(transactions.columns)

print("\nData Types:")
print(transactions.dtypes)

# Display specific columns
print("\nProductCategory and Amount Columns:")
print(transactions[['ProductCategory', 'Amount']])

# Last 3 columns
print("\nLast 3 Columns:")
print(transactions.iloc[:, -3:])

# Filter rows
print("\nRegion = North and Amount > 200:")
print(
    transactions[
        (transactions['Region'] == 'North') &
        (transactions['Amount'] > 200)
    ]
)

# Value counts
print("\nProductCategory Value Counts:")
print(transactions['ProductCategory'].value_counts())

# Unique regions
print("\nUnique Regions:")
print(transactions['Region'].unique())

# Group by Region and mean Amount
print("\nMean Amount by Region:")
print(transactions.groupby('Region')['Amount'].mean())

# 3. Manipulating the DataFrame

# Modify Amount for TransactionID 102
transactions.loc[transactions['TransactionID'] == 102, 'Amount'] = 165

print("\nAfter Modifying Amount for TransactionID 102:")
print(transactions)

# Add Discount column
transactions['Discount'] = transactions['Amount'] * 0.10

print("\nAfter Adding Discount Column:")
print(transactions)

# Remove row with TransactionID 109
transactions = transactions[transactions['TransactionID'] != 109]

print("\nAfter Removing TransactionID 109:")
print(transactions)

# Delete Discount column
transactions.drop(columns=['Discount'], inplace=True)

print("\nAfter Deleting Discount Column:")
print(transactions)