import dbutil


DATABASE = "C:/sqlite/TutorialsSampleDB"
if __name__ == '__main__':
    dbutil = dbutil.DBUtil(DATABASE)
    query = 'select * from students where StudentName like ?'
    args=['J%']
    print (dbutil.query_db(query, args, one=False))

