class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.__password = password
        self.email = email
    def set_password(self, new_password):
        self.__password = new_password
    def check_password(self, password):
        return self.__password == password
User=UserAccount("Jim", "A@Gmail.com ", "paSsw0rd")
print(f'Старый пароль верен: {User.check_password("paSsw0rd")}')
User.set_password("Passw0rd")
print('Пароль успешно изменен')
print(f'Старый пароль был верен: {User.check_password("paSsw0rd")}')
print(f'Новый пароль верен: {User.check_password("Passw0rd")}')

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"
car=Vehicle("Honda","Honda123")
print(car.get_info())
class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        Vehicle.__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        base_info= Vehicle.get_info()
        return f"{base_info}, Топливо: {self.fuel_type}"
v=Vehicle("Honda","Honda123")
c=Car("Honda","Honda123", 'дизель')
print(v.get_info())
print(c.get_info())

