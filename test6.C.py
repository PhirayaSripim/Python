import sqlite3
conn = sqlite3.connect (r"C:\Phiraya_python\week6\test6.db")
c = conn.cursor()

try:
    c.execute ("SELECT * FROM users ORDER BY id DESC")
    conn.commit ()
    result = c. fetchall()
    for x in result :
        print (x)
    c.close()

except sqlite3.Error as e :
    print(e)
finally :
    if conn:
        conn.close()    