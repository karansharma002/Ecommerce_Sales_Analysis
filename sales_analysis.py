import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Connect to the database
db_connection = sqlite3.connect("ecommerce_sales.db")

# Fetch sales data for analysis 
ecom_sales_data = pd.read_sql("""
    SELECT 
        order_id, 
        order_date, 
        product_name, 
        category, 
        quantity, 
        unit_price, 
        (quantity * unit_price) AS total_sales
    FROM sales_data
    WHERE order_date >= '2023-01-01';
""", db_connection)

# Quick check 
st.write("### Sample Sales Data")
st.dataframe(ecom_sales_data.head())

# Fetch total sales per category
category_sales = pd.read_sql("""
    SELECT category, SUM(quantity * unit_price) AS total_revenue
    FROM sales_data
    GROUP BY category
    ORDER BY total_revenue DESC
    LIMIT 5;
""", db_connection)

st.write("### Top 5 Best-Selling Categories")
st.bar_chart(category_sales.set_index("category"))


# Monthly revenue trend analysis 
monthly_revenue = pd.read_sql("""
    SELECT strftime('%Y-%m', order_date) AS month, 
           SUM(quantity * unit_price) AS total_revenue
    FROM sales_data
    GROUP BY month
    ORDER BY month;
""", db_connection)

st.write("### 📊 Monthly Revenue Trend")
st.line_chart(monthly_revenue.set_index("month"))


#Step 4: Automating Business Reports 


# Generate automated summary report 
def generate_sales_report():
    summary = f"""
    E-Commerce Sales Report 
    ==================================
    🏆 Top Category: {category_sales.iloc[0]['category']}
    💰 Highest Monthly Revenue: ${monthly_revenue['total_revenue'].max()}
    🛍️ Total Orders Analyzed: {len(ecom_sales_data)}
    """
    
    with open("sales_report.txt", "w", encoding="utf-8") as report_file:
        report_file.write(summary)
    
    st.success("✅ Report Generated: sales_report.txt")

generate_sales_report()