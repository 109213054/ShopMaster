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
<title>個別出貨</title>
</head>
<body>
""")

#查詢
form = cgi.FieldStorage()
id=form.getvalue('i')

if (bool(id)):#表格必填
    chkOut=ml.chkOut(id)#判斷此id存不存在
    if (chkOut==1):#id存在
            ml.MeachOut(id)
            print("""
            <script language="javascript">
            alert('出貨成功!');window.location.href='MListItem.py';</script>
            </script>
            """)
    else:
        print("""
        <script language="javascript">
        alert('此商品不在購物車內!');window.location.href='MListItem.py';</script>
        </script>
        """)
else:
    print("""
    <script language="javascript">
    alert('請輸入編號!');window.location.href='MListItem.py';</script>
    </script>
    """)
    
print("""
</body></html>
""")


