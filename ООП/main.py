"""
ООП - обьектно орентированное программирование
"""

class Marker():
    def __init__(self, color) -> None:
        self.color = color

    def write(self, word):
        return f'Я написал {word} цветом {self.color} маркером'

class User():
    def __init__(self, login, password) -> None:
        self.__login = login
        self.__password = password
        self.history = []

    def get_login(self):
        return self.login
    
    def get_password(self):
        return self.password
    
    def upgrade_login(self, login):
        self.login = login
        return self.login
    
    def upgrade_password(self, password):
        self.password = password
        return self.password

user_one = User('Jibo@gmail.com', "12345678")
user_two = User('Kirill@gmail.com', "87654321")
"""print(f"Login:{user_one.get_login()}, Password:{user_one.get_password()}")
user_one.upgrade_login('Himaki@gmail.com')
print(f'New login: {user_one.get_login()}')"""

user_one.__login = 50
print(user_one.__login)
user_one.__login = "asdsafhreh"
print(user_one.__login)


"""
св-во login, password
методы
1. Получить login
2. Получить password
3. Изменить login
4. Изменить password
"""

class Fraction:
    def __init__(self, numerator, denominator) -> None:
        self.__numerator = numerator
        self.__denominator = denominator

    def output_fraction(self):
        return f"{self.__numerator}/{self.__denominator}"
    
    def get_numerator(self):
        return self.__numerator
    
    def get_denominator(self):
        return self.__denominator
    
    def sum(self, other_fraction):
        new_numerator =  self.__numerator * other_fraction.get_denominator() + other_fraction.get_numerator() * self.__denominator
        new_denominator = self.__denominator * other_fraction.get_denominator()
        return Fraction(new_numerator, new_denominator)
    
    def minus(self, other_fraction):
        new_numerator =  self.__numerator * other_fraction.get_denominator() - other_fraction.get_numerator() * self.__denominator
        new_denominator = self.__denominator * other_fraction.get_denominator()
        return Fraction(new_numerator, new_denominator)
    
    def multiply(self, other_fraction):
        new_numerator = self.__numerator * other_fraction.get_numerator()
        new_denominator = self.__denominator * other_fraction.get_denominator()
        return Fraction(new_numerator, new_denominator) 

    def divide(self, other_fraction):
        new_numerator = self.__numerator * other_fraction.get_denominator()
        new_denominator = self.__denominator * other_fraction.get_numerator()
        return Fraction(new_numerator, new_denominator)

frac_one = Fraction(1, 2)
frac_two = Fraction(3, 4)
result = frac_one.sum(frac_two)
print(result.output_fraction())
x = 5
print(type(x))
print(type(frac_two))
x = str(x)
print(type(x))