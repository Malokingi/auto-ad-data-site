import streamlit as sl
import pandas as pd
import plotly_express as px

df = pd.read_csv('./data/processed_vehicles_us.csv')
# df['make'] = df['model'].apply(lambda x: x.split()[0])

# Convert date column to datetime type
df['date'] = pd.to_datetime(df['date_posted'])
# Extract day of the week from date column
df['day_of_week'] = df['date'].dt.day_name()

filtered_df = df.copy()

makes = sorted(df['make'].unique().tolist())

for i, m in enumerate(makes):
    makes[i] = m

sl.sidebar.markdown("## Show these makes \n(if none are selected, All makes will show)")

# Add checkboxes to the sidebar for each make
checkboxes = []
for m in makes:
    checkbox = sl.sidebar.checkbox(f'Show {m.upper()} cars')
    checkboxes.append(checkbox)

# Create a function that filters the data based on selected values
def filter_data_by_make(df, checkboxes):
    filtered_df = df.copy()
    selected_makes = []

    for i, checkbox in enumerate(checkboxes):
        if checkbox:
            selected_makes.append(makes[i])
    
    if selected_makes:
        filtered_df = filtered_df[filtered_df['make'].isin(selected_makes)]
    
    return filtered_df

# Add multiselect to the sidebar for the condition column
conditions = ['new', 'like new', 'excellent', 'good', 'fair', 'salvage']
sl.sidebar.markdown("## Show these Conditions \n(if none are selected, All Conditions will show)")

selected_conditions = sl.sidebar.multiselect('Filter by one or more conditions:', conditions)

# Create a function that filters the data based on selected values
def filter_data_by_condition(df, column, checkboxes, selected_values):
    filtered_df = filter_data_by_make(df, checkboxes)
    if selected_values:
        filtered_df = filtered_df.loc[filtered_df[column].isin(selected_values)]
    
    return filtered_df

sl.sidebar.markdown("## Show these Graphs")

# Create checkboxes to allow the user to choose which charts to display
show_hg = sl.sidebar.checkbox('Show Histogram of Distribution of Car Prices by Condition', True)
show_sp = sl.sidebar.checkbox('Show Scatter Plot of Price vs. Mileage by Contition', True)
show_lc = sl.sidebar.checkbox('Show Line Chart of Average Car Price by Model Year by Condition', False)
show_bc = sl.sidebar.checkbox('Show Bar Chart of Count of Cars by Fuel Type and Condition', False)
show_bp = sl.sidebar.checkbox('Show Box and Whisker Plot of Price by Car make and Condition', False)
show_hm = sl.sidebar.checkbox('Show Heatmap of Average Price by Fuel Type and Transmission', False)
show_tm = sl.sidebar.checkbox('Show Treemap of Count of Cars by Make and Model', False)
show_pc = sl.sidebar.checkbox('Show Polar Chart of Average Car Price by Day of Week and Condition', False)
show_3dsp = sl.sidebar.checkbox('Show 3D Surface Plot of Price vs. Odometer, Model Year, and Condition', False)

# Make Header above dataframe
sl.header('Car Sales Data Results')

# Filter the data based on the selected values
if sl.sidebar.button('Render'):
    filtered_df = filter_data_by_condition(df, 'condition', checkboxes, selected_conditions)

    if show_hg:
        # A histogram
        fig_hg = px.histogram(filtered_df, x='price', title='Histogram of Distribution of Car Prices by Condition', color='condition')
        sl.write(fig_hg)
    if show_sp:
        # A scatter plot
        fig_sp = px.scatter(filtered_df, x='odometer', y='price', title='Scatter Plot of Price vs. Mileage by Contition', color='condition')
        sl.write(fig_sp)
    # Some Optional Graphs (it takes a long time to render all at once every time, so I added the option 
    # to show or hide them to the sidebar)
    if show_lc:
        # A Line Chart
        fig_lc = px.line(filtered_df, x='year', y='price', title='Line Chart of Average Car Price by Model Year by Condition', color='condition')
        sl.write(fig_lc)
    if show_bc:
        # A bar chart
        fig_bc = px.bar(filtered_df, x='fuel_type', title='Bar Chart of Count of Cars by fuel Type and Condition', color='condition')
        sl.write(fig_bc)
    if show_bp:
        # A box plot
        fig_bp = px.box(filtered_df, x='make', y='price', title='Box and Whisker Plot of Price by Car make and Condition', color='condition')
        sl.write(fig_bp)
    if show_hm:
        # Calculate the average price by fuel_type and transmission
        df_agg = df.pivot_table(index='fuel_type', columns='transmission', values='price', aggfunc='mean')

        # Create a heatmap
        fig_hm = px.imshow(df_agg, x=df_agg.columns, y=df_agg.index, color_continuous_scale='Blues', title='Heatmap of Average Price by Fuel Type and Transmission')
        sl.write(fig_hm)
    if show_tm:
        # A treemap
        fig_tm = px.treemap(filtered_df, path=['make', 'model'], title='Treemap of Count of Cars by Make and Model')
        sl.write(fig_tm)
    if show_pc:
        # A polar chart
        fig_pc = px.line_polar(filtered_df, r='price', theta='day_of_week', line_close=True, title='Polar Chart of Average Car Price by Day of Week and Condition', color='condition')
        sl.write(fig_pc)
    if show_3dsp:
        # A 3D surface plot
        fig_3dsp = px.scatter_3d(filtered_df, x='odometer', y='year', z='price', title='3D Surface Plot of Price vs. Odometer, Model Year, and Condition', color='condition')
        sl.write(fig_3dsp)
else:
    sl.write('Click the "Render" button to display the data and charts.')