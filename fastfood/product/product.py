

import psycopg2
import psycopg2.extras

conn = psycopg2.connect( host="localhost",   database="users",user='postgres', password='@joy1')

#Open a cursor to perform database operations
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Insert data into the table
cur.execute("""
            
            INSERT INTO product (product_id,product_name,product_price,product_description,product_image_url) VALUES ('9','pork','$16','fresh','url')
          
            """)
conn.commit()
cur.close()
