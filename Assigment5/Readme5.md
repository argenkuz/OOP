# OOPArgenKulzhanovAssigment5
## Objective

In this assignment, students will create a shopping cart system for electronic devices, implementing the inheritance concept of Object-Oriented Programming (OOP). This system will allow customers to browse and purchase electronic devices such as smartphones, laptops, and tablets, while also managing stock and applying discounts.

## Project Overview

This project is an implementation of an e-commerce system with various device classes (`Device`, `Smartphone`, `Laptop`, `Tablet`) and a `Cart` class to manage the shopping cart. The project includes unit tests to verify the functionality of the classes.

## Classes and Methods

### Device Class

- **`__init__(self, name, price, stock, warranty_period)`**: Initializes a new device with the given attributes.
- **`display_info(self)`**: Returns a string with the device's information.
- **`apply_discount(self, discount_percentage)`**: Applies a discount to the device's price.
- **`is_available(self, amount)`**: Checks if the specified amount of the device is available in stock.
- **`reduce_stock(self, amount)`**: Reduces the stock of the device by the specified amount.

### Device Types:

- **`Smartphone`**: Contains attributes like screen size and battery life.
- **`Laptop`**: Contains attributes like RAM size and processor speed.
- **`Tablet`**: Contains attributes like screen resolution and weight.

### Smartphone Class (inherits from Device)

- **`__init__(self, name, price, stock, warranty_period, screen_size, battery_life)`**: Initializes a new smartphone with the given attributes.
- **`display_info(self)`**: Returns a string with the smartphone's information.
- **`make_call(self, number)`**: Simulates making a call to the given number.
- **`install_app(self, app_name)`**: Simulates installing an app on the smartphone.

### Laptop Class (inherits from Device)

- **`__init__(self, name, price, stock, warranty_period, ram_size, processor_speed)`**: Initializes a new laptop with the given attributes.
- **`display_info(self)`**: Returns a string with the laptop's information.
- **`run_program(self, program)`**: Simulates running a program on the laptop.
- **`use_keyboard()`**: Simulates using the laptop's keyboard.

### Tablet Class (inherits from Device)

- **`__init__(self, name, price, stock, warranty_period, screen_resolution, weight)`**: Initializes a new tablet with the given attributes.
- **`display_info(self)`**: Returns a string with the tablet's information.
- **`browse_internet(self, site)`**: Simulates browsing the internet on the tablet.
- **`use_touchscreen(self, touch)`**: Simulates using the tablet's touchscreen.

### Cart Class

- **`__init__(self)`**: Initializes a new shopping cart.
- **`add_device(self, device, amount)`**: Adds a device to the cart.
- **`remove_device(self, device, amount)`**: Removes a device from the cart.
- **`get_total_price(self)`**: Returns the total price of the items in the cart.
- **`print_items(self)`**: Prints the items in the cart.
- **`checkout(self)`**: Simulates checking out the items in the cart.


## UML Class Diagram

![Снимок экрана 2025-02-23 в 14.28.31.png](../../../%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-02-23%20%D0%B2%2014.28.31.png)

## How to Run the Code
1.Run the main script:
```sh
   python main.py
```

### Sample Run 1

**Input:**
```
1
s
1
2
2
yes
no
3
```

**Output:**
```
Menu:
1. Show Devices
2. Show Cart
3. Exit
Enter your choice: 1

Which device you want to buy Smartphone, Laptop, Tablet? (s/l/t):
1. Name: iPhone 15
   Price: 999
   Stock: 10
   Warranty Period: 24
   Screen size: 6.1 inch
   Battery life: 20 hours

2. Name: Samsung Galaxy S23
   Price: 899
   Stock: 15
   Warranty Period: 24
   Screen size: 6.4 inch
   Battery life: 22 hours

Enter device number: 1
Enter amount: 2

Menu:
1. Show Devices
2. Show Cart
3. Exit
Enter your choice: 2

iPhone 15 - 2 units
Do you want to check out? (yes/no): yes
iPhone 15 - 2 units at $999 each and total $1998
Do you want to remove items from cart? (yes/no): no

Menu:
1. Show Devices
2. Show Cart
3. Exit
Enter your choice: 3
Exiting program.
```


### Test Output
````
test_display_info (__main__.TestDevice) ... ok
test_apply_discount (__main__.TestDevice) ... ok
test_is_available (__main__.TestDevice) ... ok
test_reduce_stock (__main__.TestDevice) ... ok
test_make_call (__main__.TestSmartphone) ... ok
test_instaling_app (__main__.TestSmartphone) ... ok
test_run_program (__main__.TestLaptop) ... ok
test_use_keyboard (__main__.TestLaptop) ... ok
test_browse_internet (__main__.TestTablet) ... ok
test_use_touchscreen (__main__.TestTablet) ... ok
test_add_device (__main__.TestCart) ... ok
test_remove_device (__main__.TestCart) ... ok
test_total_price (__main__.TestCart) ... ok
test_print_items (__main__.TestCart) ... ok
test_checkout (__main__.TestCart) ... ok

----------------------------------------------------------------------
Ran 15 tests in 0.002s

OK

1)Testcase for test display_info
Name: Iphone 13
Price: 999
Stock: 10
Warranty Period: 24

Name: Samsung Galaxy S22
Price: 1099
Stock: 8
Warranty Period: 24


2)Testcase for test apply_discount
With discounted Price: 899


3)Testcase for test is_available
Iphone 13 is available: YES
Samsung Galaxy S22 is available: NO


4)Initial stock for Iphone 13: 10
  Initial stock for Samsung Galaxy S22: 8

Testcase for test reduce_stock
Reduced stock for Iphone 13: 5
Reduced stock for Samsung Galaxy S22: 8


5)Testcase for test make_call
Dialing ... 996709785 Call in progress...


6)Testcase for test instaling app
Instagram successfully installed


7)Testcase for test run_program
VS code is running


8)Testcase for test use_keyboard
Typing...


9)Testcase for test browse_internet
Browsing  www.google.com...


10)Testcase for test use_touch_screen
Touching interface...


11)Testcase for test add_item
Added items: 2


12)Testcase for test remove_device
Remaining items: [('Iphone 13', 2)]
Total price: 1998

All items removed
Remaining items: []
Total price: 0


13)Testcase for test total_price
Total price: 4995


14)Testcase for test print_items
(Вывод списка товаров)


15)Testcase for test checkout
(Вывод информации о покупке)
```