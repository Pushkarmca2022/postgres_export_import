import pandas as pd
from sqlalchemy import create_engine
database_url = ""
engine = create_engine(database_url)
data = pd.read_sql_query('SELECT * FROM "Document"', con=engine)
df = pd.DataFrame(data)
df
row = df.loc[38:38]
row
database_url = "postgresql+psycopg2://postgres:12345@localhost:5432/flow"

engine = create_engine(database_url)
row.to_sql('Document', con=engine, if_exists='append', index=False)
