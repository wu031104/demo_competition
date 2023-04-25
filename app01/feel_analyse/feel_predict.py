import paddlehub as hub
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='wdl_01', charset='utf8')

# 建立游标
cursor = conn.cursor()

# 数据库操作
# (1)定义一个格式化的sql语句

# 读取数据
list1 = []
res = cursor.execute("select content from app01_lianghui_search")
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
res = cursor.execute("select content from app01_lianghui_search")
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

# 经过测试后，大部分lstm》bilstm》cnn
senta = hub.Module(name="senta_lstm")
test_text = list1
results = senta.sentiment_classify(texts=test_text)
nums = []

for result in results:
    print(result['text'])
    print(result['sentiment_label'])
    print(result['sentiment_key'])
    print(type(result['sentiment_key']))
    print(result['positive_probs'])
    print(result['negative_probs'])
    nums.append(result['text', 'sentiment_label', 'sentiment_key', 'positive_probs', 'negative_probs'])

conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='wdl_01', charset='utf8')
#
# # 建立游标
cursor = conn.cursor()
#
# # 数据库操作
# # (1)定义一个格式化的sql语句

sql = 'insert into app01_feel_analyse_2(text,sentiment_label,sentiment_key,positive_probs,negative_probs) values(%s,%s,%s,%s,%s)'
# # 读取数据
for i in range(len(nums)):
    data = (nums[i], list2[i])
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
