class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = None
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class User:
    def __init__(self, full_name, phone_number, email, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.password = password

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class FoodOrderingApp:
    def __init__(self):
        self.food_items = []
        self.users = []
        self.admin = None
        self.current_user = None

    def admin_login(self, username, password):
        if self.admin and self.admin.username == username and self.admin.password == password:
            self.current_user = self.admin
            return True
        return False

    def user_register(self, full_name, phone_number, email, password):
        user = User(full_name, phone_number, email, password)
        self.users.append(user)

    def user_login(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                self.current_user = user
                return True
        return False

    def add_food_item(self, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        food_item.food_id = len(self.food_items) + 1
        self.food_items.append(food_item)

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                return True
        return False

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                return True
        return False

    def view_food_items(self):
        for food_item in self.food_items:
            print(
                f"FoodID: {food_item.food_id}, Name: {food_item.name}, Quantity: {food_item.quantity}, "
                f"Price: {food_item.price}, Discount: {food_item.discount}, Stock: {food_item.stock}"
            )

    def place_order(self, selected_items):
        order_items = []
        total_price = 0
        for food_id in selected_items:
            for food_item in self.food_items:
                if food_item.food_id == food_id:
                    order_items.append(food_item)
                    total_price += food_item.price
                    break
        if order_items:
            print("Selected Items:")
            for item in order_items:
                print(f"FoodID: {item.food_id}, Name: {item.name}, Price: {item.price}")
            print(f"Total Price: {total_price}")
            # Implement order placement logic here
        else:
            print("No items selected for order.")

    def view_order_history(self):
        # Implement order history retrieval logic here
        pass

    def update_user_profile(self, full_name, phone_number, email, password):
        if self.current_user:
            self.current_user.full_name = full_name
            self.current_user.phone_number = phone_number
            self.current_user.email = email
            self.current_user.password = password


# Usage example
app = FoodOrderingApp()

# Admin functionalities
app.admin = Admin("admin", "admin123")
app.admin_login("admin", "admin123")

app.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 10)
app.add_food_item("Vegan Burger", "1 piece", 320, 0, 5)
app.add_food_item("Truffle Cake", "500gm", 900, 0, 3)

app.view_food_items()

app.edit_food_item(1, "Tandoori Chicken", "6 pieces", 280, 0, 10)
app.remove_food_item(2)

app.view_food_items()

# User functionalities
app.user_register("Krishna", "1234567890", "kris@example.com", "password")
app.user_login("kris@example.com", "password")

app.place_order([2, 3])

app.view_order_history()

app.update_user_profile("Krishna", "1234567890", "kris@example.com", "newpassword")
