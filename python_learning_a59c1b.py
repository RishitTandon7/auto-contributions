# Objective: Learn to create basic, interactive data visualizations in Python using Pandas for data manipulation and Matplotlib for plotting.
# This tutorial will guide you through loading data, performing simple transformations, and generating a dynamic scatter plot.

# Import necessary libraries
import pandas as pd  # Pandas is essential for data manipulation and analysis. It provides DataFrames, which are like tables.
import matplotlib.pyplot as plt # Matplotlib is a powerful plotting library for creating static, animated, and interactive visualizations.

# --- Step 1: Load and Prepare Data ---

# For this tutorial, we'll create a simple, synthetic dataset.
# In a real-world scenario, you would load data from a file (e.g., CSV, Excel) using pd.read_csv() or pd.read_excel().

# Creating a dictionary to hold our data.
# Each key will be a column name, and the value will be a list of data points.
data = {
    'x_values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'y_values': [10, 12, 15, 18, 20, 22, 25, 28, 30, 32, 35, 38],
    'category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A']
}

# Convert the dictionary into a Pandas DataFrame.
# DataFrames make it easy to work with tabular data.
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame to understand its structure.
# .head() is useful for quickly inspecting data without printing everything.
print("Our DataFrame:")
print(df.head())
print("\n") # Add a newline for better readability.

# --- Step 2: Create a Dynamic Scatter Plot ---

# We want to visualize the relationship between 'x_values' and 'y_values'.
# A scatter plot is ideal for this purpose, showing individual data points.

# Create a figure and a set of subplots.
# 'fig' is the overall window or page, and 'ax' is the actual plot area.
fig, ax = plt.subplots(figsize=(10, 6)) # figsize sets the dimensions of the plot in inches.

# Generate the scatter plot.
# df['x_values'] and df['y_values'] select the columns from our DataFrame.
# 's' controls the size of the markers.
# 'c' controls the color of the markers. We'll use the 'category' column to color-code points.
# 'cmap' specifies the colormap to use for mapping numerical data to colors. 'viridis' is a popular choice.
scatter = ax.scatter(df['x_values'], df['y_values'], s=100, c=df['category'].astype('category').cat.codes, cmap='viridis')

# Add labels and a title to the plot for clarity.
# These are crucial for making your visualizations understandable.
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")
ax.set_title("Dynamic Scatter Plot of X vs Y by Category")

# Add a legend. This is essential when using color to represent different categories.
# We need to create a legend handle for each unique category.
# .unique() gets all unique values from the 'category' column.
# .cat.codes converts categories to numbers, which helps with color mapping.
unique_categories = df['category'].unique()
handles = [plt.Line2D([0], [0], marker='o', color='w', label=cat,
                          markerfacecolor=scatter.cmap(scatter.norm(df[df['category'] == cat]['category'].astype('category').cat.codes.iloc[0]))[0],
                          markersize=10) for cat in unique_categories]
ax.legend(handles=handles, title="Category")

# To make the plot "dynamic" in a simple sense for this tutorial, we'll ensure it displays interactively.
# Matplotlib's default backends often provide interactive features like zooming and panning.

# --- Step 3: Display the Plot ---

# This command shows the generated plot.
# When you run this script, a window will pop up displaying the interactive scatter plot.
plt.show()

# --- Example Usage ---
# To run this tutorial:
# 1. Make sure you have pandas and matplotlib installed:
#    pip install pandas matplotlib
# 2. Save the code as a Python file (e.g., 'data_viz_tutorial.py').
# 3. Run the file from your terminal:
#    python data_viz_tutorial.py
#
# You will see the DataFrame printed in your console, followed by an interactive plot window.
# You can zoom, pan, and hover over points (depending on your Matplotlib backend) for more information.