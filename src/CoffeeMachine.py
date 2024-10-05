class CoffeeMachine:
    def __init__(self):
        # Initial inventory for the coffee machine
        self.water_level = 2000  # in ml
        self.milk_level = 1500    # in ml
        self.coffee_beans = 400  # in grams
        self.sugar_cube = 200          #in grams
        self.money_earned = 0    # total money earned

    def check_inventory(self):
        print(f"Water: {self.water_level}ml")
        print(f"Milk: {self.milk_level}ml")
        print(f"Coffee Beans: {self.coffee_beans}g")
        print(f"Sugar: {self.sugar_cube}g")

    def brew_coffee(self, coffee_type):
        if coffee_type == "espresso":
            self.make_espresso()
        elif coffee_type == "latte":
            self.make_latte()
        elif coffee_type == "americano":
            self.make_americano()
        elif coffee_type == "cappuccino":
            self.make_cappuccino()
        else:
            print("Invalid selection")

    def make_espresso(self):
        if self.water_level >= 60 and self.coffee_beans >= 18:
            self.water_level -= 60
            self.coffee_beans -= 18
            self.money_earned += 10  # price of espresso
            print("Espresso is ready!")
        else:
            print("Not enough ingredients")

    def make_latte(self):
        if self.water_level >= 40 and self.milk_level >= 150 and self.coffee_beans >= 18:
            self.water_level -= 40
            self.milk_level -= 150
            self.coffee_beans -= 18
            self.money_earned += 20  # price of latte
            print("Latte is ready!")
        else:
            print("Not enough ingredients")

    def make_cappuccino(self):
        if self.water_level >= 50 and self.milk_level >= 100 and self.coffee_beans >= 18:
            self.water_level -= 50
            self.milk_level -= 100
            self.coffee_beans -= 18
            self.money_earned += 20  # price of cappuccino
            print("Cappuccino is ready!")
        else:
            print("Not enough ingredients")
            
    def make_americano(self):
        if self.water_level >= 100 and self.coffee_beans >= 18:
            self.water_level -= 100
            self.coffee_beans -= 18
            self.money_earned += 10  # price of cappuccino
            print("Americano is ready!")
        else:
            print("Not enough ingredients")
            
    def addSugar(self, add_sugar):
        if add_sugar == "Y":
            sugar_amount = int(input("Enter amount of sugar you want to add(in grams): "))
            if sugar_amount <= self.sugar_cube:
                self.sugar_cube -= sugar_amount
            else:
                print("Not enough ingredients")
            
    def restock(self, water, milk, coffee, sugar):
        try:
            self.water_level += int(water)  
            self.milk_level += int(milk)
            self.coffee_beans += int(coffee)
            self.sugar_cube += int(sugar)
            print("Inventory restocked!")
        except ValueError:
            print("Please enter valid numbers for restocking ingredients.")

def display_menu():
    print("\n--- Coffee Machine Menu ---")
    print("1. Order Coffee")
    print("2. Check Inventory")
    print("3. Restock Ingredients")
    print("4. Check Earnings")
    print("5. Exit\n")
def main():
    machine = CoffeeMachine()
    
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            coffee_type = input("Enter coffee type (espresso/latte/cappuccino/americano): ").lower()
            add_sugar = input("Add sugar(Y for Yes/N for No): ").upper()
            machine.addSugar(add_sugar)
            machine.brew_coffee(coffee_type)
        elif choice == "2":
            machine.check_inventory()
        elif choice == "3":
            water = int(input("Enter water to add (ml): "))
            milk = int(input("Enter milk to add (ml): "))
            coffee = int(input("Enter coffee beans to add (g): "))
            sugar = int(input("Enter sugar to add (g): "))
            machine.restock(water, milk, coffee, sugar)
        elif choice == "4":
            print(f"Total earnings: Rs {machine.money_earned}")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")


