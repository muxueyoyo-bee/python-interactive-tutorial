class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add(self, name, price, qty=1):
        self.items[name] = self.items.get(name, 0) + price * qty

    def total(self):
        return sum(self.items.values())

    def receipt(self):
        for name, amount in self.items.items():
            print(f"{name}: {amount} 元")
        print(f"合计: {self.total()} 元")

cart = ShoppingCart()
cart.add("Python入门", 59, 2)
cart.add("算法导论", 89, 1)
cart.add("键盘", 299)
cart.receipt()
