
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