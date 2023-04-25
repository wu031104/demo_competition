# # 获取token
# import urllib
# import urllib.request
# import json
# #client_id 为官网获取的AK， client_secret 为官网获取的SK
# client_id = 'VnHMRsIuf7m9jizQowE7V7q6'
# client_secret = 'pS8WU8QbSWdT41BLE4nM5eGwRkyRvqbx'
#
# #获取token
# def get_token():
#     host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret
#     request = urllib.request.Request(host)
#     request.add_header('Content-Type', 'application/json; charset=UTF-8')
#     response = urllib.request.urlopen(request)
#     token_content = response.read()
#     if token_content:
#         token_info = json.loads(token_content)
#         token_key = token_info['access_token']
#     return token_key
#
#
# # 获取人脸融合结果
#
# def face_detect_emotion(url):
#     request_url = 'https://aip.baidubce.com/rest/2.0/face/v3/detect'
#     params = dict()
#     params['image'] = url
#     params['image_type'] = 'URL'
#     params['face_field'] = 'emotion'
#
#     params = json.dumps(params).encode('utf-8')
#
#     access_token = get_token()
#     request_url = request_url + "?access_token=" + access_token
#     request = urllib.request.Request(url=request_url, data=params)
#     request.add_header('Content-Type', 'application/json')
#     response = urllib.request.urlopen(request)
#     content = response.read()
#     if content:
#         print (content)
#         content = content.decode('utf-8')
#         data = json.loads(content)
#         print (data)
#         return data['result']['face_list'][0]['emotion']
#     else:
#         return ''
# image_url='https://dimg03.c-ctrip.com/images/01A2f1200098x971c0D26_W_640_10000.jpg?proc=autoorient'
# print (face_detect_emotion(image_url))



# 获取token
import urllib
import urllib.request
import json
import MySQLdb
import time

#client_id 为官网获取的AK， client_secret 为官网获取的SK
client_id = 'VnHMRsIuf7m9jizQowE7V7q6'
client_secret = 'pS8WU8QbSWdT41BLE4nM5eGwRkyRvqbx'

emotions=[]
#获取token
def get_token():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    global Max_Num
    Max_Num = 10
    for i in range(Max_Num):
        try:
            response = urllib.request.urlopen(request)
            token_content = response.read()
            if token_content:
                token_info = json.loads(token_content)
                token_key = token_info['access_token']
        except:
            if i < Max_Num - 1:
                continue
            else:
                print('URLError: <urlopen error timed out> All times is failed ')
    # if token_content:
    #     token_info = json.loads(token_content)
    #     token_key = token_info['access_token']
    return token_key


# 获取人脸融合结果

def face_detect_emotion(url):
    request_url = 'https://aip.baidubce.com/rest/2.0/face/v3/detect'
    params = dict()
    params['image'] = url
    params['image_type'] = 'URL'
    params['face_field'] = 'emotion'

    params = json.dumps(params).encode('utf-8')

    access_token = get_token()
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request)
    content = response.read()
    if content:
        # print (content)
        content = content.decode('utf-8')
        data = json.loads(content)
        # print (data)
        return data['result']['face_list'][0]['emotion']
    else:
        return ''

neutral = []
sad = []
grimace = []
happy = []
suprise = []
fear = []
angry = []
pouty = []
disgust = []
w=0
conn = MySQLdb.connect(host='127.0.0.1', user='root', password='123456', database='xyxsql1', charset='utf8')
cursor = conn.cursor()
# str1 = ''
res = cursor.execute("select hrefs from imagehrefs")
# print(len(cursor.fetchall()))
for i in cursor.fetchall():
    for j in i:
        # str1+=j
        # print(j)
        image_url = j
        try:
            emotions.append(face_detect_emotion(image_url)['type'])
            print(emotions)
            # if (face_detect_emotion(j)['type'])=='neutral':
            #     neutral.append('neutral')
            #
            # elif (face_detect_emotion(j)['type'])=='sad':
            #     sad.append('sad')
            #
            # elif (face_detect_emotion(j)['type'])=='grimace':
            #     grimace.append('grimace')
            #
            # elif (face_detect_emotion(j)['type'])=='happy':
            #     happy.append('happy')
            #
            # elif (face_detect_emotion(j)['type'])=='suprise':
            #     suprise.append('suprise')
            #
            # elif (face_detect_emotion(j)['type'])=='fear':
            #     fear.append('fear')
            #
            # elif (face_detect_emotion(j)['type'])=='angry':
            #     angry.append('angry')
            #
            # elif (face_detect_emotion(j)['type'])=='pouty':
            #     pouty.append('pouty')
            #
            # else:
            #     a+=1

        except (TypeError,KeyError):
            print('图片中没有人脸')
        w = w+1
        print(w)
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
h = 0
g = 0
z = 0
for emotion in emotions:
    if emotion == 'neutral':
        a = a + 1
    if emotion == 'sad':
        b = b + 1
    if emotion == 'grimace':
        c = c + 1
    if emotion == 'happy':
        d = d + 1
    if emotion == 'suprise':
        e = e + 1
    if emotion == 'fear':
        f = f + 1
    if emotion == 'angry':
        h = h + 1
    if emotion == 'pouty':
        g = g + 1
    if emotion == 'disgust':
        z = z + 1
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(h)
print(g)
print(z)
list1 = []
list1.append(a)
list1.append(b)
list1.append(c)
list1.append(d)
list1.append(e)
list1.append(f)
list1.append(h)
list1.append(g)
list1.append(z)

conn.commit()
cursor.close()
conn.close()
# print(len(neutral))
# print(len(sad))
# print(len(grimace))
# print(len(happy))
# print(len(suprise))
# print(len(fear))
# print(len(angry))
# print(len(pouty))


# image_url='https://dimg03.c-ctrip.com/images/0306k120009c494mu3EE3_W_640_10000.jpg?proc=autoorient'
# # emotions.append(face_detect_emotion(image_url)['type'])
# # print(emotions)
# try:
#     emotions.append(face_detect_emotion(image_url)['type'])
#     print(emotions)
# except TypeError:
#     print('图片中没有人脸')

conn = MySQLdb.connect(host='127.0.0.1', user='root', password='123456', database='xyxsql1', charset='utf8')
#
# # 建立游标
cursor = conn.cursor()
#
# # 数据库操作
# # (1)定义一个格式化的sql语句

sql = 'insert into imagelabels(hrefs) values(%s)'
# # 读取数据
for i in range(9):
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