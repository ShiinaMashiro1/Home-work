import tkinter as tk
from tkinter import messagebox

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

class Math:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y
    def subtraction(self):
        return self.x - self.y
    def multiplication(self):
        return self.x * self.y
    def division(self):
        return self.x / self.y


class Button:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Кнопка")
        self.btn = tk.Button(
            self.root,
            text="Это кнопка",
            command=self.show_message,
            padx=20,
            pady=10,
            bg="White"
        )
        self.btn.pack(padx=50, pady=30)
        self.root.mainloop()

    def show_message(self):
        messagebox.showinfo(
            "Сообщение",
            "Вы нажали на кнопку"
        )


if __name__ == '__main__':
    a = Rectangle(200,100)
    print(a.area())
    print(a.perimeter())

    b = Rectangle(50,100)
    print(b.area())
    print(b.perimeter())

    c = Rectangle(10,100)
    print(c.area())
    print(c.perimeter())

    MC = Math(10,10)
    print(MC.addition())
    print(MC.subtraction())
    print(MC.multiplication())
    print(MC.division())

    button = Button()