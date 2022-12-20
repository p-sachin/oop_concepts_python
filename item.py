import csv
# Constructors are generally used for instantiating an objeect. __init__() method is called the constructor and is always
# called when an object is created.
# Class attributes belong to the class itself which are shared by all the instances. They are defined in the class body parts
# at the top usually.
# Instance attributes belongs to only one object. It is only accessible in the scope of the object and defined inside the constructor function
# of the class.


class Item:
    pay_rate = 0.8  # Class attribute (The pay rate after 20% discount)
    all = []
    # We can also pass a default value on the parameters and make it optional attribute for our object

    def __init__(self, name: str, price: float, quantity):
        # Run validations to the received arguments
        # Assert is a statement keyword that is used to check if there is a match or not.
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assigning the instance attributes dynamically to the object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # Property Decorator = Read only attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Length of the name is more than 10 characters")
        else:
            self.__name = value

    def calculate_total_price(self):
        # We assigned price and quantity attributes once the instances has been created
        # which means that we have access to those attributes throughout the method in this class
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # Converting instance method to class method as this method is responsible for instantiating the object.
    # Class methods can be accessed from class level.
    # We need to use decorators to convert this method to class method.
    # Decorators in python is a way to change the behavior of the function.

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=int(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        if isinstance(num, float):
            # Count out the floats that are points zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
