import sqlite3

#query the DB and return all records
def show_all():
    #connect to database and create cursor
    conn = sqlite3.connect('customer.db')
    #create a cursor
    c = conn.cursor()
    #query the database
    c.execute("SELECT rowid, *FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

        #commit and close connection
    conn.commit()
    conn.close()



# add a new record to table
def add_one(first, last, email):
    #connect to database2
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute("INSERT INTO customers VALUES(?,?,?)", (first, last, email))

    #close connection and commit
    conn.commit()
    conn.close()

# delete a record from the table
def delete_one(id):
    #connect connection to db
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    # delete id from database
    c.execute("DELETE from customers WHERE rowid = (?)", id)



    # commit and close
    conn.commit()
    conn.close()
