# Coffee Machine Project

This project simulates a simple coffee machine system that allows users to order different types of coffee, check the machine's inventory, restock ingredients, and track total earnings. It is implemented using Python.

## Features

- Choose between Espresso, Latte, Cappuccino, and Americano
- Option to add sugar according to user's preference
- Inventory management for ingredients (water, milk, coffee beans, sugar)
- Track total earnings from coffee sales
- Option to restock ingredients
- Menu interface for easy user interaction
- Option to exit program

## Setup and Usage

### Requirements
- Pyhton 3.x

### Run Locally

1. Clone the project:

```bash
  git clone https://github.com/Shreya-Mishra-0613/CoffeeMachineCLI.git
```

2. Go to the project directory:

```bash
  cd CoffeeMachineCLI
```

3. Run the Python script:

```bash
  python src\CoffeeMachine.py
```

### Sample Usage

```bash
   --- Coffee Machine Menu ---
1. Order Coffee
2. Check Inventory
3. Restock Ingredients
4. Check Earnings
5. Exit

Choose an option: 1
Enter coffee type (espresso/latte/cappuccino/americano): espresso
Add sugar(Y for Yes/N for No): Y
Enter amount of sugar you want to add(in grams): 4
Confirm your order:
espresso with 4g of sugar
Price: Rs 10
 Enter 'Y' to confirm: y
Espresso is ready!

--- Coffee Machine Menu ---
1. Order Coffee
2. Check Inventory
3. Restock Ingredients
4. Check Earnings
5. Exit

Choose an option: 2
Water: 1940ml
Milk: 1500ml
Coffee Beans: 382g
Sugar: 196g

--- Coffee Machine Menu ---
1. Order Coffee
2. Check Inventory
3. Restock Ingredients
4. Check Earnings
5. Exit

Choose an option: 3
Enter water to add (ml): 20
Enter milk to add (ml): 30
Enter coffee beans to add (g): 30
Enter sugar to add (g): 5
Inventory restocked!

--- Coffee Machine Menu ---
1. Order Coffee
2. Check Inventory
3. Restock Ingredients
4. Check Earnings
5. Exit

Choose an option: 2
Water: 1960ml
Milk: 1530ml
Coffee Beans: 412g
Sugar: 201g

--- Coffee Machine Menu ---
1. Order Coffee
2. Check Inventory
3. Restock Ingredients
4. Check Earnings
5. Exit

Choose an option: 4
Total earnings: Rs 10

--- Coffee Machine Menu ---
1. Order Coffee
2. Check Inventory
3. Restock Ingredients
4. Check Earnings
5. Exit

Choose an option: 5
Exiting...
```

## Design Choices

- Class-Based Design: A class-based design allows for better organization of functionality, especially as the coffee machine's behavior is modeled using attributes (inventory, earnings) and methods (brew coffee, check inventory, restock). This approach makes the code scalable and easier to maintain.

## Future Enhancements

- Add more coffee varieties and customizations.
- Implement error handling for invalid inputs.
- Add a user-friendly graphical interface.
- Payment verification.
  
## Acknowledgements

- Special thanks to all the seniors of mlcoe who provided guidance during the development of this project.
- The project was inspired by the need to understand how Object-Oriented Programming (OOP) principles can be applied to real-world scenarios, such as designing a coffee machine.
- Thanks to Python's simplicity and versatility, the implementation was a smooth learning experience.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Shreya-Mishra-0613/CoffeeMachineCLI/blob/master/LICENSE) file for details.
