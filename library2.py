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


# Instantiate the bookstore object
obj = Bookstore()

# Main loop
while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Update Quantity")
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

        case 6:
            obj.displayInventory()
        
        case 8:
            print("Exiting program...")
            break

        case _:
            print("Invalid Choice!")
