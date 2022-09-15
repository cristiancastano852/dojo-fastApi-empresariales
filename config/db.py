from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql://postgres_user_test:postgres_password_test@localhost:5433/store_db_test")
meta = MetaData()
conn = engine.connect()