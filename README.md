# 📊 E-Commerce Sales Insights Dashboard

## 🚀 Project Overview
This project leverages **SQL, Pandas, and Streamlit** to analyze e-commerce sales data, providing insights into trends, revenue distribution, and top-performing products/categories. The objective is to enhance decision-making using data-driven strategies.

       ![GRAPH](images/GRAPH.png)

---

## 📂 Technologies Used
- **SQL** (Data Extraction & Analysis)
- **Pandas** (Data Cleaning & Processing)
- **Streamlit** (Interactive Dashboard & Visualization)
- **Matplotlib** (Additional Data Visualizations)

---

## 🔍 Key Features & Insights

### 1️⃣ Data Extraction & Preprocessing
- Queries sales data from an SQLite database.
- Filters data **from 2023 onwards** for relevant insights.
- Computes **total sales** for each product.

### 2️⃣ Top 5 Best-Selling Categories
- Aggregates revenue per category.
- Orders categories based on **highest total sales**.
- Uses **bar charts** for visual representation.

### 3️⃣ Monthly Revenue Trend Analysis
- Extracts **monthly revenue trends** using `strftime('%Y-%m', order_date)`.
- Generates **interactive line charts** for visualization.

### 4️⃣ Automated Business Reports
- Summarizes **key sales insights**.
- Stores results in `sales_report.txt`.
- Uses **Streamlit alerts** to notify users.

---

## 📊 Sample SQL Queries

### ✅ Best-Selling Categories Query
```sql
SELECT category, SUM(quantity * unit_price) AS total_revenue
FROM sales_data
GROUP BY category
ORDER BY total_revenue DESC
LIMIT 5;
```

### ✅ Monthly Revenue Trend Query
```sql
SELECT strftime('%Y-%m', order_date) AS month,
       SUM(quantity * unit_price) AS total_revenue
FROM sales_data
GROUP BY month
ORDER BY month;
```

---

## 🏗️ Future Enhancements
✅ Implement **predictive analytics** using Machine Learning 🤖  
✅ Add **real-time data updates** for dashboards 🔄  
✅ Optimize SQL queries for faster performance 🚀

---

## 📎 How to Run the Project
1️⃣ **Clone the Repository**:  
```sh
git clone https://github.com/your-repo/ecommerce-sales-dashboard.git
```

2️⃣ **Install Dependencies**:  
```sh
pip install pandas sqlite3 streamlit matplotlib
```

3️⃣ **Run the Streamlit Dashboard**:  
```sh
streamlit run app.py
```

---

## 🌟 Connect With Me
🚀 [LinkedIn](https://www.linkedin.com/in/your-profile)  
📂 [GitHub](https://github.com/your-repo)  
💬 **#DataAnalytics #SQL #Pandas #Streamlit #EcommerceInsights**

