import database2

# add a record to the database
#database2.add_one("marvin","ev","me@gmex.com")

# delete record use rowid as string
database2.delete_one('6')

database2.show_all()
