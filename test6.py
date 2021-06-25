import sqlite3
conn = sqlite3.connect(r"C:\Phiraya_python\week6\test6.db")
c = conn.cursor()
"""c.execute('''CREATE TABLE users(id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(30) NOT NULL,
    IName varchar(30) NOT NULL,
    email varchar(100) NOT NULL)''')"""

c.execute('''INSERT INTO users (id,fname,IName,email) VALUES (NULL,"Phiraya","Sripim","Phiraya.sr@kkumail.com")''')
c.execute('''INSERT INTO users VALUES (NULL,"Taksayapa" ,"Tangwong", "tuksayapa.t@kkumail.com")''')
c.execute('''INSERT INTO users VALUES (NULL,"Piamsuk" ,"Wathiroiram", "Piamsuk.Wathiroiram@kkumail.com")''')
c.execute('''INSERT INTO users VALUES (NULL,"Phattarapan" ,"Yoykartok", "Phattarapan.y@kkumail.com")''')
conn.commit() 
conn.close()