from typing import List
class Book:
    def __init__(self,isbn,name,price,qty) -> None:
        self.isbn:int = isbn
        self.name:str =name
        self.price:float =price
        self.qty:int =qty
        self.is_rented = False

library:List[Book] = []

def addBook(isbn,name,price,qty):
    for book in library:
        if book.isbn == isbn:
            print("Book is already there!")
            return
    new_book = Book(isbn,name,price,qty)
    library.append(new_book)
    print("Book added successfully.")


def searchBook(isbn):
    for book in library:
        if isbn == book.isbn:
            print(f"Book found:\nISBN: {book.isbn}\nName: {book.name}\nPrice: {book.price}\nQuantity: {book.qty}"
            )
            return
    print("Book with this ISBN not found in the library.")


def checkQty(isbn):
    for book in library:
        if isbn == book.isbn:
            print(f"\n Book name {book.name} , {book.isbn} is available with {book.qty}")
            return
    print("Book with this ISBN not found in the library.")

def rentBook(isbn,rent_qty):
    for book in library:
        if isbn == book.isbn:
            if book.qty<rent_qty:
                print("Not Enough Books Available ")
                return
        book.is_rented = True
        book.qty -= rent_qty
        print(f"Rented {rent_qty} copy(ies) of {book.name}. Remaining quantity: {book.qty}")
        return
    print("Book with this ISBN not found in the library.")

def displayBooks():
    if len(library)==0:
        print("Library is Empty!")
        return
    
    for book in library:
                print(
            f"ISBN: {book.isbn}\nName: {book.name}\nPrice: {book.price}\nQuantity: {book.qty}\nIs Rented: {'Yes' if book.is_rented else 'No'}\n"
        )

    
def exitProgram():
    print("Thank you. You can Disconnect it now !")
    exit()


while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Check Quantity")
    print("4. Rent Book")
    print("5. Display Books")
    print("6. Exit Program")

    choice:int = int(input("\n Enter your choice: \n"))

    match choice:
        case 1:
            isbn:int = int(input("Enter the ISBN of Book : "))
            name:str = str(input("Enter the name of the Book: "))
            price:float = float(input("Enter the price of the Book"))
            Quantity:int = int(input("Enter the Quantity of the Book: "))
            addBook(isbn,name,price,Quantity)


        case 2:
            isbn:int = int(input("Enter the ISBN of Book : "))
            searchBook(isbn)
        
        case 3:
            isbn:int = int(input("Enter the ISBN of Book : "))
            checkQty(isbn)
        
        case 4:
            isbn:int = int(input("Enter the ISBN of Book : "))
            rent_qty:int = int(input("How many books you need"))
            rentBook(isbn,rent_qty)
        
        case 5:
            displayBooks()
        
        case 6:
            exitProgram()
        
        case _:
            print("Invalid Choice !")
