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

        # Temporary value and operation:
        self.temp_val = None
        self.temp_op  = None

        # State marker for field:
        self.field_refresh = False

    def create_field(self):
        self.field = tk.Entry(self)
        self.field.grid(row=0,
                        column=0,
                        columnspan=5,
                        padx=5,
                        pady=5)

    def create_buttons(self):
        self.btn_1 = tk.Button(self, text="1", padx=40, pady=20,
                command=lambda: self.num_click(1))
        self.btn_2 = tk.Button(self, text="2", padx=40, pady=20,
                command=lambda: self.num_click(2))
        self.btn_3 = tk.Button(self, text="3", padx=40, pady=20,
                command=lambda: self.num_click(3))
        self.btn_4 = tk.Button(self, text="4", padx=40, pady=20,
                command=lambda: self.num_click(4))
        self.btn_5 = tk.Button(self, text="5", padx=40, pady=20,
                command=lambda: self.num_click(5))
        self.btn_6 = tk.Button(self, text="6", padx=40, pady=20,
                command=lambda: self.num_click(6))
        self.btn_7 = tk.Button(self, text="7", padx=40, pady=20,
                command=lambda: self.num_click(7))
        self.btn_8 = tk.Button(self, text="8", padx=40, pady=20,
                command=lambda: self.num_click(8))
        self.btn_9 = tk.Button(self, text="9", padx=40, pady=20,
                command=lambda: self.num_click(9))
        self.btn_0 = tk.Button(self, text="0", padx=85, pady=20,
                command=lambda: self.num_click(0))

        self.btn_c = tk.Button(self, text="C", padx=40, pady=20,
                command=self.clear_field)
        self.btn_e = tk.Button(self, text="=", padx=40, pady=20,
                command=lambda: self.button_click(self.equals))
        self.btn_a = tk.Button(self, text="+", padx=40, pady=20,
                command=lambda: self.button_click(self.add))
        self.btn_s = tk.Button(self, text="-", padx=40, pady=20,
                command=lambda: self.button_click(self.subtract))
        self.btn_m = tk.Button(self, text="x", padx=40, pady=20,
                command=lambda: self.button_click(self.multiply))
        self.btn_d = tk.Button(self, text="/", padx=40, pady=20,
                command=lambda: self.button_click(self.divide))
        self.btn_p = tk.Button(self, text=".", padx=40, pady=20,
                command=self.per_click)

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

        self.btn_p.grid(row=5, column=2)

    def num_click(self, num):
        if self.field_refresh == True:
            self.field.delete(0, tk.END)
            self.field.insert(0, str(num))
            self.field_refresh = False
        else:
            field_val = self.field.get()
            self.field.delete(0, tk.END)
            self.field.insert(0, str(field_val) + str(num))

    def per_click(self):
        if self.field_refresh == True:
            self.field.delete(0, tk.END)
            self.field.insert(0, ".")
            self.field_refresh = False
        else:
            field_val = self.field.get()
            self.field.delete(0, tk.END)
            self.field.insert(0, str(field_val) + ".")
        

    def button_click(self, op):
        """
        Performs or appends operations. If op already set in self.temp_op,
        perform self.temp_op and append op, otherwise only append op.
        """
        # marker for nums to whipe field next click
        self.field_refresh = True

        # Get value in field:
        field_val = self.field.get()

        # if field is empty, do nothing:
        if field_val == '': # is an empty field.get() really ''?
            return None

        # set type of field value:
        elif '.' in field_val:
            field_val = float(field_val)
        else:
            field_val = int(field_val)

        # otherwise, load val and op:
        if op != self.equals and self.temp_val==None:
            self.temp_val = field_val
            self.temp_op = op

        elif op != self.equals:
            if self.temp_op == self.equals:
                self.temp_op = op
                # and pass setting temp_val, remains the same
            else:
                self.temp_val = self.temp_op(field_val, self.temp_val)
                self.temp_op = op

            # reset field:
            field_output = self.temp_val

            # prefer int if no decimal val
            if field_output % 1 == 0:
                field_output = int(field_output)

            self.field.delete(0, tk.END)
            self.field.insert(0, str(field_output))

        else: # when op == self.equals
            self.temp_val = self.temp_op(field_val, self.temp_val)
            self.temp_op = self.equals

            # reset field:
            field_output = self.temp_val

            # prefer int if no decimal val
            if field_output % 1 == 0:
                field_output = int(field_output)

            self.field.delete(0, tk.END)
            self.field.insert(0, str(field_output))

    def clear_field(self):
        self.field.delete(0, tk.END)
        self.temp_val = None
        self.temp_op = None

    def equals(self):
        pass

    def add(self, num_1, num_2):
        return num_1 + num_2

    def subtract(self, sub_val, sub_from):
        return sub_from - sub_val

    def multiply(self, num_1, num_2):
        return num_1 * num_2

    def divide(self, divisor, dividend):
        return dividend / divisor

root = tk.Tk()
calc = Calculator(root)
calc.mainloop()
