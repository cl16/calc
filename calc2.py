"""
Object-based version of calculator app.
"""
import tkinter as tk


class Calculator(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_field()
        self.create_buttons()

    def create_field(self):
        self.field = tk.Entry(self)
        self.field.grid(row=0,
                        column=0,
                        columnspan=5,
                        padx=5,
                        pady=5)

    def create_buttons(self):
        self.btn_1 = tk.Button(self, text="1", padx=40, pady=20,
                command=lambda: self.button_click(1))
        self.btn_2 = tk.Button(self, text="2", padx=40, pady=20,
                command=lambda: self.button_click(2))
        self.btn_3 = tk.Button(self, text="3", padx=40, pady=20,
                command=lambda: self.button_click(3))
        self.btn_4 = tk.Button(self, text="4", padx=40, pady=20,
                command=lambda: self.button_click(4))
        self.btn_5 = tk.Button(self, text="5", padx=40, pady=20,
                command=lambda: self.button_click(5))
        self.btn_6 = tk.Button(self, text="6", padx=40, pady=20,
                command=lambda: self.button_click(6))
        self.btn_7 = tk.Button(self, text="7", padx=40, pady=20,
                command=lambda: self.button_click(7))
        self.btn_8 = tk.Button(self, text="8", padx=40, pady=20,
                command=lambda: self.button_click(8))
        self.btn_9 = tk.Button(self, text="9", padx=40, pady=20,
                command=lambda: self.button_click(9))
        self.btn_0 = tk.Button(self, text="0", padx=85, pady=20,
                command=lambda: self.button_click(0))

        self.btn_c = tk.Button(self, text="C", padx=40, pady=20,
                command=self.clear_field)
        self.btn_e = tk.Button(self, text="=", padx=40, pady=20,
                command=self.equals)
        self.btn_a = tk.Button(self, text="+", padx=40, pady=20,
                command=self.add)
        self.btn_s = tk.Button(self, text="-", padx=40, pady=20,
                command=self.subtract)
        self.btn_m = tk.Button(self, text="x", padx=40, pady=20,
                command=self.multiply)
        self.btn_d = tk.Button(self, text="/", padx=40, pady=20,
                command=self.divide)

        # Place buttons:
        self.btn_1.grid(row=4, column=0)
        self.btn_2.grid(row=4, column=1)
        self.btn_3.grid(row=4, column=2)
        self.btn_4.grid(row=3, column=0)
        self.btn_5.grid(row=3, column=1)
        self.btn_6.grid(row=3, column=2)
        self.btn_7.grid(row=2, column=0)
        self.btn_8.grid(row=2, column=1)
        self.btn_9.grid(row=2, column=2)
        self.btn_0.grid(row=5, column=0, columnspan=2)

        self.btn_c.grid(row=1, column=0)
        self.btn_e.grid(row=5, column=3)
        self.btn_a.grid(row=4, column=3)
        self.btn_s.grid(row=3, column=3)
        self.btn_m.grid(row=2, column=3)
        self.btn_d.grid(row=1, column=3)

    def button_click(self, num):
        field_val = self.field.get()
        self.field.delete(0, tk.END)
        self.field.insert(0, str(field_val) + str(num))

    def clear_field(self):
        self.field.delete(0, tk.END)

    def equals(self):
        pass

    def add(self):
        pass

    def subtract(self):
        pass

    def multiply(self):
        pass

    def divide(self):
        pass

root = tk.Tk()
calc = Calculator(root)
calc.mainloop()
