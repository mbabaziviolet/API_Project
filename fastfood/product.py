

import psycopg2
import psycopg2.extras


conn = psycopg2.connect( host="localhost",   database="Products",user='postgres', password='@joy1')

#Open a cursor to perform database operations
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Insert data into the table
cur.execute("""
            
            INSERT INTO product (food_id,food_name,food_price,food_quantity) VALUES ('9','pork','$16','3kg')
          
            """)
conn.commit()
cur.close()
