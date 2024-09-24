from fastapi import FastAPI
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

app = FastAPI()
DATABASE_URL = "postgresql://postgres:postgres@db/northwind"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.get("/customers")
def read_customers():
    db = SessionLocal()
    result = db.execute(text("SELECT customer_id, company_name, contact_name FROM customers LIMIT 10"))
    customers = [{"customer_id": row[0], "company_name": row[1], "contact_name": row[2]} for row in result]
    db.close()
    return {"customers": customers}
