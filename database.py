#OM NAMAHSHYA SHIVAYA
#DATABASE
import sqlite3
#conn = sqlite3.connect("database.db")
#c = conn.cursor()
#c.execute("UPDATE users SET mail = 'mayankraj3313@gmail.com'  WHERE rowid = 7")
#c.execute("SELECT * FROM users WHERE rowid= 7 ")
#items = (c.fetchall())
#for item in items:
      #print(item)
#conn.commit()
#conn.close()
def search(rowid):
   conn = sqlite3.connect("database.db")
   c = conn.cursor()
   c.execute("SELECT * FROM users WHERE rowid= ? ",(rowid,))
   items = (c.fetchall())
   for item in items:
        return item[2]
   conn.commit()
   conn.close()
def name(rowid):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE rowid= ? ",(rowid,))
    items = (c.fetchall())
    for item in items:
          return (item[0]+" " +item[1])
    conn.commit()
    conn.close()
def balance(rowid):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE rowid= ? ",(rowid,))
    items = (c.fetchall())
    for item in items:
          return (item[3])
    conn.commit()
    conn.close()
def update(balance,rowid):
     conn = sqlite3.connect("database.db")
     c = conn.cursor()
     c.execute("UPDATE users SET balance = ? WHERE rowid = ?",(balance,rowid))
     conn.commit()
     conn.close()
def update_pin(pin_no,rowid):
      conn = sqlite3.connect("database.db")
      c = conn.cursor()
      c.execute("UPDATE users SET pin_no = ? WHERE rowid = ?",(pin_no,rowid))
      conn.commit()
      conn.close()
def email(rowid):
     conn = sqlite3.connect("database.db")
     c = conn.cursor()
     c.execute("SELECT * FROM users WHERE rowid = ? ",(rowid,))
     items = c.fetchall()
     for item in items:
             return (item[4])
     conn.commit()
     conn.close()
def phone_no(rowid):
     conn = sqlite3.connect("database.db")
     c = conn.cursor()
     c.execute("SELECT * FROM users WHERE rowid = ? ",(rowid,))
     items = c.fetchall()
     for item in items:
             return (item[5])
     conn.commit()
     conn.close()
def mini_statement(date,time,amount,balance,id):
     conn = sqlite3.connect("database.db")
     c = conn.cursor()
     c.execute("INSERT INTO statement VALUES (?,?,?,?,?)",(date,time,amount,balance,id))
     conn.commit()
     conn.close()
def showdata(id):
     conn = sqlite3.connect("database.db")
     c = conn.cursor()
     c.execute("SELECT rowid, * FROM statement WHERE id = ? ORDER BY rowid DESC LIMIT 5",(id,))
     items = c.fetchall()
     a = ""
     for item in items:
               a = str(item[1] +"\t       "+item[2] +"\t                 Rs."+str(item[3])+"\t                    Rs."+str(item[4]) +"\n" + a)
     return(a)           
     conn.commit()
     conn.close()
def transfer(balance,account_no):
     conn = sqlite3.connect("database.db")
     c = conn.cursor()
     c.execute("UPDATE users SET balance = ? WHERE rowid = ?",(balance,account_no))
     c.execute("SELECT * FROM users WHERE rowid= ? ",(account_no,))
     items = (c.fetchall())
     for item in items:
          return (item[0]+" " +item[1])
     conn.commit()
     conn.close()
#conn = sqlite3.connect("database.db")
#c = conn.cursor()
#c.execute("""CREATE TABLE statement (
                 #date text,
                 #time text,
                 #amount integer,
                 #balance integer,
                 #id integer)
                    # """)
#conn.commit()
#conn.close()

