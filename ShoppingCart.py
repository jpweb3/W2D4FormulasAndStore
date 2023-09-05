def storeinfo():
    cart = {}

    def add():
        item = input("What would you like to add to your cart? ")
        quan = input("How many? ")
        cart[item] = quan
        print(f"{item} has been added  to your cart.")

    def show():
        print(cart)

    while True:
        menu = input("Welcome to my  shop!  Show/Add/Delete or Quit?  ")
        
        if menu.lower() == "quit":
            show()
            break

        elif menu.lower()  ==  "add":
            add()

storeinfo()
