import requests,json
from urllib.parse import  quote,unquote
import sys
import connector
class conn():

  mydb = connector.connect(
  host="192.168.0.102",
  port= 3336,
  user="root1",
  passwd="root1",
  database="TD_OA",
  auth_plugin='mysql_native_password' #要加上这个东东才行
)
 

def im_discuss_group(str):
  a=conn()
  mycursor=a.mydb.cursor()
  sql="select * from im_discuss_group where DISC_GROUP_NAME like'%s'"%str
  sql="select * from im_discuss_group where DISC_GROUP_NAME like'%{}%'".format(str)
  # print(sql)
  mycursor.execute(sql)
  rs=mycursor.fetchall()
  # print(rs)
  head=[]
  for item in mycursor.description:
    head.append(item[0])
  # print(head)
  alldata=[]

  for tupitem in rs:
    n=0
    objdate={}
    for item in tupitem:
        objdate[head[n]]=item
        n=n+1
    alldata.append(objdate)

  # print(alldata)
  list=[]
  for mydata in alldata:
    data = {'DISC_GROUP_NAME':mydata.get("DISC_GROUP_NAME"),'REMARK':mydata.get("REMARK"),'TO_ID':mydata.get("DISC_GROUP_UID"),'TO_NAME':'','DISC_GROUP_ID':mydata.get("DISC_GROUP_ID"),'submit':'保存'}
    list.append(data)




  session = requests.Session()
  form_data = {
      "UNAME": "admin",
      "PASSWORD": "Dnk8090",
      "encode_type": 1,
  }
  i2 = session.post('http://192.168.0.101/logincheck.php', data=form_data)
  c2 = i2.cookies.get_dict()
  str=""
  for key,d in c2.items():
      str=str+key+"="+d+";"
  headers = {
      'Cookie':str,
      'Host': '192.168.0.101',
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
      'Referer': 'http://192.168.0.101/general/status_bar/sms_back.php?I_VER=2&type=mac&C=Web'
  }
  print(list)
  for data in list:
# data = {'DISC_GROUP_NAME':'验厂工资讨论群5.28','REMARK':'1','TO_ID':'448,423,1013,807,1124,1541,960,','TO_NAME':'','DISC_GROUP_ID':'38140','submit':'保存'}
      r = requests.post( r'http://192.168.0.101/general/sms/ls_group/update.php', headers=headers,data=data)
  
  print(r)
  

im_discuss_group("验厂工资讨论群5.28")