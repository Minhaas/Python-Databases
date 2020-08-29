import sqlite3

conn = sqlite3.connect("new.db")
cur = conn.cursor()

def create_insert_delete(item, quan, price):
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quan, price))
    cur.execute("SELECT * FROM store")
    row = cur.fetchall()
    return row

def delete(newItem):
    cur.execute("DELETE FROM store WHERE item=?",(newItem,))
    cur.execute("SELECT * FROM store")
    rowDel = cur.fetchall()
    return rowDel

getItem = input("Enter the item name: ")
getPrice = float(input("Enter the Price: "))
getQty = int(input("Enter the quantity: "))

print(create_insert_delete(getItem, getPrice, getQty))

getDelete = input("Enter item to be deleted: ")
print(delete(getDelete))

def update(item, quantity, price):
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity, price, item))
    row = cur.fetchall()
    return row

updateItem = input("Enter the Item name to be updated: ")
updateQuan = input("Enter the updated quantity: ")
updatePrice = input("Enter the updated price: ")

print(update(updateItem, updateQuan, updatePrice))

conn.commit()
conn.close()