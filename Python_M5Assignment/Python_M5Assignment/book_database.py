import sqlite3
book1=sqlite3.connect('books.db')
curbook=book1.cursor()
while True:
    ch=int(input("Enter 1 to create new booklist,enter 2 to add data to existing booklist or enter 3 to exit"))
    if ch==1:
        curbook.execute('''CREATE TABLE booklist(Book_ID INTEGER PRIMARY KEY,Title VARCHAR NOT NULL,Author VARCHAR,Price REAL NOT NULL);''')
        print("Table successfully created")
    elif ch==2:
        try:
            book_id=int(input("Enter book id"))
            title=input("Enter book title")
            author=input("Enter author")
            price=float(input("Enter price"))
            curbook.execute("INSERT INTO booklist (Book_ID,TITLE,AUTHOR,PRICE) VALUES (?,?,?,?);",(book_id,title,author,price))
            print("Successfully added")
            book1.commit()
        except:
            print("book_id should be integer and price should be real no")
            book1.rollback()
    elif ch==3:
        book1.close()
        break
    else:
        print("Wrong choice")
