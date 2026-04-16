from dotenv import load_dotenv
import os 
import psycopg2
from pathlib import Path

load_dotenv()

# 1. 取得這份檔案 (db.py) 所在的目錄絕對路徑
current_dir = Path(__file__).resolve().parent
env_path = current_dir / ".env"

# 2. 載入檔案並加入 override=True
# 我們用變數 success 來確認到底有沒有讀到檔案
success = load_dotenv(dotenv_path=env_path, override=True)

if success:
    print("✅ 成功找到並載入 .env 檔案")
else:
    print(f"❌ 找不到 .env 檔案！請確認檔案是否存在於: {env_path}")

# 3. 測試輸出
print(f"DEBUG: DB_USER = {os.getenv('DB_USER')}")
print(f"DEBUG: DB_PASSWORD = {os.getenv('DB_PASSWORD')}")

DB_CONFIG={
    "dbname":os.getenv("DB_NAME"),
    "user":os.getenv("DB_USER"),
    "password":os.getenv("DB_PASSWORD"),
    "host":os.getenv("DB_HOST"),
    "port":os.getenv("DB_PORT"),
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)