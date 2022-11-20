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
<title>刪除商品</title>
</head>
<body>
""")

#查詢
form = cgi.FieldStorage()
id=form.getvalue('i')

if (bool(id)):#表格必填
    chknum=ml.chkItem(id)#存在為1 不存在為0
    if chknum==1:
        ml.MdelItem(id)
        print("""
        <script language="javascript">
        alert('商品已刪除!');window.location.href='MListItem.py';</script>
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
    alert('請輸入商品編號!');window.location.href='MListItem.py';</script>
    </script>
    """)
    
#print("<br><a href='MListItem.py'>回商品清單</a>")
print("</body></html>")



