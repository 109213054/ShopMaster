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
<title>加入購物車</title>
</head>
<body>
""")

#查詢
form = cgi.FieldStorage()
id=form.getvalue('i')#商品編號
num=form.getvalue('num')#購買的數量
inv=ml.chkinv(id,num)#庫存量


if (bool(id)&bool(num)):#表單不可留白
    chknum=ml.chkItem(id)#id存在為1不存在為0
    if (chknum==1):#id存在
        if int(inv)>=int(num):
            ml.Caddnum(id,num)
            print("""
            <script language="javascript">
            alert('商品新增成功!');window.location.href='CListItem.py';</script>
            </script>
            """)
        else:#庫存量小於購買量
            print("""
            <script language="javascript">
            alert('庫存量不足，加入失敗!');window.location.href='CListItem.py';</script>
            </script>
            """)
    else:
        print("""
        <script language="javascript">
        alert('id不存在!');window.location.href='CListItem.py';</script>
        </script>
        """)
else:
    print("""
    <script language="javascript">
    alert('欄位不可留白!');window.location.href='CListItem.py';</script>
    </script>
    """)

print("<br><a href='CListItem.py'>回商品清單</a>")
print("</body></html>")
