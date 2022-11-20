#連線DB
from dbConfig import conn, cur


    
    #管理端商品清單
def getList():
    sql="select id, name, price, inventory from mitemlist;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
    
    #出貨列表
def getPayList():
    sql="select id, name, pay from mitemlist where pay>0;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
    
    #管理端顯示的
def ManaList():
    sql="select id, name, price, inventory, pay from mitemlist;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
    
    #新增商品
def MaddItem(name,price,inventory):
    sql="insert into mitemlist (name,price,inventory) values (%s,%s,%s);"
    cur.execute(sql,(name,price,inventory))
    conn.commit()
    return True
    
    #檢查資料有沒有填寫正確
def chkstr(name,price,inventory):
    chknum=0
    if (bool(name)&bool(price)&bool(inventory)):#必填項目都有填
        if(int(price)>0):#價格要大於0
            chknum=chknum+0
        else:
            chknum=chknum+1
        if (int(inventory)>=0):#庫存量不可為負
            chknum=chknum+0
        else:
            chknum=chknum+1
    else:
        chknum=chknum+1
    return chknum
    
    #刪除商品
def MdelItem(id):
    sql="delete from mitemlist where id=%s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True
    
    #檢查有無此商品
def chkItem(id):
    chknum=0
    sql="select id from mitemlist;"
    cur.execute(sql)
    records = cur.fetchall()
#    re = cursor.fetchone()
    for i in records:
        if int(id)!=int(i[0]):#如果陣列中的數字與id不一樣，則chknum不動，表不存在
            chknum=chknum+0
        else: 
            chknum = chknum+1#若相同則加一
    return chknum #存在為1 不存在為0
    
    
    #更新庫存
def MaddInv(id,num):
    sql="update mitemlist set `inventory`=inventory+%s where id=%s;"
    cur.execute(sql,(num,id))
    conn.commit()
    return True
    
    #取出該id的庫存量
def chkinv(id,num):
    chkinv=0
    sql="select inventory from mitemlist where id=%s;"
    cur.execute(sql,(id,))
    records = cur.fetchall()#只有一個數
    for i in records:
        chkinv=int(i[0])
    return chkinv
    
    #取該id當前的pnum
def chkpnum(id,num):
    chkpnum=0
    sql="select pnum from mitemlist where id=%s;"
    cur.execute(sql,(id,))
    records = cur.fetchall()#只有一個數
    for i in records:
        chknum=int(i[0])
    return chknum

    #加入購買數量
def Caddnum(id,num):
    sql="update mitemlist set `pnum`=pnum+%s where id=%s;"
    cur.execute(sql,(num,id))
    conn.commit()
    return True
    
    #購物清單
def getCart():
    #查詢
    sql="select id, name, price, inventory, pnum from mitemlist where pnum>0;"#需大於0 才代表有加入購物車
    cur.execute(sql)
    records = cur.fetchall()
    return records
    
    #變更購買數量購物車
def Cedit(id,num):
    sql="update mitemlist set `pnum`=%s where id=%s;"
    cur.execute(sql,(num,id))
    conn.commit()
    return True
    
    #刪除購物車中商品
def CdelItem(id):
    sql="update mitemlist set `pnum`=0 where id=%s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True

    #檢查購物車有無此商品
def chkCart(id):
    chknum=0
    sql="select id from mitemlist where pnum>0;"
    cur.execute(sql)
    records = cur.fetchall()
    for i in records:
        if int(id)!=int(i[0]):#如果陣列中的數字與id不一樣，則chknum不動，表不存在
            chknum=chknum+0
        else: 
            chknum = chknum+1#若相同則加一
    return chknum #存在為1 不存在為0
    
    #結帳囉
def Cout():
    #結帳前先記在pay裡
    sql="select id, pnum from mitemlist where pnum>0;"#購物車內的id、pnum
    cur.execute(sql)
    records = cur.fetchall()
    for i in records:#每一項商品的id (i[0])、pnum (i[1])
        sql="update mitemlist set `pay`=pay+%s where id=%s;"#在出貨前，pay要增加
        cur.execute(sql,(i[1],i[0]))
        conn.commit()
    #再將消費者端的pnum購物車清空
    sql1="update mitemlist set `pnum`=0;"
    cur.execute(sql1,)
    conn.commit()
    #減庫存量
    sql2="select id, pay from mitemlist where pay>0;"#購物車內的id、pay
    cur.execute(sql2)
    results = cur.fetchall()
    for v in results:#每一項商品的id (v[0])、pay (v[1])
        sql2="update mitemlist set `inventory`=inventory-%s where id=%s;"#在出貨前，pay要增加
        cur.execute(sql2,(v[1],v[0]))
        conn.commit()
    return True

    
    #出貨囉
def Mout():
    #清空pay
    sql1="update mitemlist set `pay`=0;"
    cur.execute(sql1,)
    conn.commit()
    return True
    
    #檢查出貨列表有無此商品
def chkOut(id):
    chknum=0
    sql="select id from mitemlist where pay>0;"
    cur.execute(sql)
    records = cur.fetchall()
    for i in records:
        if int(id)!=int(i[0]):#如果陣列中的數字與id不一樣，則chknum不動，表不存在
            chknum=chknum+0
        else: 
            chknum = chknum+1#若相同則加一
    return chknum #存在為1 不存在為0
    
    #個別出貨
def MeachOut(id):
    sql="update mitemlist set `pay`=0 where id=%s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True