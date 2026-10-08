import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load the data
df = pd.read_csv("sales_analytics_dataset-1.xls")

# Convert date
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Title
st.title("📊 Sales Analytics Dashboard")
st.write("Explore sales, profit and regional performance.")

# Sidebar
st.sidebar.header("🔎 Filters")

regions = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

categories = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

# Date filter
min_date = df["Order_Date"].min().date()
max_date = df["Order_Date"].max().date()

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Get selected dates
start_date = pd.to_datetime(date_range[0])
end_date = pd.to_datetime(date_range[-1])

# Apply filters
filtered_df = df[
    (df["Region"].isin(regions)) &
    (df["Category"].isin(categories)) &
    (df["Order_Date"] >= start_date) &
    (df["Order_Date"] <= end_date)
]

# KPIs
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order_ID"].nunique()
total_quantity = filtered_df["Quantity"].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("📈 Total Profit", f"${total_profit:,.2f}")
col3.metric("🛒 Total Orders", f"{total_orders:,}")
col4.metric("📦 Quantity Sold", f"{total_quantity:,}")

st.divider()
# -----------------------------
# Monthly Sales Trend
# -----------------------------
st.subheader("📈 Monthly Sales Trend")

monthly_sales = (
    filtered_df
    .groupby(filtered_df["Order_Date"].dt.to_period("M"))["Sales"]
    .sum()
)

# Convert period to string for Streamlit
monthly_sales.index = monthly_sales.index.astype(str)

st.line_chart(monthly_sales)

# Sales by Category
st.subheader("📦 Sales by Category")

sales_by_category = (
    filtered_df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(sales_by_category)

# Sales by Region
st.subheader("🌍 Sales by Region")

sales_by_region = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(sales_by_region)