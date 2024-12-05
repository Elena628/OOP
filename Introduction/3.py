class Numbers:
    limit = [0, 100]
    def set_data(self, data):
        self.data = data

    def drow(self):
        print(" ".join(str(x) for x in self.data if Numbers.limit[0] <= x <= Numbers.limit[1]))


numb = Numbers()
numb.set_data([1, 2, 3, 4, 5, 1000, 200, 6, 7, 300])
numb.drow()

