


class library:
    no_of_book = 0
    book_list = []

    def manage(self):
        a= input("do you want to insert book say 'yes'")
        while(a=='yes'):
            insert=input("which book you want to insert")
            self.book_list.append(insert)
            self.no_of_book=self.no_of_book+1
            a= input("insert again say 'yes' or want to see books say 'see'")
        if a=='see':
            print(f"book wee have{self.no_of_book} or  of book is")
            for i in self.book_list:
                print(i, f"\n")
        else:
            print("invailad syntext")  



obj= library()
obj.manage()
