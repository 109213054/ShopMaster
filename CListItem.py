#!C:\Users\julia\AppData\Local\Programs\Python\Python310\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
# 如果是要輸出中文，記得重新 encode
#ctypes.windll.user32.MessageBoxA(0, "內容".decode("utf-8").encode("big5"), "標題".decode("utf-8").encode("big5"), 1)

import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import mitemlist as ml#導入檔案mitemlist
#連線DB
from dbConfig import conn, cur
#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>商品列表</title>
<style>
    h1{text-align:center;}
    body{
        margin: 30px auto;
        background-color: #e0dcd9;
        width: 700px;
    }
    div{
        margin: 30px auto;
        background-color: white;
        width: 700px;
        border: solid #8f8681 5px;
        text-align:center;
    }
    fieldset{
        position: absolute;
        right: 20px;
        top: 10px;
        width:200px;
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
<fieldset>
<legend>加入購物車</legend>
<form method="post" action="CaddCart.py">
輸入商品號碼: <input type='text' name='i'><br/>
輸入加入數量:<input type='int' name='num'>
<input class="button" type="submit" value="提交">
</form>
</fieldset>
<div>
<h1>商品清單</h1><hr/>
""")

#只要定義好函數(變成物件)
clList=ml.getList()#呼叫ml.py裡的function:getList

for (id,name,price,inventory) in clList:
	print(f"<p>商品編號{id}: 商品名稱:{name} 單價:{price} 庫存量:{inventory}</p>")
    
print("""
</div>
<div>
<h1>依價格排序前三名</h1><hr/>
""")
#這個式助教叫我改的部分!
threeList=ml.three()
for (id,name,price,inventory) in threeList:
	print(f"<p>商品編號{id}: 商品名稱:{name} 單價:{price} 庫存量:{inventory}</p>")
    
print("""
</div>
<input class="button" type="button" value="點我回首頁" onclick="location.href='home.html'">
<input class="button" type="button" value="查看購物車" onclick="location.href='CgetCartItems.py'">
</body></html>
""")
