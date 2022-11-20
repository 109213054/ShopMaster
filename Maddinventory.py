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
<title>增加商品庫存</title>
</head>
<body>
""")

#查詢
form = cgi.FieldStorage()
id=form.getvalue('id')
num=form.getvalue('num')

if (bool(id)&bool(num)):
    chknum = ml.chkItem(id)
    if chknum==1:
        ml.MaddInv(id,num)
        #print(f"{id}號商品 庫存更新成功!")
        print("""
        <script language="javascript">
        alert('庫存更新成功!');window.location.href='MListItem.py';</script>
        </script>
        """)
    else:
        print("""
        <script language="javascript">
        alert('此id不存在!');window.location.href='MListItem.py';</script>
        </script>
        """)
else:
    print("""
    <script language="javascript">
    alert('請填寫正確的資訊');window.location.href='MListItem.py';</script>
    </script>
    """)
   
print("<br><a href='MListItem.py'>回商品清單</a>")
print("</body></html>")


