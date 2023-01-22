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