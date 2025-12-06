import pandas as pd
from sqlalchemy import create_engine
import os
from datetime import datetime

# -------- CONFIG --------
DB_USER = "postgres"
DB_PASS = "long5671"  
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "bank_dw"

# Đường dẫn file CSV
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CUSTOMER_CSV = os.path.join(BASE_DIR, "customer.csv")
TRANSACTION_CSV = os.path.join(BASE_DIR, "transaction.csv")
LOAN_CSV = os.path.join(BASE_DIR, "loan.csv")

# -------- MAIN FUNCTION --------
def main():
    print(f"\n🚀 ETL started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # 1️⃣ Đọc file CSV
    dim_customer = pd.read_csv(CUSTOMER_CSV)
    fact_transaction = pd.read_csv(TRANSACTION_CSV)
    fact_loan = pd.read_csv(LOAN_CSV)

    # 2️⃣ Làm sạch dữ liệu cơ bản
    dim_customer.drop_duplicates(subset='customer_id', inplace=True)

    if 'full_name' in dim_customer.columns:
        dim_customer['full_name'] = dim_customer['full_name'].astype(str).str.title()

    if 'region' in dim_customer.columns:
        dim_customer['region'] = dim_customer['region'].astype(str).str.upper()

    if 'age' in dim_customer.columns:
        def age_group(age):
            try:
                a = int(age)
                if a < 25: return 'Young'
                elif a < 45: return 'Adult'
                else: return 'Senior'
            except:
                return None
        dim_customer['age_group'] = dim_customer['age'].apply(age_group)

    # 3️⃣ Kết nối tới PostgreSQL
    engine = create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # 4️⃣ Nạp dữ liệu vào schema bank_dw
    dim_customer.to_sql('dim_customer', engine, schema='bank_dw', if_exists='replace', index=False)
    fact_transaction.to_sql('fact_transaction', engine, schema='bank_dw', if_exists='replace', index=False)
    fact_loan.to_sql('fact_loan', engine, schema='bank_dw', if_exists='replace', index=False)

    print("✅ Dữ liệu đã được nạp thành công vào PostgreSQL!")
    print(f"🏁 ETL finished at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
