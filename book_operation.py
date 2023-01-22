from book import book
class shelf:

    booklist=[]

    def addbook(self):
        bookid=int(input('enter book id  : '))
        bookname=input('enter book name : ')
        bedition=input('enter book edition : ')
        bauthor=input('enter book author name : ')
        bpublication=input('enter book publication : ')
        bprice=input('enter book price : ')
        bookobj=book(bookid,bookname,bedition,bauthor,bpublication,bprice)
        self.booklist.append(bookobj)
        print('Book added successfully....')
        print(self.booklist)

    def viewbook(self):
        for i in self.booklist:
            print(i)
        
        
    def search_book(self):
        book_id=int(input('enter book id of book which u want to search'))
        for i in self.booklist:
            if i.get_bookid()==book_id:
                print(i)
                return i
         
        print('pls check your Id and try again')
           
    def DeleteBook(self):
        book_id=int(input('enter book id of book which u want to delete'))
        for i in self.booklist:
            if i.get_bookid()==book_id:
                 self.booklist.remove(i)
                 print('delete successfully')
                 return i
        print('pls check your Id and try again')         

    def updatebook(self):
        book_id=int(input('enter book id of book which u want to update'))
        for i in self.booklist:
            if i.get_bookid()==book_id:
                book_name = input("Enter updated book name : ")
                book_edition = (input("Enter updated book edition : "))
                book_author = input("Enter updated book author : ")
                book_publication = input("Enter updated book publication : ")
                book_price = (input("Enter updated book price : "))
                 
                i.set_bookname(book_name)
                i.set_bookedition(book_edition)
                i.set_bookauthor(book_author)
                i.set_bookpub(book_publication)
                i.set_bookprice(book_price)
                print('updated successfully')
                return i
        print('pls check your Id and try again')

class book:
    def __init__(self,bookid,bookname,bedition,bauthor,bpublication,bprice):
        self.__bookid=bookid
        self.__bookname=bookname
        self.__bedition=bedition
        self.__bauthor=bauthor
        self.__bpublication=bpublication
        self.__bprice=bprice

    def __str__(self):
        return f"book id : {self.__bookid}\nbook name : {self.__bookname}\nbook edition : {self.__bedition}\nbook author : {self.__bauthor}\nbook publication : {self.__bpublication}\nbook price : {self.__bprice}"
     
    def get_bookid(self):
        return self.__bookid
    
    def set_bookname(self,newname):
        self.__bookname = newname
    
    def set_bookedition(self,newedition):
        self.__bedition = newedition

    def set_bookauthor(self,newauthor):
        self.__bauthor=newauthor

    def set_bookpub(self,newpublication):
        self.__bpublication=newpublication

    def set_bookprice(self ,newprice):
        self.__bprice = newprice
from book_operation import shelf
class main:
   def execute(self,choice):
    if choice==1:
        print('________ADD BOOK________')
        library.addbook()
    if choice==2:
        print('________VIEW BOOK________')
        library.viewbook()
    if choice==3:
        print('________SEARCH BOOK________')
        library.search_book()
    if choice==4:
        print('______DELETE BOOK________')
        library.DeleteBook()
    if choice==5:
        print('______UPDATE BOOK________')
        library.updatebook()
       
    


if __name__=='__main__':
    obj=main()
    library=shelf()
    while True:
     ch=int(input("Enter your choice : \n1.Add Book \n2.View Book \n3.Search Book By ID \n4.Delete Book \n5.Update Book : \n  "))
     obj.execute(ch)
