

import psycopg2
import psycopg2.extras

def get_db():
    
  conn = psycopg2.connect( host="localhost",   database="FastFood",user='postgres', password='@joy1')

#Opening a cursor to perform database operations
  cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Inserting data into the table
  cur.execute("""
            
            INSERT INTO customer (cst_id,cst_name,cst_email,cst_gender,cst_address,cst_contact) VALUES ('10','Nabatanzi Gorret','nabb@gmail.com','female','Mengo','0776574523')
          
            """)
  conn.commit()
  
  cur.close()

