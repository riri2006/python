class Shop:

    def __init__(self, shop_name):
        self.shop_name = shop_name

        self.items(
            "Laptop",
            "Mobile",
            "Headphones",
            "Keyboard",
            "Mouse",
            "Monitor"
        )

    def owner(self, owner_name):
        self.owner_name = owner_name
        print("Owner Name:", self.owner_name)

    def items(self, item1, item2, item3, item4, item5, item6):
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.item4 = item4
        self.item5 = item5
        self.item6 = item6

        print("Shop Name:", self.shop_name)
        print("Item 1:", self.item1)
        print("Item 2:", self.item2)
        print("Item 3:", self.item3)
        print("Item 4:", self.item4)
        print("Item 5:", self.item5)
        print("Item 6:", self.item6)


object = Shop("Tech World")

object.owner("Rahul")
