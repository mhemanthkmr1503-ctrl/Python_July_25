class GrandFather():
    def land(self):
        print("2 Acres of Land")

class Father():
    def gold(self):
        print("100 grams of gold")

class Son(GrandFather,Father):
    def car(self):
        print("Tata Nexon")

son = Son()
son.gold()
son.land()
son.car()