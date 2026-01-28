# Learning Objective: Introduction to Data Processing and Analysis with Pandas in Python

# This tutorial will introduce you to the fundamental concepts of
# processing and analyzing data using the powerful 'pandas' library in Python.
# We'll cover loading data, basic inspection, filtering, and simple calculations.

# Make sure you have pandas installed:
# pip install pandas

# Import the pandas library, conventionally aliased as 'pd'
import pandas as pd

# --- 1. Creating a DataFrame ---
# A DataFrame is the primary data structure in pandas,
# similar to a table in a database or a spreadsheet.
# We'll start by creating a sample DataFrame from a Python dictionary.

# A dictionary where keys are column names and values are lists of data for each column.
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age': [25, 30, 35, 28, 22, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Chicago', 'Los Angeles'],
    'Salary': [60000, 75000, 80000, 65000, 55000, 90000]
}

# Create the DataFrame from the dictionary.
df = pd.DataFrame(data)

# --- 2. Inspecting the Data ---
# It's crucial to understand your data's structure and content.

# Display the first 5 rows of the DataFrame.
# 'head()' is useful for a quick look at the data.
print("--- First 5 rows of the DataFrame ---")
print(df.head())
print("\n") # Add a newline for better readability

# Display the last 3 rows of the DataFrame.
# 'tail()' shows the end of the DataFrame.
print("--- Last 3 rows of the DataFrame ---")
print(df.tail(3))
print("\n")

# Get a concise summary of the DataFrame, including the index dtype and column dtypes,
# non-null values, and memory usage.
print("--- DataFrame Info ---")
df.info()
print("\n")

# Get descriptive statistics of the DataFrame.
# This includes count, mean, standard deviation, min, max, and quartiles for numerical columns.
print("--- Descriptive Statistics ---")
print(df.describe())
print("\n")

# Get the shape of the DataFrame (number of rows, number of columns).
print("--- DataFrame Shape (rows, columns) ---")
print(df.shape)
print("\n")

# Get the column names.
print("--- Column Names ---")
print(df.columns)
print("\n")

# --- 3. Selecting Data (Column and Row Access) ---

# Select a single column by its name.
# This returns a pandas Series.
print("--- Selecting the 'Name' column ---")
print(df['Name'])
print("\n")

# Select multiple columns by passing a list of column names.
# This returns a new DataFrame.
print("--- Selecting 'Name' and 'Salary' columns ---")
print(df[['Name', 'Salary']])
print("\n")

# Select rows based on their integer position (index).
# '.iloc[]' is used for integer-location based indexing.
# Get the first row (index 0).
print("--- First row using iloc ---")
print(df.iloc[0])
print("\n")

# Get rows from index 1 up to (but not including) index 3.
print("--- Rows from index 1 to 2 using iloc ---")
print(df.iloc[1:3])
print("\n")

# --- 4. Filtering Data ---
# Filtering allows you to select rows that meet specific conditions.

# Filter rows where 'Age' is greater than 30.
# This creates a boolean Series, which is then used to index the DataFrame.
print("--- People older than 30 ---")
older_than_30 = df[df['Age'] > 30]
print(older_than_30)
print("\n")

# Filter rows where 'City' is 'New York'.
print("--- People living in New York ---")
new_yorkers = df[df['City'] == 'New York']
print(new_yorkers)
print("\n")

# Combine multiple conditions using logical operators:
# '&' for AND, '|' for OR. Parentheses are important for clarity and correctness.
print("--- People in New York earning more than $60,000 ---")
ny_high_earners = df[(df['City'] == 'New York') & (df['Salary'] > 60000)]
print(ny_high_earners)
print("\n")

# --- 5. Basic Data Analysis ---

# Calculate the average salary.
# The '.mean()' method calculates the arithmetic mean of the column.
average_salary = df['Salary'].mean()
print(f"--- Average Salary: ${average_salary:.2f} ---")
print("\n")

# Find the maximum age.
# The '.max()' method finds the largest value in the column.
max_age = df['Age'].max()
print(f"--- Maximum Age: {max_age} ---")
print("\n")

# Count the number of people in each city.
# '.value_counts()' is a very useful method for categorical data.
print("--- Count of people per city ---")
city_counts = df['City'].value_counts()
print(city_counts)
print("\n")

# Calculate the sum of salaries.
total_salary_paid = df['Salary'].sum()
print(f"--- Total Salary Paid: ${total_salary_paid} ---")
print("\n")


# --- Example Usage: Analyzing a hypothetical sales dataset ---

# Let's imagine we have sales data.
sales_data = {
    'Product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A'],
    'Quantity': [10, 5, 12, 8, 7, 15, 9, 6, 11],
    'Price': [2.5, 5.0, 2.5, 10.0, 5.0, 2.5, 10.0, 5.0, 2.5]
}
sales_df = pd.DataFrame(sales_data)

# Calculate the 'Total Revenue' for each sale.
# We can create a new column by performing calculations on existing ones.
sales_df['Total Revenue'] = sales_df['Quantity'] * sales_df['Price']

print("--- Sales DataFrame with Total Revenue ---")
print(sales_df)
print("\n")

# Find the total revenue for each product.
# '.groupby()' is a powerful method for split-apply-combine operations.
# We group by 'Product', then sum the 'Total Revenue' for each group.
product_revenue = sales_df.groupby('Product')['Total Revenue'].sum()

print("--- Total Revenue per Product ---")
print(product_revenue)
print("\n")

# Find the product with the highest total revenue.
# '.idxmax()' returns the index (product name in this case) of the maximum value.
most_profitable_product = product_revenue.idxmax()
highest_revenue = product_revenue.max()

print(f"--- The most profitable product is '{most_profitable_product}' with a total revenue of ${highest_revenue:.2f} ---")
print("\n")

# This concludes the basic introduction to data processing and analysis with pandas.
# You've learned how to create, inspect, select, filter, and perform simple
# calculations on data.