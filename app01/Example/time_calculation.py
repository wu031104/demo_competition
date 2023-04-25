import jieba
import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', user='root', password='123456', database='xyxsql1', charset='utf8')
#
# # 建立游标
cursor = conn.cursor()
#
# # 数据库操作
# # (1)定义一个格式化的sql语句
a=0
b=0
c=0
d=0
# # 读取数据
try:
    sql = "select * from menghuan"
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in range(len(data)):
        print(type(str(data[0][8])))
        if str(data[i][8])[0:4] == '2019':
            a+=1
        elif str(data[i][8])[0:4] == '2020':
            b+=1
        elif str(data[i][8])[0:4] == '2021':
            c+=1
        elif str(data[i][8])[0:4] == '2022':
            d+=1
    print(a)
    print(b)
    print(c)
    print(d)
    cursor.close()
except Exception as e:
    print('未正常查询', e)
    conn.rollback()  # 回滚

conn = MySQLdb.connect(host='127.0.0.1', user='root', password='123456', database='xyxsql1', charset='utf8')
#
# # 建立游标
cursor = conn.cursor()
sql = 'insert into menghuannums(nums) values(%s)'
# # 读取数据
list1 = []
list1.append(a)
list1.append(b)
list1.append(c)
list1.append(d)
print(list1)
for i in range(4):
    data = (list1[i],)
    try:
        cursor.execute(sql, data)
        conn.commit()
    except Exception as e:
        print('插入数据失败', e)
        conn.rollback()  # 回滚
#
# # 关闭游标
cursor.close()
#
# # 关闭连接
conn.close()