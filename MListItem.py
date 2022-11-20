#!C:\Users\julia\AppData\Local\Programs\Python\Python310\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import mitemlist as ml
#連線DB

#from dbConfig import conn, cur

#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>商品列表</title>
<style>
    body{background-color: #e0dcd9;}
    h1{text-align:center;}
    h2{text-align:center;}
    #add{
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
        left: 20px;
        top: 230px;
        width:300px;
        background-color: white;
        padding: 10px;
        border: solid #8f8681 5px;
    }
    #update{
        position: absolute;
        right: 20px;
        top: 10px;
        width:300px;
        background-color: white;
        padding: 10px;
        border: solid #8f8681 5px;
    }
    #out{
        position: absolute;
        right: 20px;
        top: 200px;
        width:300px;
        background-color: white;
        padding: 10px;
        border: solid #8f8681 5px;
    }
    #main{
        margin: 40px auto;
        background-color: white;
        width: 700px;
        border: solid #8f8681 5px;
    }
    #back{
        margin: 40px auto;
        background-color: white;
        width: 700px;
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


<fieldset id="add">
<legend>請輸入新商品</legend>
<form method="post" action="MaddItem.py">
輸入商品名稱<input type="text" name='name'><br>
輸入商品定價<input type="text" name='price'><br>
輸入商品庫存<input type="text" name='inventory'><br>
<input class="button" type="submit" value="提交">
</form>
</fieldset>


<fieldset id="del">
<legend>刪除商品</legend>
<form method="post" action="MdelItem.py">
輸入商品編號<input type='text' name='i'>
<input class="button" type="submit" value="提交">
</form>
</fieldset>
</div>

<fieldset id="update">
<legend>更新商品</legend>
<form method="post" action="Maddinventory.py">
輸入商品編號<input type="text" name='id'><br>
輸入進貨數<input type="text" name='num'><br>
<input class="button" type="submit" value="提交">
</form>
</fieldset>
</div>


<fieldset id="out">
<legend>出貨</legend>
<form method="post" action="Mout.py">
<input class="button" type="submit" value="查看出貨列表">
</form>
</fieldset>
</div>

<div id="main">
<h1>商品管理清單</h1><hr/>
""")

mlList=ml.getList()

for (id,name,price,inventory) in mlList:
	print(f"<p>商品編號{id}: 商品名稱:{name} 單價:{price} 庫存量:{inventory}</p>")

print("""
<input class="button" type="button" value="點我回首頁" onclick="location.href='home.html'">
</div>
</body></html>
""")

outList=ml.getPayList()
for (id,name,pay) in outlList:
	print(f"<p>商品編號{id}: 商品名稱:{name} 待出貨量:{pay}</p>")


