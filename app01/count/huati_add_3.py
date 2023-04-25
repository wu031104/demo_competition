import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='wdl_01', charset='utf8')

# 建立游标
cursor = conn.cursor()

# 数据库操作
# (1)定义一个格式化的sql语句

# 读取数据
list16 = []
res = cursor.execute("select jiji from app01_feel_analyse_result")
for i in cursor.fetchall():
    for j in i:
        list16.append(j)
print(list16)
# 提交事务
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()


conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='wdl_01', charset='utf8')

# 建立游标
cursor = conn.cursor()

# 数据库操作
# (1)定义一个格式化的sql语句

# 读取数据
list17 = []
res = cursor.execute("select zhongxing from app01_feel_analyse_result")
for i in cursor.fetchall():
    for j in i:
        list17.append(j)
print(list17)
# 提交事务
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()


conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='wdl_01', charset='utf8')

# 建立游标
cursor = conn.cursor()

# 数据库操作
# (1)定义一个格式化的sql语句

# 读取数据
list18 = []
res = cursor.execute("select xiaoji from app01_feel_analyse_result")
for i in cursor.fetchall():
    for j in i:
        list18.append(j)
print(list18)
# 提交事务
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()


conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='wdl_01', charset='utf8')

# 建立游标
cursor = conn.cursor()

# 数据库操作
# (1)定义一个格式化的sql语句

# 读取数据
list19 = []
res = cursor.execute("select jiji from app01_feel_analyse_result_2")
for i in cursor.fetchall():
    for j in i:
        list19.append(j)
print(list19)
# 提交事务
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()



conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='wdl_01', charset='utf8')

# 建立游标
cursor = conn.cursor()

# 数据库操作
# (1)定义一个格式化的sql语句

# 读取数据
list20 = []
res = cursor.execute("select zhongxing from app01_feel_analyse_result_2")
for i in cursor.fetchall():
    for j in i:
        list20.append(j)
print(list20)
# 提交事务
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()


conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='wdl_01', charset='utf8')

# 建立游标
cursor = conn.cursor()

# 数据库操作
# (1)定义一个格式化的sql语句

# 读取数据
list21 = []
res = cursor.execute("select xiaoji from app01_feel_analyse_result_2")
for i in cursor.fetchall():
    for j in i:
        list21.append(j)
print(list21)
# 提交事务
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()


conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='wdl_01', charset='utf8')

# 建立游标
cursor = conn.cursor()

# 数据库操作
# (1)定义一个格式化的sql语句

# 读取数据
list22 = []
res = cursor.execute("select jiji from app01_feel_analyse_result_3")
for i in cursor.fetchall():
    for j in i:
        list22.append(j)
print(list22)
# 提交事务
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()


conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='wdl_01', charset='utf8')

# 建立游标
cursor = conn.cursor()

# 数据库操作
# (1)定义一个格式化的sql语句

# 读取数据
list23 = []
res = cursor.execute("select zhongxing from app01_feel_analyse_result_3")
for i in cursor.fetchall():
    for j in i:
        list23.append(j)
print(list23)
# 提交事务
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()


conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='wdl_01', charset='utf8')

# 建立游标
cursor = conn.cursor()

# 数据库操作
# (1)定义一个格式化的sql语句

# 读取数据
list24 = []
res = cursor.execute("select xiaoji from app01_feel_analyse_result_3")
for i in cursor.fetchall():
    for j in i:
        list24.append(j)
print(list24)
# 提交事务
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()



jiji_add=int(list16[0])+int(list19[0])+int(list22[0])
zhongxing_add=int(list17[1])+int(list20[1])+int(list23[1])
xiaoji_add=int(list18[2])+int(list21[2])+int(list24[2])


conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='wdl_01', charset='utf8')

# # 建立游标
cursor = conn.cursor()

# # 数据库操作
# # (1)定义一个格式化的sql语句

sql = 'insert into app01_huati_add_3(f_j, f_z, f_x, g_j, g_z, g_x, h_j, h_z, h_x, jiji_add, zhongxing_add, xiaoji_add) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
# # 读取数据
# for i in range(len(nums)):
#     data = (jiji,zhongxing,xaioji,nums[1][i],nums[0][i],list1[1],list2[i],list3[i],list4[i],list5[i],list6[i],list7[i])
data = (list16[0],list17[0],list18[0],list19[0],list20[0],list21[0],list22[0],list23[0],list24[0],jiji_add,zhongxing_add,xiaoji_add)
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