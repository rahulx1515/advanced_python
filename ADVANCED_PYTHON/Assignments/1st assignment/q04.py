class Car:
    def _init_(self, model, brand, price):
        self.model = model
        self.brand = brand
        self.price = price

    def display_info(self):
        return f"Model: {self.model}, Brand: {self.brand}, Price: ${self.price}"

cars = []
while True:
    print("\n1. Add Car\n2. View All Cars\n3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        model = input("Enter car model: ")
        brand = input("Enter car brand: ")
        price = float(input("Enter car price: "))
        cars.append(Car(model, brand, price))
    elif choice == 2:
        if not cars:
            print("No cars in the showroom.")
        else:
            for car in cars:
                print(car.display_info())
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")