# Learning Objective:
# This tutorial will teach you how to create interactive data visualizations
# that tell a story using the Python libraries Pandas for data manipulation
# and Plotly for creating dynamic and explorable charts.
# We will focus on a single, common data analysis task:
# exploring trends over time in a dataset and highlighting specific events.

# Import necessary libraries
# Pandas is essential for handling and manipulating data in a structured way.
# We'll use it to load, clean, and prepare our data for visualization.
import pandas as pd

# Plotly is our tool for creating beautiful, interactive visualizations.
# Specifically, we'll use `plotly.express` which is a high-level API
# that makes it very easy to create common chart types quickly.
import plotly.express as px

# --- Data Preparation ---
# For this tutorial, let's create a simple, fictional dataset.
# In a real-world scenario, you would load your data from a CSV, Excel,
# database, or API using `pd.read_csv()`, `pd.read_excel()`, etc.

# Create a dictionary to hold our sample data.
# This simulates data you might get from a real-world source.
data = {
    'Date': pd.to_datetime(['2023-01-01', '2023-01-15', '2023-02-01', '2023-02-20',
                           '2023-03-10', '2023-03-25', '2023-04-05', '2023-04-20',
                           '2023-05-01', '2023-05-15', '2023-06-01', '2023-06-20',
                           '2023-07-05', '2023-07-20', '2023-08-01', '2023-08-15',
                           '2023-09-10', '2023-09-25', '2023-10-05', '2023-10-20']),
    'MetricA': [10, 12, 15, 14, 18, 20, 22, 21, 25, 26, 28, 27, 30, 32, 35, 33, 38, 40, 42, 41],
    'MetricB': [5, 6, 7, 6, 8, 9, 10, 9, 11, 12, 13, 12, 14, 15, 16, 15, 17, 18, 19, 18],
    'EventType': [None, None, None, 'Milestone A', None, None, None, 'Milestone B',
                  None, None, None, 'Milestone C', None, None, None, 'Milestone D',
                  None, None, None, None] # Placeholder for events
}

# Convert the dictionary into a Pandas DataFrame.
# DataFrames are the core data structure in Pandas, offering powerful ways
# to organize and analyze tabular data.
df = pd.DataFrame(data)

# --- Enhancing the Data for Narrative ---
# To tell a story, we often need to highlight specific points or events.
# Let's add a column that can be used to mark important dates.
# This column will help us later to add annotations to our plot.

# We can create a boolean column to identify rows where an EventType is not None.
# This is a common technique for filtering and highlighting data.
df['IsEvent'] = df['EventType'].notna()

# --- Creating the Interactive Visualization ---
# Now, let's use Plotly Express to create our visualization.
# We will create a line chart to show trends over time and use color
# and symbol to highlight events.

# `px.line` is a function that creates line charts.
# `data_frame`: Specifies the Pandas DataFrame to use.
# `x`: The column to use for the x-axis (our 'Date' column).
# `y`: The column(s) to use for the y-axis (we'll plot 'MetricA' and 'MetricB').
# `color`: We can use this to differentiate lines if we were plotting multiple
#          metrics. Here, we'll use it to highlight our 'IsEvent' column later.
# `symbol`: Similar to color, we can use different symbols for points.
# `hover_data`: Specifies additional columns to show when hovering over a point.
# `title`: The title of our chart, making it informative.
# `labels`: Renames axis labels for better readability.

fig = px.line(
    df,
    x='Date',
    y=['MetricA', 'MetricB'], # Plotting both metrics as separate lines
    color_discrete_map={'MetricA': 'blue', 'MetricB': 'green'}, # Assign specific colors
    symbol='IsEvent', # Use different symbols for rows where IsEvent is True
    symbol_sequence=['circle', 'diamond'], # Specify symbols for False and True respectively
    hover_data={'Date': '|%Y-%m-%d', 'MetricA': True, 'MetricB': True, 'EventType': True}, # Customize hover info
    title='Trends of MetricA and MetricB Over Time with Key Events',
    labels={'Date': 'Date', 'value': 'Metric Value', 'variable': 'Metric Type'} # Meaningful axis and legend labels
)

# --- Enhancing the Narrative: Annotations ---
# To make the story even clearer, let's add text annotations for our specific events.
# This directly points out what happened at certain points in time.

# We iterate through the DataFrame to find rows where 'IsEvent' is True.
for i, row in df.iterrows():
    if row['IsEvent']:
        # `fig.add_annotation` adds text labels to the plot.
        # `x`: The x-coordinate of the annotation (usually the date of the event).
        # `y`: The y-coordinate of the annotation. We'll place it slightly above
        #      the data point for better visibility.
        # `text`: The text to display (the 'EventType' in our case).
        # `showarrow`: Whether to draw an arrow pointing from the annotation to the point.
        # `arrowhead`: The style of the arrow head.
        # `ax`: The x-offset of the annotation's text box from the point.
        # `ay`: The y-offset of the annotation's text box from the point.
        fig.add_annotation(
            x=row['Date'],
            y=row[row['EventType'].replace('Milestone ', '')] if row['EventType'].startswith('Milestone') else row['MetricA'], # Try to place near the line, adjust as needed
            text=row['EventType'],
            showarrow=True,
            arrowhead=1,
            ax=20, # Adjust arrow position
            ay=-30 # Adjust arrow position
        )

# --- Improving Interactivity ---
# Plotly charts are interactive by default (zooming, panning, hovering).
# We can also customize other interactive features.
# For this tutorial, the default interactivity is sufficient to demonstrate
# how users can explore the data and see event details on hover.

# --- Displaying the Visualization ---
# `fig.show()` renders the interactive plot.
# In environments like Jupyter Notebooks or VS Code, this will display the
# plot directly. In a script, it might open in your default web browser.

# Example Usage:
# This section demonstrates how to use the code.
if __name__ == "__main__":
    print("Creating interactive data visualization...")
    # The `fig.show()` command will render the interactive plot.
    # You can then explore it by hovering over points, zooming, and panning.
    # The annotations will highlight the specific events.
    fig.show()
    print("Visualization displayed. Explore it in your browser or IDE.")

# End of Tutorial