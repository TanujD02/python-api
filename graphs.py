import plotly.express as px
import pandas as pd
import plotly.io as pio

# 1. KPI data - These are dummy values that you can later replace with real data
def get_kpi_values():
    kpi_data = {
        "Total Sales": 15000,  # Example KPI: Total Sales in a period
        "New Users": 1200,      # Example KPI: Number of new users
        "Conversion Rate": 8.5, # Example KPI: Conversion Rate (%)
        "Revenue Growth": 25    # Example KPI: Revenue Growth (%)
    }
    return kpi_data

# 2. Bar Chart (Sales over time)
def bar_chart():
    data = {"Month": ["Jan", "Feb", "Mar", "Apr", "May"], "Sales": [1000, 1500, 2000, 1700, 500]}
    df = pd.DataFrame(data)
    fig = px.bar(df, x="Month", y="Sales", title="Sales Over Time")
    return pio.to_html(fig, full_html=False)

# 3. Pie Chart (Market Share)
def pie_chart():
    data = {"Category": ["A", "B", "C", "D"], "Market Share": [30, 40, 20, 10]}
    df = pd.DataFrame(data)
    fig = px.pie(df, names="Category", values="Market Share", title="Market Share Distribution")
    return pio.to_html(fig, full_html=False)

# 4. Categorical Bar Chart (Sales by Category)
def categorical_bar_chart():
    data = {"Category": ["Electronics", "Clothing", "Home Goods", "Toys"], "Sales": [5000, 4000, 3500, 2500]}
    df = pd.DataFrame(data)
    fig = px.bar(df, x="Category", y="Sales", title="Sales by Category", color="Category")
    return pio.to_html(fig, full_html=False)

# 5. Table (Product Information)
def product_table():
    data = {
        "Product": ["Product A", "Product B", "Product C", "Product D"],
        "Price": [100, 150, 120, 80],
        "Stock": [200, 150, 120, 300]
    }
    df = pd.DataFrame(data)
    table_html = df.to_html(classes='table table-striped table-bordered')
    return table_html

# 6. Line Chart (Sales Trend)
def line_chart():
    data = {"Month": ["Jan", "Feb", "Mar", "Apr", "May"], "Sales": [1000, 1500, 2000, 1700, 2100]}
    df = pd.DataFrame(data)
    fig = px.line(df, x="Month", y="Sales", title="Sales Trend")
    return pio.to_html(fig, full_html=False)

# 7. Bubble Chart (Sales vs. Region)
def bubble_chart():
    data = {"Region": ["North", "South", "East", "West"], "Sales": [1000, 2000, 1500, 1800], "Size": [30, 60, 40, 50]}
    df = pd.DataFrame(data)
    fig = px.scatter(df, x="Region", y="Sales", size="Size", color="Region", title="Sales vs. Region")
    return pio.to_html(fig, full_html=False)
