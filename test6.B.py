import sqlite3
conn = sqlite3.connect (r"C:\Phiraya_python\week6\test6.db")
c = conn.cursor()
try :
    data = ("Plaii","Fah","Phi"),("TiTy","YoYo","Mimy"),("RiRy","Kiky","FiFy")
    c.executemany("INSERT INTO users (fname,IName,email) VALUES (?,?,?)",data)
    conn.commit ()
    c.close ()
except sqlite3.Error as e:
    print(e)

finally :
    if conn:
        conn.close()  