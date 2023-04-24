import streamlit as sl
import pandas as pd
import plotly_express as px

df = pd.read_csv('./data/vehicles_us.csv')
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

# Convert date column to datetime type
df['date'] = pd.to_datetime(df['date_posted'])
# Extract day of the week from date column
df['day_of_week'] = df['date'].dt.day_name()

# Create a list of unique condition values
conditions = df['condition'].unique().tolist()

# Add checkboxes to the sidebar for each condition
checkboxes = []
for condition in conditions:
    checkbox = sl.sidebar.checkbox(f'Show only {condition} cars')
    checkboxes.append(checkbox)

# Create a function that filters the data based on checkbox values
def filter_data(df, checkboxes):
    filtered_df = df.copy()
    for i, checkbox in enumerate(checkboxes):
        if checkbox:
            filtered_df = filtered_df[filtered_df['condition'] == conditions[i]]
    return filtered_df

# Filter the data based on the checkbox values
filtered_df = filter_data(df, checkboxes)

# Make Header above dataframe
sl.header('Data Viewer')
# display df with streamlit
sl.dataframe(filtered_df)

# set the app title
sl.title('Dropdown Menus')

all_cols = sorted(filtered_df.columns.unique())
# A the dropdown menus
x_axis_col = sl.selectbox('Select X-axis', all_cols, index=all_cols.index('price'))
y_axis_col = sl.selectbox('Select Y-axis/Color', all_cols, index=all_cols.index('condition'))

# A the scatter plot
fig_custom_sp = px.scatter(filtered_df, x=x_axis_col, y=y_axis_col)
fig_custom_hg = px.histogram(filtered_df, x=x_axis_col, color=y_axis_col)

# display the plot
sl.title('Scatter Plot')
sl.write(fig_custom_sp)
sl.title('Histogram')
sl.write(fig_custom_hg)

# A Line Chart
fig_lc = px.line(filtered_df, x='model_year', y='price', title='Average Car Price Over Time', color='condition')

# A scatter plot
fig_sp = px.scatter(filtered_df, x='odometer', y='price', title='Price vs. Odometer', color='condition')

# A bar chart
fig_bc = px.bar(filtered_df, x='fuel', title='Count of Cars by Fuel Type', color='condition')

# A histogram
fig_hg = px.histogram(filtered_df, x='price', title='Distribution of Car Prices', color='condition')

# A box plot
fig_bp = px.box(filtered_df, x='manufacturer', y='price', title='Price by Car Manufacturer', color='condition')

# A heatmap
fig_hm = px.density_heatmap(filtered_df, x='fuel', y='transmission', z='price', title='Average Price by Fuel and Transmission')

# A treemap
fig_tm = px.treemap(filtered_df, path=['manufacturer', 'model'], title='Count of Cars by Make and Model', color='condition')

# A polar chart
fig_pc = px.line_polar(filtered_df, r='price', theta='day_of_week', line_close=True, title='Average Car Price by Day of Week', color='condition')

# A 3D surface plot
fig_3dsp = px.scatter_3d(filtered_df, x='odometer', y='model_year', z='price', title='Price vs. Odometer and Model Year', color='condition')

sl.write(fig_lc)
sl.write(fig_sp)
sl.write(fig_bc)
sl.write(fig_hg)
sl.write(fig_bp)
sl.write(fig_hm)
sl.write(fig_tm)
sl.write(fig_pc)
sl.write(fig_3dsp)