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
#many_customers =[('Wes','Brown', 'wes@brown.com'),('Wes','Brown', 'wes@brown.com'),('Wes','Brown', 'wes@brown.com'),]
#c.execute("INSERT INTO customers VALUES (?,?,?)", many_customers)

#c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

#queryall
c.execute("SELECT * FROM customers")
#c.fetchone()
#c.fetchmany(3)
#c.fetchall()
print(c.fetchall())

#commit our commond
conn.commit()

#close our connection
conn.close()
