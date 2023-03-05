class Pizza:
    def get_description(self):
        print(
            "Pizza: the crown jewel of culinary creations, loved for its crispy crust, rich tomato sauce, savory cheeses, and endless topping possibilities. Versatile and adaptable, it's a timeless masterpiece that has won the hearts of food lovers worldwide and will continue to do so for generations to come.")

    def get_cost(self):
        print("super")


class Classic(Pizza):
    def get_description(self):
        print(
            "The classic pizza: a perfect blend of crisp crust, tomato sauce, and savory cheeses. Simple yet flavorful, it's a feast for the senses that leaves you craving more.")

    def get_cost(self):
        cost = 12
        return cost

class Margherita(Pizza):
    def get_description(self):
        print(
            "The Margherita pizza: a classic delight where quality ingredients shine through. Fragrant basil, velvety mozzarella, and herb-infused tomato sauce come together on a crispy crust to transport you to the hills of Italy with each flavorful bite.")

    def get_cost(self):
        cost = 15
        return cost

class Turkish(Pizza):
    def get_description(self):
        print(
            "Turkish pizza, also known as ""lahmacun,"" is a flavorful fusion of Middle Eastern spices, savory meats, and fresh veggies on a crispy crust. With a complex blend of earthy cumin, tangy sumac, and fragrant parsley, it's a taste of Istanbul in every bite.")

    def get_cost(self):
        cost = 17
        return cost

class Plain(Pizza):
    def get_description(self):
        print(
            "Plain pizza: a timeless classic that celebrates high-quality ingredients with a crispy crust, luscious tomato sauce, and a perfect blend of mozzarella and Parmesan cheeses. Simple yet delicious, it's a versatile canvas for your favorite toppings.")

    def get_cost(self):
        cost = 16
        return cost




class Decorator:
    def get_cost(self):
        return self.component.get_cost() + \
            Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
            ' ' + Pizza.get_description(self)


class Olives(Decorator):
    def get_description(self):
        print("Olives: small but mighty, prized for their bold flavor and nutritional benefits.")


    def get_cost(self):
     cost = 1
     return cost

class Mushrooms(Decorator):
    def get_description(self):
        print("Mushrooms: earthy delicacies prized for their unique taste and remarkable versatility. ")


    def get_cost(self):
     cost = 1
     return cost

class Goat_cheese(Decorator):
    def get_description(self):
        print("Goat cheese: a creamy and tangy delight cherished for centuries. ")


    def get_cost(self):
     cost = 2
     return cost

class Meat(Decorator):
    def get_description(self):
        print("Meat: a cornerstone of many cuisines, beloved for its rich and complex flavors. ")


    def get_cost(self):
     cost = 2
     return cost

class Onions(Decorator):
    def get_description(self):
        print("Onions: pungent and flavorful, adding depth and complexity to dishes.")


    def get_cost(self):
     cost = 0.5
     return cost

class Corns(Decorator):
    def get_description(self):
        print("Corn: a golden grain beloved for its sweetness and versatility. ")


    def get_cost(self):
      cost = 0.5
      return cost




