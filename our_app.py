import database2

# add a record to the database
#database2.add_one("marvin","ev","me@gmex.com")

# delete record use rowid as string
#database2.delete_one('6')


# add many records
stuff =[
    ('brenda','smiter','brenda@smiter.com'),
    ('jake','dumas','jakedumas@gmex.com')
]


database2.add_many(stuff)

database2.show_all()
