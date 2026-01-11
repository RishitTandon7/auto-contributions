# This tutorial demonstrates how to build a simple Python application that visualizes data from a CSV file.
# We will use Matplotlib for creating plots and Streamlit for building an interactive web interface.
# This will teach you the basics of data visualization and how to create simple web apps with Python.

# Import necessary libraries
# Streamlit is used to create interactive web applications easily.
# We'll use it to display our plots and allow users to upload their CSV files.
import streamlit as st
# Pandas is a powerful library for data manipulation and analysis.
# It's excellent for reading and working with CSV files.
import pandas as pd
# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
# We'll use itspyplot module for creating our plots.
import matplotlib.pyplot as plt

# Set the title of our Streamlit application
# This will be displayed as the main heading on the web page.
st.title("Simple CSV Data Visualizer")

# Allow the user to upload a CSV file
# st.file_uploader creates a widget that lets users upload files.
# The 'type' parameter restricts the upload to CSV files only.
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Check if a file has been uploaded by the user
if uploaded_file is not None:
    # If a file is uploaded, read it into a Pandas DataFrame.
    # pd.read_csv() is the standard way to load CSV data into a DataFrame.
    try:
        df = pd.read_csv(uploaded_file)

        # Display the first few rows of the DataFrame to give the user an idea of the data.
        # st.subheader creates a smaller heading for this section.
        st.subheader("Data Preview")
        # st.dataframe displays the DataFrame in an interactive table format.
        st.dataframe(df)

        # Now, let's allow the user to choose which columns to plot.
        # We'll provide a dropdown (select box) for X-axis and Y-axis.

        # Get a list of column names from the DataFrame.
        # These will be used as options in our dropdown menus.
        column_names = df.columns.tolist()

        # Create a select box for the X-axis.
        # st.selectbox displays a dropdown. The first argument is the label, and the second is the list of options.
        x_axis_column = st.selectbox("Select X-axis column", column_names)

        # Create a select box for the Y-axis.
        # We do the same for the Y-axis.
        y_axis_column = st.selectbox("Select Y-axis column", column_names)

        # Now, let's create the plot if both X and Y columns are selected.
        # This condition ensures we don't try to plot before the user makes selections.
        if x_axis_column and y_axis_column:
            st.subheader("Data Visualization")

            # Create a Matplotlib figure and axes.
            # plt.figure() creates a new figure.
            # fig.add_subplot(111) adds a subplot to the figure. 111 means a 1x1 grid, first subplot.
            fig, ax = plt.subplots()

            # Create a scatter plot.
            # ax.scatter() plots points. It takes the X and Y data from our DataFrame columns.
            # We label the axes for better understanding.
            ax.scatter(df[x_axis_column], df[y_axis_column])
            ax.set_xlabel(x_axis_column)
            ax.set_ylabel(y_axis_column)
            ax.set_title(f"Scatter Plot of {y_axis_column} vs {x_axis_column}")

            # Display the Matplotlib plot in Streamlit.
            # st.pyplot() renders a Matplotlib figure.
            st.pyplot(fig)

    except Exception as e:
        # If there's an error reading the CSV (e.g., incorrect format), display an error message.
        st.error(f"Error reading CSV file: {e}")

# Example Usage:
# To run this app:
# 1. Save the code as a Python file (e.g., `data_viz_app.py`).
# 2. Make sure you have Streamlit, Pandas, and Matplotlib installed:
#    pip install streamlit pandas matplotlib
# 3. Open your terminal or command prompt.
# 4. Navigate to the directory where you saved the file.
# 5. Run the command: streamlit run data_viz_app.py
# 6. A web browser window will open with your application.
# 7. Click the "Browse files" button to upload a CSV file and see the visualization.

# For testing, you can create a simple CSV file named 'sample_data.csv' with content like:
# x,y,category
# 1,10,A
# 2,12,B
# 3,15,A
# 4,11,C
# 5,13,B