import pymysql
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             database='py',
                             charset='utf8')
try:
    with connection.cursor() as cursor:
        sql = 'select name, userid from user where userid > %(id)s'
        cursor.execute(sql, {'id': 0})

        result_set = cursor.fetchall()
        for row in result_set:
            print('id:{0} - name : {1}'.format(row[1], row[0]))
finally:
    connection.close()