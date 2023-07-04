from math import pi
from tkinter import *  # GUI - Graphics User Interface
from tkinter import filedialog
from PIL import Image, ImageTk  # Pillow

# Change

def get_size(obj):
    print(f'Размер: {obj.__sizeof__()} байт(а)')


# isinstance
def print_figure_info(figure):
    # o_type = type(figure).__name__
    if isinstance(figure, Square):
        print('Для квадрата:')
    elif isinstance(figure, Rectangle):
        print('Для прямоульника:')
    else:
        print('Для круга:')
    print(f'\tПлощадь={figure.area():.1f}\n\tПериметр={figure.perimeter():.1f}')


class Rectangle:
    def __init__(self, side1, side2):
        self.a = side1
        self.b = side2
        self.name = 'Прямоугольник'

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return (self.a + self.b) * 2

    def __eq__(self, other):
        if (self.a + self.b) == (other.a + other.b):
            return True
        else:
            return False

    def __ge__(self, other):
        if (self.a + self.b) >= (other.a + other.b):
            return True
        else:
            return False


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.name = 'Круг'

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side
        self.name = 'Квадрат'

    # def area(self):
    #     return self.side ** 2
    #
    # def perimeter(self):
    #     return self.side * 4


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def get_name(self):
        return self.name

    def set_author(self, new_author):
        self.author = new_author


class Car:
    count = 0  # СТАТИЧЕСКИЙ АТРИБУТ

    def __init__(self):
        self.engine_on = False  # пока не заведён
        Car.count += 1  # увеличиваем на 1

    def start_engine(self):
        self.engine_on = True  # завели

    def drive(self, place='работу'):
        if self.engine_on:
            print(f'Еду на {place}')
        else:
            print('Забыл завести мотор!')

    @staticmethod
    def get_count():
        return Car.count


class Fruit:
    def __init__(self, name, color, weight):
        self.name = name  # private
        self.color = color
        self.weight = weight

    def set_new_value(self, new_color, new_weight):  # setter
        self.color = new_color
        self.weight = new_weight

    def get_color(self):  # getter
        return self.color

    def get_info(self):
        print(f'{self.name}, '
              f'{self.color}, '
              f'{self.weight} гр.')


class Greeter:
    def say_hello(self):
        print('Hello')

    def hello_name(self, name):
        print(f'Hello, {name}')

    def hello_and_talk(self, name, weather):
        print(f'Hello, {name}')
        print(f'{name}, {weather}!')


class List:
    def __init__(self, n=0):
        if n == 0:
            self.a = []
        else:
            try:
                n = int(n)
                n = abs(n)
                self.a = [0 for i in range(n)]
            except ValueError:
                self.a = []

    def add(self, value=''):
        self.a.append(value)

    def clear(self):
        self.a.clear()

    def remove(self, value):
        try:
            self.a.remove(value)
        except:
            print('Элемента нет в списке')

    def show_list(self):
        print(*self.a, sep=', ')


class Special:
    def __init__(self):
        self.value = 10

    def __add__(self, other):
        return 'Выполнился __add__'

    def __radd__(self, other):
        return 'Выполнился __radd__'

    def __iadd__(self, other):
        self.value += other
        print('Выполнился __iadd__')
        return self

    def __str__(self):
        return f'Значение {self.value}.'


class Time:
    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f'{self.minutes:02d}:{self.seconds:02d}'

    def __repr__(self):
        return f'{self.minutes:02d}:{self.seconds:02d}'

    def __add__(self, other):
        m = self.minutes + other.minutes
        s = self.seconds + other.seconds
        m += s // 60
        s = s % 60
        return Time(m, s)


class Okno:
    def __init__(self):
        self.window = Tk()  # Инициализация GUI
        self.window.title('Добро пожаловать в Tkinter')
        self.window.geometry('800x600')
        self.window.resizable(False, False)
        self.lbl = Label(self.window, text='Картинка ниже')
        self.lbl.pack()
        self.canvas = Canvas(self.window, height=100, width=133)
        self.image = ImageTk.PhotoImage(Image.open('images/girl.jpg'))
        self.canvas.create_image(0, 0, anchor='nw', image=self.image)
        self.canvas.pack()
        self.btn = Button(self.window, text='Нажми', command=self.click)
        self.btn.pack()

        self.window.mainloop()

    def click(self):
        path = filedialog.askopenfilename()
        original = Image.open(path)
        w, h = original.size
        ratio = w / h
        if w > 133:
            original.resize((133, int(133 * ratio)))
        self.image = ImageTk.PhotoImage(original)
        self.canvas.create_image(0, 0, anchor='nw', image=self.image)

# 33333333333333333333333
# BASH

