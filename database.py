import sqlite3

conn = sqlite3.connect('customer.db')

#create cursor
c = conn.cursor()

#create a table
####
#c.execute(""" CREATE TABLE  customers (

#    first_name  text,
#    last_name  text,
#    email       text

#)""")
#
#
#many_customers =[('Wes','Brown', 'wes@brown.com'),
#('Wes','Brown', 'wes@brown.com'),
#('Wes','Brown', 'wes@brown.com'),]
#c.execute("INSERT INTO customers VALUES (?,?,?)", many_customers)

#c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

#queryall
#c.execute("SELECT rowid, * FROM customers")
#c.execute("SELECT  * FROM customers WHERE last_name = 'Brown'")
#c.execute("SELECT  * FROM customers WHERE email like '%codemy.com'")
#c.fetchone()
#c.fetchmany(3)
#c.fetchall()
#print(c.fetchall())
#print(c.fetchone()[1])

#items = c.fetchall()


#print(" Name " + "\t\t email")

#for item in items:
#    print(item[1] + "\t " + item[2]  + "\t" + item[0])


#update records

#c.execute("""DELETE from customers
#            WHERE rowid = 4

#""")




#c.execute("SELECT rowid,* FROM customers")
#c.execute("DELETE from customers WHERE rowid = 6")
#c.execute("SELECT rowid,* FROM customers")
#c.execute("SELECT rowid,* FROM customers ORDER BY  last_name DESC")
#c.execute("SELECT rowid,* FROM customers WHERE last_name LIKE 'Br%'  AND rowid = 5")

#drop table
#c.execute("DROP TABLE customers")
#conn.commit()






c.execute("SELECT rowid,* FROM customers ORDER BY last_name DESC LIMIT 4")
items = c.fetchall()

for item in items:
    print(item)



#commit our commond
conn.commit()


#close our connection
conn.close()
