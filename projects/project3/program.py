import json

class Drink:
    def __init__(self, name, price):
        self.name = name
        self.size = "Medium"  # Fixed size
        self.price = price

class OrderItem:
    def __init__(self, drink, customization="None"):
        self.drink = drink
        self.customization = customization

class CustomerOrder:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, order_item):
        self.items.append(order_item)

class BistroSystem:
    def __init__(self):
        self.menu = [
            Drink("Bearcat Mocha", 4.50),
            Drink("Caramel Catpuccino", 4.25),
            Drink("Meowcha Latte", 4.75),
            Drink("Hazelnut Cappuccino", 4.00),
            Drink("Matcha Green Tea", 4.50)
        ]
        self.open_orders = []
        self.completed_orders = []
        self.load_orders()  # Load saved data

    def display_menu(self):
        print("\n📋 Menu:")
        for drink in self.menu:
            print(f"{drink.name} - ${drink.price:.2f}")

    def take_new_order(self):
        customer_name = input("\nEnter customer name: ")
        order = CustomerOrder(customer_name)
        while True:
            self.display_menu()
            drink_choice = input("Select a drink by name (or type 'done' to finish): ")
            if drink_choice.lower() == 'done':
                break
            selected_drink = next((drink for drink in self.menu if drink.name.lower() == drink_choice.lower()), None)
            if not selected_drink:
                print("Invalid selection. Try again.")
                continue
            customization = input("Enter customization (or press enter for none): ")
            order.add_item(OrderItem(selected_drink, customization))
        self.open_orders.append(order)
        self.save_orders()
        print("\nOrder confirmed!")

    def view_open_orders(self):
        if not self.open_orders:
            print("\nNo open orders.")
        else:
            print("\n📋 Open Orders:")
            for idx, order in enumerate(self.open_orders, start=1):
                print(f"{idx}. {order.customer_name}:")
                for item in order.items:
                    print(f"  - {item.drink.name} (Customization: {item.customization})")

    def mark_next_order_complete(self):
        if not self.open_orders:
            print("\nNo orders to complete.")
        else:
            completed_order = self.open_orders.pop(0)
            self.completed_orders.append(completed_order)
            self.save_orders()
            print(f"\n✅ Completed Order for {completed_order.customer_name}!")

    def generate_end_of_day_report(self):
        sales_summary = {}
        total_revenue = 0
        for order in self.completed_orders:
            for item in order.items:
                sales_summary[item.drink.name] = sales_summary.get(item.drink.name, 0) + 1
                total_revenue += item.drink.price

        print("\n📋 End-of-Day Report")
        print("----------------------------")
        print(f"{'Drink Name':<20}{'Qty Sold':<10}{'Total Sales':<10}")
        for drink, quantity in sales_summary.items():
            total_sales = quantity * next(d.price for d in self.menu if d.name == drink)
            print(f"{drink:<20}{quantity:<10}${total_sales:.2f}")
        print(f"Total Revenue: ${total_revenue:.2f}")

    def save_orders(self):
        """Save open & completed orders to a file."""
        with open("orders.json", "w") as f:
            json.dump({
                "open_orders": [[o.customer_name, [[i.drink.name, i.customization] for i in o.items]] for o in self.open_orders],
                "completed_orders": [[o.customer_name, [[i.drink.name, i.customization] for i in o.items]] for o in self.completed_orders]
            }, f)

    def load_orders(self):
        """Load saved orders."""
        try:
            with open("orders.json", "r") as f:
                data = json.load(f)
                self.open_orders = [CustomerOrder(name) for name, items in data["open_orders"]]
                self.completed_orders = [CustomerOrder(name) for name, items in data["completed_orders"]]
        except FileNotFoundError:
            pass

    def run(self):
        while True:
            print("\nWelcome to the Bearcat Bistro!")
            print("1. Display Menu")
            print("2. Take New Order")
            print("3. View Open Orders")
            print("4. Mark Next Order as Complete")
            print("5. View End-of-Day Report")
            print("6. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.display_menu()
            elif choice == "2":
                self.take_new_order()
            elif choice == "3":
                self.view_open_orders()
            elif choice == "4":
                self.mark_next_order_complete()
            elif choice == "5":
                self.generate_end_of_day_report()
            elif choice == "6":
                print("Exiting Bearcat Bistro. Have a great day!")
                break
            else:
                print("Invalid choice. Try again.")

# Run the Bistro system
bistro = BistroSystem()
bistro.run()