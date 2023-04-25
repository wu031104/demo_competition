import paddlehub as hub
import pymysql



conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='wdl_01', charset='utf8')

# 建立游标
cursor = conn.cursor()

# 数据库操作
# (1)定义一个格式化的sql语句

# 读取数据
list1 = []
res = cursor.execute("select jiji from app01_remenzongyi_result")
for i in cursor.fetchall():
    for j in i:
        list1.append(j)
print(list1)
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
list2 = []
res = cursor.execute("select zhongxing from app01_remenzongyi_result")
for i in cursor.fetchall():
    for j in i:
        list2.append(j)
print(list2)
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
list3 = []
res = cursor.execute("select xiaoji from app01_remenzongyi_result")
for i in cursor.fetchall():
    for j in i:
        list3.append(j)
print(list3)
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
list4 = []
res = cursor.execute("select jiji from app01_mingxingbagua_result")
for i in cursor.fetchall():
    for j in i:
        list4.append(j)
print(list4)
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
list5 = []
res = cursor.execute("select zhongxing from app01_mingxingbagua_result")
for i in cursor.fetchall():
    for j in i:
        list5.append(j)
print(list5)
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
list6 = []
res = cursor.execute("select xiaoji from app01_mingxingbagua_result")
for i in cursor.fetchall():
    for j in i:
        list6.append(j)
print(list6)
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
list7 = []
res = cursor.execute("select jiji from app01_shehuiredian_result")
for i in cursor.fetchall():
    for j in i:
        list7.append(j)
print(list7)
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
list8 = []
res = cursor.execute("select zhongxing from app01_shehuiredian_result")
for i in cursor.fetchall():
    for j in i:
        list8.append(j)
print(list8)
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
list9 = []
res = cursor.execute("select xiaoji from app01_shehuiredian_result")
for i in cursor.fetchall():
    for j in i:
        list9.append(j)
print(list9)
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
list10 = []
res = cursor.execute("select jiji from app01_tiyusaishi_result")
for i in cursor.fetchall():
    for j in i:
        list10.append(j)
print(list10)
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
list11 = []
res = cursor.execute("select zhongxing from app01_tiyusaishi_result")
for i in cursor.fetchall():
    for j in i:
        list11.append(j)
print(list11)
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
list12 = []
res = cursor.execute("select xiaoji from app01_tiyusaishi_result")
for i in cursor.fetchall():
    for j in i:
        list12.append(j)
print(list12)
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
list13 = []
res = cursor.execute("select jiji from app01_meishilvyou_result")
for i in cursor.fetchall():
    for j in i:
        list13.append(j)
print(list13)
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
list14 = []
res = cursor.execute("select zhongxing from app01_meishilvyou_result")
for i in cursor.fetchall():
    for j in i:
        list14.append(j)
print(list14)
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
list15 = []
res = cursor.execute("select xiaoji from app01_meishilvyou_result")
for i in cursor.fetchall():
    for j in i:
        list15.append(j)
print(list15)
# 提交事务
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()



a_j = list1[0]  # 热门综艺
a_z = list2[0]
a_x = list3[0]
b_j = list4[0]  # 明星八卦
b_z = list5[0]
b_x = list6[0]
c_j = list7[0]  # 社会热点
c_z = list8[0]
c_x = list9[0]
d_j = list10[0]  # 体育赛事
d_z = list11[0]
d_x = list12[0]
e_j = list13[0]  # 美食旅游
e_z = list14[0]
e_x = list15[0]

jiji_add=int(a_j)+int(b_j)+int(c_j)+int(d_j)+int(e_j)
zhongxing_add=int(a_z)+int(b_z)+int(c_z)+int(d_z)+int(e_z)
xiaoji_add=int(a_x)+int(b_x)+int(c_x)+int(d_x)+int(e_x)
all_add=jiji_add+zhongxing_add+xiaoji_add

conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='wdl_01', charset='utf8')

# # 建立游标
cursor = conn.cursor()

# # 数据库操作
# # (1)定义一个格式化的sql语句

sql = 'insert into app01_huati_add_5(a_j, a_z, a_x, b_j, b_z, b_x, c_j, c_z, c_x, d_j, d_z, d_x, e_j, e_z, e_x, jiji_add, zhongxing_add, xiaoji_add,all_add) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
# # 读取数据
# for i in range(len(nums)):
#     data = (jiji,zhongxing,xaioji,nums[1][i],nums[0][i],list1[1],list2[i],list3[i],list4[i],list5[i],list6[i],list7[i])
data = (list1[0],list2[0],list3[0],list4[0],list5[0],list6[0],list7[0],list8[0],list9[0],list10[0],list11[0],list12[0],list13[0],list14[0],list15[0],jiji_add,zhongxing_add,xiaoji_add,all_add)
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
