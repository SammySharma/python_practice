class Bookstore:
    def __init__(self) -> None:
        self.inventory = {}
        self.salesData = []

    def addBook(self, isbn: int, name: str, author: str, price: float, quantity: int):
        if isbn in self.inventory:
            print("Book is already there!")
            return
        self.inventory[isbn] = {
            "name": name,
            "author": author,
            "price": float(price),  # Ensure price is float
            "quantity": int(quantity)  # Ensure quantity is int
        }
        print("Book added successfully!")

    def searchBook(self, query: str):
        foundBook_ids = []
        for isbn, details in self.inventory.items():
            if query.lower() in [
                str(isbn),  # ISBN as string for searching
                details["name"].lower(),
                details["author"].lower()
            ]:
                foundBook_ids.append(isbn)
        if len(foundBook_ids) == 0:
            print("No Book Found")
            return

        for ids in foundBook_ids:
            print(f"ISBN: {ids}\n"
                  f"Book Name: {self.inventory[ids]['name'].title()}\n"
                  f"Author: {self.inventory[ids]['author'].title()}\n"
                  f"Price: {self.inventory[ids]['price']}\n"
                  f"Quantity: {self.inventory[ids]['quantity']}")

    def displayInventory(self):
        if len(self.inventory) == 0:
            print("No books in inventory.")
            return
        for isbn, book in self.inventory.items():
            print("\n--------------------------------------")
            print(f"ISBN: {isbn}\n"
                  f"Book Name: {book['name'].title()}\n"
                  f"Author: {book['author'].title()}\n"
                  f"Price: {book['price']}\n"
                  f"Quantity: {book['quantity']}\n")
            print("\n--------------------------------------")

    def UpdateQuantity(self):
        quantity: int = int(input("Enter the quantity to update: "))
        isbn: int = int(input("Enter the ISBN of the book: "))
        if quantity <= 0:
            print("Quantity should be positive.")
            return
        if isbn not in self.inventory:
            print("Invalid ISBN, book not found.")
            return
        
        self.inventory[isbn]["quantity"] += quantity
        print("Quantity updated successfully!")

    def processOrder(self,isbn:int,customer_name:str,qty:int):
        if isbn not in self.inventory:
            print("Invalid ISBN, book not found.")
            return
        if qty>self.inventory[isbn]["quantity"]:
            print("Insufficient Quantity!")
            return
        
        if qty<=0:
            print("Invalid Quantity!")
            return
        total_price = self.inventory[isbn]['price']*qty
        self.inventory[isbn]["quantity"] -= qty

        data = {"isbn":isbn,"customer_name":customer_name,"quantity":qty,"total_price":total_price}
        self.salesData.append(data)

    def displaySalesReport(self):
        total_revenue = sum([txn['total_price'] for txn in self.salesData])
        total_book_sold =sum( [txn['quantity'] for txn in self.salesData])
        print("\n---------REVENUE DATA------------------")
        print(f"Total Revenue: {total_revenue}")
        print(f"Total Book Sold: {total_book_sold}")



# Instantiate the bookstore object
obj = Bookstore()

# Main loop
while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Update Quantity")
    print("4. Process Order")
    print("5. Sales Report")
    print("6. Display Inventory")
    print("8. Exit")

    choice: int = int(input("Please Enter a Choice: "))

    match choice:
        case 1:
            isbn = int(input("Enter ISBN (as a number): "))  # Ensure ISBN is int
            name = input("Enter Book Name: ")
            author = input("Enter Author Name: ")
            price = float(input("Enter Price: "))  # Convert to float
            qty = int(input("Enter Quantity: "))  # Convert to int
            obj.addBook(isbn, name, author, price, qty)
        
        case 2:
            q = input("Search by ISBN, Author, or Book Name: ")
            obj.searchBook(q)

        case 3:
            obj.UpdateQuantity()
        
        case 4:
            isbn:int = int(input("Please Enter the ISBN of the Book: "))
            customer_name:str = str(input("Please Enter Customer's Name: " ).title())
            quantity:int = int(input("Please Enter total Qty you need: "))
            obj.processOrder(isbn,customer_name,quantity)
        
        case 5:
            obj.displaySalesReport()

        case 6:
            obj.displayInventory()
        
        case 8:
            print("Exiting program...")
            break

        case _:
            print("Invalid Choice!")
1