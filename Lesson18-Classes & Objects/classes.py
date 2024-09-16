class Vehicle:  # 類包含了屬性跟方法，是一個object的藍圖，self不影響輸入參數時的輸入順序
    def __init__(self, make, model):  # self在定義變數裡也要加! 每個()裡面都加self讓其他方法可以用這裡創的變數
        self.make = make  # def __init__(self): 是標準格式這個object的屬性
        self.model = model

    def moves(self):
        print('Moves along..')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle('Tesla', 'Model 3')
# 創造my_car這個object，並給他命名，輸入__init__(也就是廠牌跟型號)裡面的參數
# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()  # 使用這個物件的方法
my_car.moves()

your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves()

# Polymorphism 多型，允許同一個方法在不同物件中有不同的行為

# inheritance繼承


class Airplane(Vehicle):  # class(放要繼承的類)
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)  # 可以繼承parent class裡的 make跟model屬性
        self.faa_id = faa_id

    def moves(self):  # 直接覆蓋舊的方法
        print('Flies along..')


class Truck(Vehicle):
    def moves(self):
        print('Rumbles along..')


class GolfCart(Vehicle):
    pass  # 完全繼承Vehicke這個類


cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')
# 創建opject

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()
# 創建方法

print('\n\n')

# 使用OOP物件導向的方法
# 物件為核心的程式設計範式。物件導向程式設計的目的是通過將資料和行為（方法）封裝在一起，來模擬現實世界中的實體，從而提高程式碼的可讀性、可維護性和重用性。
# OOP 的核心目標是讓程式更具結構性和模組化，便於擴展和維護。
for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()
