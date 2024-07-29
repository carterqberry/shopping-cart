# carter quesenberry lab 6 shopping cart program

# requirement 1:
class Product:
    def __init__(self, name, price, quantity):
        # create product attributes:
        self.name = name
        self.price = price
        self.quantity = quantity

# requirement 2:
class ShoppingCart:
    def __init__(self):
        # create shopping cart list:
        self.products = []
        self.tax_rate = 0.0

    def add_product(self, product):
        # add a product to the cart:
        self.products.append(product)

    def remove_product(self, product_name):
        # remove a product from the cart by name:
        self.products = [p for p in self.products if p.name != product_name]

    def update_quantity(self, product_name, new_quantity):
        # update the quantity of a product in the cart:
        for product in self.products:
            if product.name == product_name:
                product.quantity = new_quantity

    def calculate_subtotal(self):
        # calculate the subtotal of items in the cart:
        return sum(product.price * product.quantity for product in self.products)

    def set_tax_rate(self, tax_rate):
        # set the tax rate for the cart:
        if tax_rate < 0:
            raise ValueError("Tax rate cannot be negative")
        self.tax_rate = tax_rate

    def calculate_tax(self):
        # calculate the total tax amount:
        return self.calculate_subtotal() * self.tax_rate

    def calculate_total(self):
        # calculate the total cost:
        return self.calculate_subtotal() + self.calculate_tax()

    def display_cart(self):
        # display all items in the cart:
        for product in self.products:
            print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

def main():
    shopping_cart = ShoppingCart()
    while True:
        # requiement 3:
        # print menu:
        print("\nShopping Cart Menu")
        print("1. Add product to cart")
        print("2. Remove product from cart")
        print("3. Update product quantity")
        print("4. Show all items in cart")
        print("5. Calculate total cost")
        print("6. Set tax rate")
        print("7. Calculate total tax")
        print("8. Quit")

        # get user choice:
        choice = input("\nEnter your choice: ")

        if choice == '1' or choice == 'add':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Product(name, price, quantity)
            shopping_cart.add_product(product)
            print("\nProduct added.")
        elif choice == '2' or choice == 'remove':
            name = input("Enter product name to remove: ")
            shopping_cart.remove_product(name)
            print("\nProduct removed.")
        elif choice == '3' or choice == 'update':
            name = input("Enter product name to update quantity: ")
            new_quantity = int(input("Enter new quantity: "))
            shopping_cart.update_quantity(name, new_quantity)
            print("\nProduct quantity updated.")
        elif choice == '4' or choice == 'show':
            shopping_cart.display_cart()
        elif choice == '5' or choice == 'total cost':
            print("Total cost:", shopping_cart.calculate_total())
        elif choice == '6' or choice == 'set tax':
            tax_rate = float(input("Enter tax rate (as decimal): "))
            shopping_cart.set_tax_rate(tax_rate)
            print("\nTax rate set.")
        elif choice == '7' or choice == 'total tax':
            print("Total tax:", shopping_cart.calculate_tax())
        elif choice == '8' or choice == 'quit' or choice == 'q':
            print("Exiting the Shopping Cart.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
