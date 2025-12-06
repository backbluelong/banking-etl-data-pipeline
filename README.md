# banking-etl-data-pipeline
📦 Banking ETL Data Pipeline (PostgreSQL + Python)

Status: In Progress – Dashboard coming soon

🔍 1. Overview

This project simulates a mini Banking Data Warehouse and demonstrates the full ETL workflow using Python and PostgreSQL.
It includes data modeling, data cleaning, ETL pipeline development, SQL KPI calculation, and preparation for BI dashboards.

🗂 2. Project Architecture

Source → ETL (Python) → Data Warehouse (PostgreSQL) → Power BI

Schemas & tables:

dim_customer

fact_transaction

fact_loan

Data model: Star Schema
DW schema: bank_dw

⚙️ 3. Technologies Used
Component	Tool
Database	PostgreSQL
ETL	Python (pandas, SQLAlchemy)
Modeling	Star Schema
Visualization	Power BI (in progress)
SQL Analysis	PostgreSQL SQL
🔧 4. ETL Pipeline Steps
Extract

Load CSV files: customer.csv, transaction.csv, loan.csv.

Transform

Remove duplicates

Standardize date formats

Convert name to Title Case

Create age group segmentation

Clean region values

Validate NULL / duplicate checks

Load

Push final tables into PostgreSQL schema bank_dw

Replace or append modes supported

📊 5. SQL KPIs

The following KPIs were implemented:

1. Total Customers
SELECT COUNT(*) FROM bank_dw.dim_customer;

2. Active Customers

Based on having at least 1 transaction:

SELECT COUNT(DISTINCT customer_id)
FROM bank_dw.fact_transaction;

3. Monthly Revenue
SELECT DATE_TRUNC('month', txn_date) AS month,
       SUM(amount) AS revenue
FROM bank_dw.fact_transaction
GROUP BY 1;

4. Outstanding Loan Balance
SELECT SUM(loan_amount) AS total_loan
FROM bank_dw.fact_loan;

📊 6. Power BI Dashboard (Coming Soon)

Planned visuals:

Total Customers, Active Customers, Revenue, Loan KPIs

Revenue trend (monthly)

Customer segmentation

Loan distribution

📝 7. Folder Structure
```
banking-etl/
│── data/
│   ├── customer.csv
│   ├── transaction.csv
│   └── loan.csv
│── etl/
│   └── etl_load.py
│── sql/
│   └── bank_kpi.sql
│── README.md

✔️ 8. Status

ETL: ✔ Done

SQL Modeling: ✔ Done

KPI Queries: ✔ Done

Power BI Dashboard: In progress
