# Library Management System using python
class Library:
    """
    This Class is use for Library Management.
    It has total 5 methods:
    addBook(book_name), removeBook(book_name), lendBook(book_name,person_name), returnBook(book_name), displayBooks(), displayLendRecords()
    """
    def __init__(self,lib_name,bk_list=[]):
        self.lib_name = lib_name.capitalize()  # contains library name
        self.bk_list = bk_list  # contains list of available books
        self.no_of_books = len(bk_list)  # contains no of books available
        self.lend_record = {}  # contains lend records

    def addBook(self,bk_name):  # method for adding book
        if bk_name == "":
            print("--- Name cant be Empty ---")
            return self.addBook(input("Book Name: "))
        elif len(bk_name) > 20:
            print("--- Name is too long.  limit: 20char ---")
            return self.addBook(input("Book Name: "))
        else:
            self.bk_list.append(bk_name)
            self.no_of_books+=1
            print(f"--- \"{bk_name}\" is added to the Library ---")

    def removeBook(self,bk_name):  # method for removing book
        if bk_name == "":
            print("--- Name cant be Empty ---")
            return self.removeBook(input("Book Name: "))
        elif bk_name in self.bk_list:
            self.bk_list.remove(bk_name)
            self.no_of_books -= 1
            print(f"--- \"{bk_name}\" is removed from the library ---")
        else:
            print("--- Book Not Exist ---")

    def lendBook(self,bk_name,person_name):  # method for lending book
        if bk_name == "" or person_name == "":
            print("--- Fields cannot be Empty ---")
            return self.lendBook(input("Book Name: "),input("Lender's Name: "))
        elif bk_name in self.bk_list:
            self.bk_list.remove(bk_name)
            self.no_of_books -= 1
            self.lend_record[bk_name] = person_name
            print(f"--- Congrats! \"{bk_name}\" has been lent to you ---")
        elif bk_name in self.lend_record:
            print(f"--- Sorry, \"{bk_name}\" has been lent to \"{self.lend_record[bk_name]}\" ---")
        else:
            print(f"--- Sorry, We dont have \"{bk_name}\" ---")

    def returnBook(self,bk_name):  # method for returning lent book
        if bk_name == "":
            print("--- Name cant be Empty ---")
            return self.returnBook(input("Book Name: "))
        elif bk_name in self.lend_record:
            self.bk_list.append(bk_name)
            self.no_of_books += 1
            del self.lend_record[bk_name]
            print(f"--- Thank you for returning \"{bk_name}\" ---")
        else:
            print("--- This Book has never been lent to anyone ---")

    def displayBooks(self):  # method for displaying available books
        if len(self.bk_list) != 0:
            print("--- List of Books ---")
            for i,book in enumerate(self.bk_list):
                print(f"{i}. {book}")
            print("---------------------")
        else:
            print("--- No Books are Available ---")

    def __str__(self):
        return f"Library: {self.lib_name}"

    def displayLendRecords(self):  # method for displaying lend records
        if len(self.lend_record) != 0:
            print("--- Lend Records ---")
            for i,x in enumerate(self.lend_record.items()):
                print(f"{i}. {x[0]}: {x[1]}")
            print("--------------------")
        else:
            print("--- No Records found ---")

if __name__ == '__main__':
    galaxy = Library('galaxy')
    key_press_list = {'A':'Add Book','R':'Remove Book','L':'Lend Book','T':'Return Book','D':'Display Books','C': 'Lend Records','Q': 'Quit'}
    key_press = 0
    while key_press != 'q':
        print(f"\n--- Welcome to {galaxy.lib_name}! ---")
        for key,desc in key_press_list.items():
            print(f"{key}: {desc}")
        print("--------------------------")

        key_press = input("Press Key: ").lower()
        if key_press == 'a':
            galaxy.addBook(input('Book Name: '))
        elif key_press == 'r':
            galaxy.removeBook(input('Book Name: '))
        elif key_press == 'l':
            galaxy.lendBook(input('Book Name: '),input("Lender's Name: "))
        elif key_press == 't':
            galaxy.returnBook(input('Book Name: '))
        elif key_press == 'd':
            galaxy.displayBooks()
        elif key_press == 'c':
            galaxy.displayLendRecords()
        elif key_press == 'q':
            pass
        else:
            print("--- Invalid Input ---")