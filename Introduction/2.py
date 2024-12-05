class Cake:
    def __init__(self, flavor):
        self.flavor = flavor

    def show_my_cake(self):
        if self.flavor == "":
            print("Обычный тортик")
        else:
            print(f"Торт со вкусом {self.flavor}")


