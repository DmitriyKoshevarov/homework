class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self,owner, __model, __engine_power, color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.color = color

    def get_model(self):
        return (f'Модель: {self.__model}')

    def get_horsepower(self):
        return (f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        return (f'Мощность двигателя: {self.color}')

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        upper_color_variants = list(map(str.upper, self.__COLOR_VARIANTS))
        if new_color.upper() in upper_color_variants:
            self.color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}.")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)



# Изначальные свойства

vehicle1.print_info()



# Меняем свойства (в т.ч. вызывая методы)

vehicle1.set_color('Pink')

vehicle1.set_color('BLACK')

vehicle1.owner = 'Vasyok'



# Проверяем что поменялось

vehicle1.print_info()
