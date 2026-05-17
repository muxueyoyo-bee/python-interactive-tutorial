class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add(self, name, price, qty=1):
        self.items[name] = self.items.get(name, 0) + price * qty

    def total(self):
        return sum(self.items.values())

    def receipt(self):
        for name, amount in self.items.items():
            print(f"{name}: {amount} 鍏?)
        print(f"鍚堣: {self.total()} 鍏?)

cart = ShoppingCart()
cart.add("Python鍏ラ棬", 59, 2)
cart.add("绠楁硶瀵艰", 89, 1)
cart.add("閿洏", 299)
cart.receipt()
