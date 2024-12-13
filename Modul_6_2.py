class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white', 'orange']
    def __init__(self, owner, _model, _engine_power, _color):
        self.owner = owner
        self._model = _model
        self._engine_power = _engine_power
        self._color = _color

    def get_model(self):
        return str(f'Модель: {self._model}')
    def get_horsepower(self):
        return str(f'Мощность двигателя: {self._engine_power}')
    def get_color(self):
        return str(f'Цвет: {self._color}')
    def get_owner(self):
        return str(f'Владелец: {self.owner}')
    def print_info(self):
        print(self._model)
        print(self._engine_power)
        print(self._color)
        print(self.owner)
    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self._color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500 , 'blue')

vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('GREEN')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()