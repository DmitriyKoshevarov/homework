class Figure:

    def __init__(self,__color = (0,0,0), *sides):
        self.__color = __color
        self.__sides = list(sides)
        self.filled = False
        self.sides_count = len(sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return False
        return all(isinstance(side, int) and side > 0 for side in new_sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            return self.__sides

    def get_sides(self):
        return self.__sides

circle1 = Figure((200, 200, 100), 10)
circle1.set_sides(5, 3, 12, 4, 5) # Не изменится

print(circle1.get_sides())

circle1.set_sides(15) # Изменится

print(circle1.get_sides())

