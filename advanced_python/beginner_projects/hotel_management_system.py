class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = True

    def book_room(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def checkout_room(self):
        self.is_available = True

    def __str__(self):
        return f"Room {self.room_number} - Type: {self.room_type}, Price: {self.price}, Available: {'Yes' if self.is_available else 'No'}"

class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.room = None
        self.bill = 0

    def assign_room(self, room):
        if room.book_room():
            self.room = room
            self.bill += room.price
            return True
        return False

    def checkout(self):
        if self.room:
            self.room.checkout_room()
            print(f"\n{self.name} has checked out. Total bill: {self.bill}")
            self.room = None
            self.bill = 0
        else:
            print("\nCustomer has no room assigned!")

class HotelManagement:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.customers = []

    def add_room(self, room):
        self.rooms.append(room)
        print(f"Room {room.room_number} added successfully!")

    def find_available_room(self, room_type):
        for room in self.rooms:
            if room.room_type == room_type and room.is_available:
               return room
        return None

    def book_room(self, customer, room_type):
        room = self.find_available_room(room_type)
        if room:
            if customer.assign_room(room):
                self.customers.append(customer)
                print(f"\nRoom {room.room_number} booked for {customer.name} (Phone: {customer.phone})")
            else:
                print("\nRoom booking failed!")
        else:
            print("\nNo rooms available for the selected type!")

    def checkout_customer(self, phone):
        for customer in self.customers:
            if customer.phone == phone:
                customer.checkout()
                self.customers.remove(customer)
                return
        print("\nCustomer not found!")

    def show_available_rooms(self):
        available_rooms = [str(room) for room in self.rooms if room.is_available]
        if available_rooms:
            print("\n--- Available Rooms ---")
            for room in available_rooms:
                print(room)
        else:
            print("\nNo rooms available!")


my_hotel = HotelManagement("Taj Hotel")

my_hotel.add_room(Room(101, "Single", 1500))
my_hotel.add_room(Room(102, "Double", 2500))
my_hotel.add_room(Room(103, "Single", 5000))

# main logic
while True:
    print("\n--- Hotel Management System ---")
    print("1. Book Room")
    print("2. Checkout Customer")
    print("3. Add New Room")
    print("4. Show Available Rooms")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter customer name: ")
        phone = input("Enter phone number: ")
        print("Room Types: Single, Double")
        room_type = input("Enter room type: ")
        customer = Customer(name, phone)
        my_hotel.book_room(customer, room_type)

    elif choice == "2":
        phone = input("Enter customer's phone number: ")
        my_hotel.checkout_customer(phone)

    elif choice == "3":
        room_number = int(input("Enter new room number: "))
        room_type = input("Enter room type (Single/Double): ")
        price = int(input("Enter room price: Rs"))
        new_room = Room(room_number, room_type, price)
        my_hotel.add_room(new_room)

    elif choice == "4":
        my_hotel.show_available_rooms()

    elif choice == "5":
        print("Exiting...")
        break
    
    else:
        print("Invalid choice! Please try again.")