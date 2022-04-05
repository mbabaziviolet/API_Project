
import psycopg2
import psycopg2.extras


conn = psycopg2.connect( host="localhost",   database="users",user='postgres', password='@joy1')

#Open a cursor to perform database operations
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#Insert data into the table
cur.execute("""
            
            INSERT INTO orders (order_id,order_quantity,order_name,order_date) VALUES ('9','3','meat','9/04/2022')
          
            """)
conn.commit()
cur.close()
