import psycopg2
from psycopg2.extras import execute_values
import os
import logging
from contextlib import contextmanager
from db import get_connection

#READ: 最近交易
def query_recent(limit=5):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
            select transaction_id,amount,status,source_system,created_at
            from financial_logs
            order by created_at DESC LIMIT %s
            """,(limit,))
            return cur.fetchall()

#insert :單筆
def insert_single(tx_data):
    """tx_data=(transaction_id,amount,status,source_system,profit_margin)"""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                insert into financial_logs(transaction_id,amount,status,source_system,profit_margin)
                values (%s,%s,%s,%s,%s)        
            """,tx_data)
            conn.commit()

def upsert_batch(transactions):
    """transactions=[('TX001',1250.50,'success','costco',0.3025),...]"""
    unique_transactions = list({tx[0]: tx for tx in transactions}.values())
    with get_connection() as conn:
        with conn.cursor() as cur:
            upsert_sql="""
            insert into financial_logs(transaction_id,amount,status,source_system,profit_margin)
            values %s
            ON CONFLICT (transaction_id) do update set
                amount=excluded.amount,
                status=excluded.status,
                profit_margin=excluded.profit_margin,
                updated_at=Current_timestamp
            """

            #批次插入(100一批)
            execute_values(cur, upsert_sql, unique_transactions, page_size=100)
            conn.commit()
            print(f"upsert {len(transactions)}筆交易")
#測試重複更新
test_data=[
    ('TX_UPSERT_001',1000.00,'pending','costco',0.20),
    ('TX_UPSERT_001',1200.00,'success','costco',0.30),#更新!
    ('TX_UPSERT_002',850.50,'success','shopee',0.25),
]

upsert_batch(test_data)
print("UPSERT結果:",query_recent(3))

if __name__=="__main__":
    # 1. 查詢目前狀態
    print("目前最新交易:", query_recent(3))
    
    # 2. 使用批次 Upsert 來處理單筆，這樣重複執行也不會報錯
    single_data = [('TX_PYTHON_001', 999.99, 'success', 'python', 0.25)]
    upsert_batch(single_data)
    
    print("執行完畢。")