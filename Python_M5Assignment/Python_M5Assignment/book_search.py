import sqlite3
book1=sqlite3.connect('books.db')
curbook=book1.cursor()
total=0.0
ch='Y'
while ch.upper()=='Y':
    t=input("Enter book title")
    curbook.execute("SELECT * from booklist WHERE UPPER(Title)=?;",(t.upper(),))
    result=curbook.fetchall()
    if len(result)>0:
        p=0.0
        for i in result:
            print(i)
            p=float(i[-1])
        else:
            c=int(input("No of copies:"))
        total=total+p*c
    else:
        print("Not available")
    ch=input("Add more books\? Y/N")
    while ch.upper()!='Y':
        if ch.upper()=='N':
            print("Total cost:{}".format(total))
            book1.close()
            break
        else:
            print("Wrong choice,enter again")
            ch=input("Add more books\? Y/N")
