import sqlite3

def getConnection():
    con=sqlite3.connect("bookstore.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Books(id INTEGER PRIMARY KEY,title text,author text,year interger,isbn integer) ")
    con.commit()
    con.close()

getConnection()

def add(title,author,year,isbn):
    con=sqlite3.connect("bookstore.db")
    cur=con.cursor()
    cur.execute("INSERT INTO Books VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    con.commit()
    con.close()

def view():
    con=sqlite3.connect("bookstore.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Books")
    restultset=cur.fetchall()
    con.commit()
    con.close()
    return restultset

def search(title="",author="",year="",isbn=""):
    con=sqlite3.connect("bookstore.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Books where title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    restultset=cur.fetchall()
    con.commit()
    con.close()
    return restultset



def update(id,author="",year="",isbn="",title=""):
    con=sqlite3.connect("bookstore.db")
    cur=con.cursor()
    cur.execute("UPDATE Books SET title=? ,author=?, year=?, isbn=? where id=?",(title,author,year,isbn,str(id)))
    con.commit()
    con.close()

def delete(id):
    con=sqlite3.connect("bookstore.db")
    cur=con.cursor()
    cur.execute("DELETE FROM Books where id=?",(id,))
    con.commit()
    con.close()



#add(author="jhon tablet",year="1982",isbn="123456",title="The See")
#delete(2)
#print(view())

search(author="Binny")
