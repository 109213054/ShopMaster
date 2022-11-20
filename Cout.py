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
<title>結帳</title>
<style>
    body{
        margin: 30px auto;
        background-color: #e0dcd9;
        width: 700px;
    }
    #list{
        margin: 30px auto;
        width: 700px;
        border: solid;
    }
    fieldset{
        margin: 30px auto;
        background-color: white;
        width: 400px;
        border: solid #8f8681 5px;
    }
    div{text-align:center;}
    form{text-align:center;}
    .button {
        -webkit-transition-duration: 0.4s; /* Safari */
        transition-duration: 0.4s;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 10px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
     
    .button:hover {
        background-color: #8f8681; /*藍色*/
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 10px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
</style>
</head>
<body>
<fieldset>
<legend>確認要結帳了嗎?</legend>
<form method="post" action="Cpay.py">
一旦送出，將無法反悔
<input class="button" type="submit" value="確定">
</form>
</fieldset>
<div id="list">
<h2>結帳清單</h2><hr/>
""")
clList=ml.getCart()
for (id,name,price,inventory,pnum) in clList:
	print(f"<p>商品編號{id}: 商品名稱:{name} 單價:{price} 庫存量:{inventory} 購買數量:{pnum} </p>")
print("""
</div>
<div>
<input class="button" type="button" value="回商品清單" onclick="location.href='CListItem.py'">
<input class="button" type="button" value="回購物車" onclick="location.href='CgetCartItems.py'"></div>
</div>
</body></html>
""")


