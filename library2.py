class Bookstore:
    def __init__(self) -> None:
        self.inventory = {}
        self.salesData = []


    def addBook(self,isbn,name,author,price,quantity):
        if isbn in self.inventory:
            print("Book is Already there!")
            return
        self.inventory[isbn] = {
            "name":name,
            "author":author,
            "Price":price,
            "Quantity":quantity
            }
        print("Book Added Successfully!")
    
    def searchBook(self,query):
        foundBook_ids=[]
        for isbn,details in self.inventory.items():
            if query.lower() in [
                str(isbn),
                details["name"].lower(),
                details["author"].lower()
                ]:
                foundBook_ids.append(isbn)
        if len(foundBook_ids)==0:
            # print("No Nook Found")
            return

        for ids in foundBook_ids:
            print(f"{self.inventory[ids]}")

    def displayInventory(self):
          for isbn, book in self.inventory.items():
              print(f"ISBN: {isbn}\n"
              f"Book Name: {book['name'].title()}\n"
              f"Book Author: {book['author'].title()}\n"
              f"Book Price: {book['price']}\n"
              f"Book Quantity: {book['quantity']}\n")


obj = Bookstore()


while True:
    print("\n1. Add Book")
    print("2. Search Book")
    # print("3. Update Quantity")
    # print("4. Process Order")
    # print("5. Generate Sales Report")
    print("6. Display Inventory")
    # print("7. Display Sales Data")
    print("8. Exit")

    choice:int = int(input("Please Enter a Choice: "))

    match choice:
        case 1:
            isbn = (input("Please Enter ISBN: "))
            name = (input("Please Enter Book Name: "))
            author = (input("Please Enter Author Name: "))
            price = (input("Please Enter Price: "))
            qty = (input("Please Enter Quantity: "))
            obj.addBook(isbn,name,author,price,qty)
        
        case 2:
            q = input("Search By ISBN / author / Book Name")
            obj.searchBook(q)

        case 6:
            obj.displayInventory()
        
        case 8:
            break

        case _:
            print("Invalid Choice")

    