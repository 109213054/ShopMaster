#!C:\Users\julia\AppData\Local\Programs\Python\Python310\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import mitemlist as ml
#連線DB
from dbConfig import conn, cur
#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>存入成功</title>
</head>
<body>
""")

#查詢
form = cgi.FieldStorage()
name=form.getvalue('name')
price=form.getvalue('price')
inventory=form.getvalue('inventory')

chknum=ml.chkstr(name,price,inventory)

if chknum==0:#商品資訊都有輸入正確的話就可新增

    ml.MaddItem(name,price,inventory)
    print("""
    <script language="javascript">
    alert('新商品已存入!');window.location.href='MListItem.py';</script>
    </script>
    """)
else:
    print("""
    <script language="javascript">
    alert('商品新增失敗，請填寫正確資訊');window.location.href='MListItem.py';</script>
    </script>
    """)

print("</body></html>")

