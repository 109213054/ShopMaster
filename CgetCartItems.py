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
<title>購物車</title>
<style>
    body{
        margin: 30px auto;
        background-color: #e0dcd9;
        width: 700px;
    }
    #buy{
        margin: 30px auto;
        background-color: white;
        width: 700px;
        border: solid #8f8681 5px;
    }
    #update{
        position: absolute;
        left: 20px;
        top: 10px;
        width:300px;
        background-color: white;
        padding: 10px;
        border: solid #8f8681 5px;
    }
    #del{
        position: absolute;
        right: 20px;
        top: 10px;
        width:300px;
        background-color: white;
        padding: 10px;
        border: solid #8f8681 5px;
    }
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

<fieldset id="update">
<legend>更改購物車</legend>
<form method="post" action="CeditCart.py">
輸入要變更的商品號碼: <input type='text' name='i'><br/>
此商品總共買幾件: <input type='int' name='num'>
<input class="button" type="submit" value="提交">
</form>
</fieldset>

<fieldset id="del">
<legend>取消購買</legend>
<form method="post" action="CdelCart.py">
輸入商品編號 <input type='text' name='i'>
<input class="button" type="submit" value="提交">
</form>
</fieldset>
""")
#只要定義好函數(變成物件)
clList=ml.getCart()
print("""
<fieldset id="buy">
<legend>購物清單</legend>
""")

for (id,name,price,inventory,pnum) in clList:
	print(f"<p>商品編號{id}: 商品名稱:{name} 單價:{price} 庫存量:{inventory} 購買數量:{pnum} </p>")

print("""
</fieldset>
<input class="button" type="button" value="結帳" onclick="location.href='Cout.py'">
<input class="button" type="button" value="回商品清單" onclick="location.href='CListItem.py'">
</body></html>
""")

