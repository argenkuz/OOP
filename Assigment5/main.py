from smartphone import Smartphone
from laptop import Laptop
from tablet import Tablet
from cart import Cart

def main():
    devices = [
        # 10 Smartphones
        Smartphone("iPhone 15", 999, 10, 24, "6.1 inch", "20 hours"),
        Smartphone("Samsung Galaxy S23", 899, 15, 24, "6.4 inch", "22 hours"),
        Smartphone("Google Pixel 7", 799, 8, 24, "6.3 inch", "19 hours"),
        Smartphone("OnePlus 11", 749, 12, 24, "6.7 inch", "24 hours"),
        Smartphone("Xiaomi Mi 13", 699, 20, 24, "6.6 inch", "21 hours"),
        Smartphone("Sony Xperia 1 V", 1199, 6, 24, "6.5 inch", "25 hours"),
        Smartphone("Realme GT 3", 599, 15, 24, "6.7 inch", "18 hours"),
        Smartphone("Oppo Reno 8", 549, 14, 24, "6.4 inch", "19 hours"),
        Smartphone("Vivo X90 Pro", 1099, 9, 24, "6.78 inch", "22 hours"),
        Smartphone("Motorola Edge 40", 699, 10, 24, "6.55 inch", "20 hours"),

        # 10 Laptops
        Laptop("MacBook Pro M2", 1999, 5, 36, "16GB", "3.2 GHz"),
        Laptop("Dell XPS 15", 1799, 7, 24, "32GB", "2.8 GHz"),
        Laptop("HP Spectre x360", 1499, 6, 24, "16GB", "2.5 GHz"),
        Laptop("Lenovo ThinkPad X1", 1699, 4, 36, "32GB", "2.9 GHz"),
        Laptop("Asus ROG Zephyrus", 1899, 9, 24, "16GB", "3.5 GHz"),
        Laptop("Acer Predator Helios 300", 1399, 8, 24, "16GB", "3.1 GHz"),
        Laptop("MSI Stealth 16", 2099, 5, 24, "32GB", "3.8 GHz"),
        Laptop("Razer Blade 15", 2499, 3, 24, "32GB", "4.0 GHz"),
        Laptop("LG Gram 17", 1499, 6, 24, "16GB", "2.7 GHz"),
        Laptop("Asus ZenBook 14", 999, 9, 24, "16GB", "3.0 GHz"),

        # 10 Tablets
        Tablet("iPad Pro", 1299, 10, 24, "2732x2048", "600g"),
        Tablet("Samsung Galaxy Tab S8", 1099, 12, 24, "2560x1600", "567g"),
        Tablet("Microsoft Surface Pro 9", 1399, 8, 24, "2880x1920", "879g"),
        Tablet("Lenovo Tab P12", 799, 15, 24, "2000x1200", "450g"),
        Tablet("Huawei MatePad Pro", 999, 10, 24, "2560x1600", "500g"),
        Tablet("Amazon Fire HD 10", 149, 20, 12, "1920x1200", "465g"),
        Tablet("Google Pixel Tablet", 699, 11, 24, "2560x1600", "450g"),
        Tablet("Xiaomi Pad 6", 499, 18, 24, "2880x1800", "480g"),
        Tablet("Samsung Galaxy Tab A8", 349, 22, 24, "1920x1200", "508g"),
        Tablet("Asus ROG Flow Z13", 1699, 7, 24, "3840x2400", "1180g")
    ]

    cart = Cart()

    while True:
        print("\nMenu:")
        print("1. Show Devices")
        print("2. Show Cart")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nWhich device you want to buy Smartphone, Laptop, Tablet? (s/l/t):")
            device_type = input().lower()
            if device_type == "s":
                for i, device in enumerate(devices[:10], 1):
                    print(f"{i}. {device.display_info()}\n")
                device_choice = int(input("Enter device number: "))
                amount = int(input("Enter amount: "))
                cart.add_device(devices[device_choice - 1], amount)

            elif device_type == "l":
                for i, device in enumerate(devices[10:20], 1):
                    print(f"{i}. {device.display_info()}\n")
                device_choice = int(input("Enter device number: "))
                amount = int(input("Enter amount: "))
                cart.add_device(devices[device_choice + 9], amount)

            elif device_type == "t":
                for i, device in enumerate(devices[20:], 1):
                    print(f"{i}. {device.display_info()}\n")
                device_choice = int(input("Enter device number: "))
                amount = int(input("Enter amount: "))
                cart.add_device(devices[device_choice + 19], amount)

            else:
                print("Invalid choice. Please try again.")

        elif choice == "2":
            cart.print_items()
            checkout_choice = input("Do you want to checkout? (yes/no): ").lower()
            if checkout_choice == "yes":
                cart.checkout()
                remove = input("Do you want to remove items from cart? (yes/no): ").lower()
                if remove == "yes":
                    for i, (device, amount) in enumerate(cart.items, 1):
                        print(f"{i}. {device.name} - {amount} units")
                    remove_choice = int(input("Enter device number to remove: "))
                    if 1 <= remove_choice <= len(cart.items):
                        remove_amount = int(input("Enter amount to remove: "))
                        cart.remove_device(cart.items[remove_choice - 1][0], remove_amount)
                    else:
                        print("Invalid device number. Please try again.")


        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()