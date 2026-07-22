# 📊 Interactive Sales Performance & Statistical Analysis Dashboard

An end-to-end data processing, exploratory data analysis (EDA), and graphical reporting suite built using **Python**, **Pandas**, **Seaborn**, and **Matplotlib**. This repository contains a modular analytical pipeline designed to parse transactional sales datasets, execute statistical distribution checks, compute business KPIs, and render publication-grade dashboard visualizations.

---

## 📌 Project Overview

Analyzing raw transactional data requires identifying hidden patterns across product categories, pricing strategies, and regional demand. This project transforms unstructured e-commerce transaction logs into actionable business intelligence through a automated data pipeline and a clean **2×2 visual report frame**:

* **Key Performance Indicators (KPIs)**: Tracks total revenue, total units sold, average order value (AOV), and total transaction volume.
* **Sales Trend Over Time**: Line plot capturing revenue fluctuations and demand seasonality.
* **Regional Sales Breakdown**: Donut chart representing regional revenue share.
* **Price vs. Quantity Analysis**: Multi-variable scatter plot highlighting pricing strategy dynamics and purchasing patterns across products.
* **Product Category Performance**: Ranked bar chart visualizing overall revenue contribution by product.

---

## 📁 Repository Structure

```text
├── sales_data.csv          # Raw sales dataset (100 records)
├── dashboard.ipynb         # Jupyter Notebook with exploratory data analysis
├── dashboard.py        # Main Python script to generate the dashboard
├── requirements.txt        # Frozen dependency environment file
├── visualizations/         # Exported chart artifacts
│   └── dashboard_grid.png  # High-DPI composite dashboard output
└── README.md               # Technical project documentation
