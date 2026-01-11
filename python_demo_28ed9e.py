# Learning Objective: Build a simple interactive data visualization app using Python and Streamlit.
# This tutorial will guide you through creating a basic web application that displays and interacts with data.
# We will focus on using Streamlit for rapid web app development and Matplotlib for plotting.
# By the end, you'll have a functional app that allows users to filter data and see a corresponding chart.

# Import the necessary libraries
import streamlit as st  # Streamlit is a framework for building interactive web apps with Python
import pandas as pd     # Pandas is used for data manipulation and analysis, specifically DataFrames
import matplotlib.pyplot as plt # Matplotlib is a popular plotting library for creating static, interactive, and animated visualizations

# --- Data Preparation ---
# In a real application, you'd load data from a file (like CSV) or a database.
# For this example, we'll create a simple, small dataset directly in the code.
# This makes the tutorial self-contained and easy to run.
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'Value': [10, 15, 12, 8, 20, 11, 9, 18, 13, 7],
    'AnotherValue': [5, 7, 6, 4, 10, 5, 4, 9, 6, 3]
}
df = pd.DataFrame(data) # Convert the dictionary into a Pandas DataFrame. DataFrames are tabular data structures that are easy to work with.

# --- App Title and Description ---
st.title("Simple Interactive Data Visualization App") # Set the main title of your Streamlit app. This will be displayed prominently.
st.write("This app demonstrates how to create an interactive data visualization using Streamlit and Matplotlib.") # Provide a brief description of what the app does.

# --- User Input/Interactivity ---
# Streamlit provides various widgets for user interaction.
# Here, we'll create a dropdown (select box) to allow users to filter the data by 'Category'.

# Get a list of unique categories from our DataFrame.
# .unique() returns an array of unique values in the 'Category' column.
unique_categories = df['Category'].unique()

# Add a "Select All" option to the list for convenience.
# This makes it easier for users to view all data without selecting each category individually.
options = ['Select All'] + list(unique_categories)

# Create a selectbox widget.
# st.selectbox() displays a dropdown menu.
# The first argument is the label displayed next to the dropdown.
# The second argument is the list of options the user can choose from.
selected_category = st.selectbox(
    'Filter by Category:', # Label for the dropdown menu
    options # The list of categories to choose from
)

# --- Data Filtering ---
# Based on the user's selection, we'll filter the DataFrame.
if selected_category == 'Select All':
    # If 'Select All' is chosen, display the entire DataFrame.
    filtered_df = df
    st.write("Displaying all data.") # Inform the user what is being displayed.
else:
    # If a specific category is chosen, filter the DataFrame.
    # We use boolean indexing to select rows where the 'Category' column matches the selected_category.
    filtered_df = df[df['Category'] == selected_category]
    st.write(f"Displaying data for category: **{selected_category}**") # Show which category is currently filtered.

# --- Displaying Filtered Data (Optional but good for understanding) ---
st.subheader("Filtered Data Preview") # A sub-header for the data preview section.
st.dataframe(filtered_df) # st.dataframe() displays the DataFrame in an interactive table. This is useful for users to see the raw data.

# --- Data Visualization ---
# Now, let's create a plot based on the filtered data.
st.subheader("Data Visualization") # Sub-header for the plotting section.

# Create a figure and an axes object for the plot.
# This is the standard way to create plots with Matplotlib.
fig, ax = plt.subplots()

# Create a bar chart.
# We'll plot the 'Category' on the x-axis and 'Value' on the y-axis from the filtered data.
# The .plot.bar() method is a convenient Pandas wrapper around Matplotlib for creating bar charts.
filtered_df.plot.bar(x='Category', y='Value', ax=ax, legend=False) # ax=ax tells Pandas to draw on our created axes. legend=False hides the default legend.

# Customize the plot.
ax.set_title('Value by Category') # Set the title of the plot.
ax.set_xlabel('Category') # Set the label for the x-axis.
ax.set_ylabel('Value') # Set the label for the y-axis.
ax.tick_params(axis='x', rotation=0) # Ensure x-axis labels are horizontal for readability.

# Display the plot in the Streamlit app.
st.pyplot(fig) # st.pyplot() renders the Matplotlib figure in the Streamlit interface.

# --- Example Usage ---
# To run this app:
# 1. Save the code as a Python file (e.g., app.py).
# 2. Open your terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: streamlit run app.py
#
# This will open the app in your web browser, where you can interact with the dropdown and see the chart update.
# This is a very basic example, but it lays the foundation for more complex interactive dashboards.