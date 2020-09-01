import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='manu141198' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quan, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='manu141198' host='localhost' port='5432'")
    cur = conn.cursor()
    #cur.execute("INSERT INTO store VALUES('%s', '%s', '%s')" % (item, quan, price)) This is prone to SQL injection errors, instead pass them as another parameter to the execute function as shown in the next line.
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quan, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='manu141198' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * from store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='manu141198' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,)) #Any item added and if the rest two are empty then a comma is a must 
    conn.commit()
    conn.close()


def update(item, quant, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='manu141198' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quant, price, item))
    conn.commit()
    conn.close() 

create_table()
insert("Apple", 15, 130)
insert("Banana", 2, 60)
delete("Apple")
print(view())