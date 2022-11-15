class Laptop:
    _count = 0

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        first_price = price
        Laptop._count += 1

    def __str__(self):
        return f"Laptop:\nbrand - {self.brand} \nmodel - {self.model}" \
               f"\nprice - {self.price}"

    def get_price(self):
        return self.price

    def calculate_price(self):
        return self.first_price + self.price

    def finde_low_price(self):
        if self.first_price < self.price:
            return self.first_price
        return self.price



Laptop1 = Laptop("ACER", "Aspire3", 1000)
print(Laptop1.__str__())
Laptop2 = Laptop("Lenovo", "IdeaPad", 1600)
print(Laptop2.__str__())

msg = f"You have {Laptop._count} laptops."
print(msg)


price = Laptop.calculate_price()
print(price)

low_price = Laptop.finde_low_price()
print(low_price)


