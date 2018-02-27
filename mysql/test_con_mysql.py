import MySQLdb

# 获取连接
try:
    conn = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='root',
        db='bookstore',
        port=3306,
        charset='utf8'
    )
    # 获取数据
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user_student')
    rest = cursor.fetchone()
    print(rest)
except MySQLdb.Error as e:
    print('Error: %s' % e)
