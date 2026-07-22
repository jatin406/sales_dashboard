import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set overall seaborn theme
sns.set_theme(style="whitegrid")

# 1. Load Data
df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

# 2. Calculate and Print Top Key Metrics (KPIs)
total_sales = df["Total_Sales"].sum()
total_units = df["Quantity"].sum()
avg_order_val = df["Total_Sales"].mean()
total_orders = len(df)

print("="*40)
print("📊 SALES DASHBOARD KPIs")
print("="*40)
print(f"Total Revenue:      ${total_sales:,.0f}")
print(f"Units Sold:         {total_units:,}")
print(f"Avg Order Value:    ${avg_order_val:,.2f}")
print(f"Total Transactions: {total_orders}")
print("="*40)

# 3. Create a 2x2 Dashboard Figure
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle("Sales Trends, Customer Behavior & Product Performance", fontsize=18, fontweight='bold', y=0.98)

# --- Top Left: Sales Trend Over Time (Line Chart) ---
daily_sales = df.groupby("Date")["Total_Sales"].sum().reset_index()
sns.lineplot(
    data=daily_sales, 
    x="Date", 
    y="Total_Sales", 
    marker="o", 
    ax=axes[0, 0],
    color="#2b5c8f"
)
axes[0, 0].set_title("Revenue Timeline", fontsize=14)
axes[0, 0].tick_params(axis='x', rotation=45)
axes[0, 0].set_ylabel("Total Sales")

# --- Top Right: Regional Sales Breakdown (Donut Chart via Matplotlib) ---
# Seaborn doesn't do pie charts natively, so we use matplotlib
region_sales = df.groupby("Region")["Total_Sales"].sum()
axes[0, 1].pie(
    region_sales, 
    labels=region_sales.index, 
    autopct='%1.1f%%', 
    startangle=90,
    wedgeprops={'width': 0.4, 'edgecolor': 'w'} # width creates the donut hole
)
axes[0, 1].set_title("Revenue Share by Region", fontsize=14)

# --- Bottom Left: Price vs. Quantity Sold (Scatter Plot) ---
sns.scatterplot(
    data=df, 
    x="Price", 
    y="Quantity", 
    hue="Product", 
    alpha=0.7,
    s=100,
    ax=axes[1, 0]
)
axes[1, 0].set_title("Price vs Quantity Analysis", fontsize=14)

# --- Bottom Right: Product Performance Comparison (Bar Chart) ---
prod_sales = df.groupby("Product")["Total_Sales"].sum().reset_index().sort_values(by="Total_Sales", ascending=False)
sns.barplot(
    data=prod_sales, 
    x="Product", 
    y="Total_Sales", 
    hue="Product", 
    legend=False, # Avoids the warning about passing palette without hue
    ax=axes[1, 1],
    palette="viridis"
)
axes[1, 1].set_title("Sales by Product Category", fontsize=14)
axes[1, 1].set_ylabel("Total Sales")

# Adjust layout and display
plt.tight_layout()
plt.subplots_adjust(top=0.92) # Leave space for main title
plt.show()