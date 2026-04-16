# Financial Data Pipeline

📌 **專案介紹**
本專案使用 Python 與 PostgreSQL 建立自動化的資料處理管線（Data Pipeline），模擬從爬蟲獲取資料後，高效且安全地寫入資料庫的流程。

---

## 🔧 技術
- **語言**: Python 3.x
- **資料庫**: PostgreSQL
- **驅動程式**: `psycopg2`,'python-dotenv'

---

## 🚀 核心功能
- 新增交易資料（INSERT）。
- 查詢最新交易（SELECT）。

---
## 🔒 安全設計
- 使用 .env 管理敏感資訊（資料庫密碼）。
- .gitignore 防止機密資料上傳。

---

## ▶️ 使用方式

1. **安裝依賴套件**:
   ```bash
   pip install -r requirements.txt

2. **設定環境變數**:
建立 .env 檔案：

DB_NAME=finance_db
DB_USER=postgres
DB_PASSWORD=你的密碼
DB_HOST=localhost
DB_PORT=5432

3. **執行**:

python pipeline.py