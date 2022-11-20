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
<title>刪除購買商品</title>
</head>
<body>
""")

#查詢
form = cgi.FieldStorage()
id=form.getvalue('i')

if (bool(id)):#表格必填
    chkCart=ml.chkCart(id)#判斷此id存不存在
    if (chkCart==1):#id存在
            ml.CdelItem(id)
            print("""
            <script language="javascript">
            alert('移除成功!');window.location.href='CListItem.py';</script>
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
    alert('請輸入編號!');window.location.href='CgetCartItems.py';</script>
    </script>
    """)
    
print("<br><a href='CgetCartItems.py'>回購物車</a>")
print("</body></html>")

