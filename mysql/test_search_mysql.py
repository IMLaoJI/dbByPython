import MySQLdb

class MysqlSearch(object):
    def __init__(self):
        self.get_conn()

    def get_conn(self):
        # 获取连接
        try:
            self.conn = MySQLdb.connect(
                host='localhost',
                user='root',
                passwd='root',
                db='bookstore',
                port=3306,
                charset='utf8'
            )
        except MySQLdb.Error as e:
            print('Error: %s' % e)

    def close_conn(self):
        try:
            if self.conn:
                self.conn.close()
        except MySQLdb.Error as e:
            print('Error: %s' % e)


    def get_one(self):
        # 准备SQL
        sql = 'SELECT * FROM `user_student` where `nickname` = %s '
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行sql
        cursor.execute(sql,('luoyu',))
        # 拿到结果
        # rest = cursor.fetchone()
        rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        # 处理数据
        # 关闭cursor/连接
        cursor.close()
        self.close_conn()
        return rest


    def get_more(self):
        # 准备SQL
        sql = 'SELECT * FROM `user_student` where `nickname` = %s '
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行sql
        cursor.execute(sql, ('luoyu',))
        # 拿到结果
        # rest = cursor.fetchone()
        rest = [dict(zip([k[0] for k in cursor.description],row))
            for row in cursor.fetchall()]
        # 处理数据
        # 关闭cursor/连接
        cursor.close()
        self.close_conn()
        return rest


def main():
    obj = MysqlSearch()
    # obj.get_one()
    rest = obj.get_more()
    for item in rest:
        print(item['name'])
if __name__ == '__main__':
    main()