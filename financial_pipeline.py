import random
from datetime import datetime
from postgres_crud import upsert_batch,query_recent,insert_single


def simulate_costco_crawler():
    """模擬真實爬蟲:Costco->shopee 利潤"""
    products = [
        ('TX_COSTCO_001',1250.50,'success','costco',0.3025),
        ('TX_SHOPEE_001',890.75,'pending','shopee',0.2150),
        ('TX_PXMART_001',450.00,'failed','pxmart',0.1),
    ]
    return products + [(f"TX_{random.randint(100,999)}_{datetime.now().strftime('%H%M')}",
                       round(random.uniform(200,1500),2),
                       random.choice(['success','pending']),
                       random.choice(['costco','shopee']),
                       round(random.uniform(0.1,0.4),4)) for _ in range(5)]

if __name__ == "__main__":
    print("最近交易：", query_recent())

    insert_single(('TX_SAFE_001', 500.00, 'success', 'python', 0.2))

    print("新增後：", query_recent())