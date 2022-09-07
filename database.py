##conn = psycopg2.connect(
##host="localhost",
##database="database-1",
##user="postgres",
##password="Vale1714!")


# import packages
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
  
# establish connections
conn_string = 'postgres://postgres:pass@localhost/master'
  
db = create_engine(conn_string)
conn = db.connect()
conn1 = psycopg2.connect(
    database="Database-1",
  user='postgres', 
  password='Vale1714!', 
  host='localhost', 
  port= '5432'
)
  
conn1.autocommit = True
cursor = conn1.cursor()
  
# drop table if it already exists
cursor.execute('drop table if exists master')
  
sql = '''CREATE TABLE master(country VARCHAR,
year_ INT,
sex VARCHAR,
agE INT,
suicides_no	INT,
population VARCHAR,
suicides100k_pop INT,
country_year VARCHAR,
hdi_for_year INT,
gdp_for_year INT,
gdp_per_capita INT,
generation VARCHAR);'''
  
cursor.execute(sql)
  
# import the csv file to create a dataframe
data = pd.read_csv("master.csv")
  
# Create DataFrame
print(data)
  
# converting data to sql
data.to_sql('master', conn, if_exists= 'replace')
  
# fetching all rows
sql1='''select * from master;'''
cursor.execute(sql1)
for i in cursor.fetchall():
    print(i)
  
conn1.commit()
conn1.close()