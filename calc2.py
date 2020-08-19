"""
Object-based version of calculator app, based off simple calculator from
Free Code Camp Tkinter tutorial.
"""
import tkinter as tk  


def num_sep(num_str):
    """Separate with a comma (',') after every 3rd non-starting digit"""
    result = ''
    decimal = False
    if '.' in num_str:
        decimal = True
        num_str_split = num_str.split('.')
        num_str = num_str_split[0]
        decimal_digits = num_str_split[-1]
    num_str = num_str[::-1]
    
    chars = 0
    for char in num_str:
        if chars != 0 and chars % 3 == 0:
            result += ','
            chars = 0
        chars += 1
        result += char
    
    if decimal:
        return result[::-1] + '.' + decimal_digits
    else:
        return result[::-1]


class Calculator(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_field()
        self.create_buttons() 
        self.field_overwrite = True
        self.sign = True
        self.val = None
        self.opr = None
        self.last_num = None
        self.last_opr = None
        self.temp_val = None
        self.temp_opr = None
        self.ord = {self.multiply: 2,
                    self.divide:   2,
                    self.add:      1,
                    self.subtract: 1,
                    self.equals:   0}
        # set initial field value to 0:
        self.put_field('0')

    def create_field(self):
        self.field = tk.Entry(self)
        self.field.grid(row=0,
                        column=0,
                        columnspan=5,
                        padx=5,
                        pady=5,
                        ipadx=35,
                        ipady=10)

    def get_field(self):
        """Extract values from window field."""
        field_str = self.field.get()
        if field_str == '':
            return None
        field_str = field_str.replace(',', '')
        if '.' in field_str:
            if field_str[-1] == '.': # if in process of entering decimal
                return field_str
            num = float(field_str)
            # if num % 1 == 0:
            #     num = int(num)
        else:
            num = int(field_str)
        return num

    def put_field(self, value, current=False):
        """Write values to window field."""
        if isinstance(value, float):
            if value != 0 and value % 1 == 0:
                value = int(value)
        if current:
            current_val = str(self.get_field())
        value = current_val + str(value) if current else str(value)
        value = num_sep(value) # separate digits with commas
        self.field.delete(0, tk.END)
        self.field.insert(0, value)

    def num_click(self, num):
        """Button-click of calculator numbers."""
        if self.field_overwrite == True:
            self.put_field(num)
            self.last_num = self.get_field()
            self.field_overwrite = False
        else:
            self.put_field(num, current=True)
            self.last_num = self.get_field()
    
    def opr_click(self, opr):
        """Button-click of calculator "operator" buttons. I.e. +, -."""
        self.field_overwrite = True
        self.last_opr = opr
        if self.opr != None and self.ord[opr] > self.ord[self.opr]:
            self.temp_val = self.val
            self.temp_opr = self.opr
            self.val = self.get_field()
            self.opr = opr
        else:
            if self.opr == None:
                self.opr = opr
                self.val = self.get_field()
            else:
                self.equals()
                if self.temp_val != None:
                    self.equals(temp=True)
                self.opr = opr
                self.val = self.get_field()

    def per_click(self):
        """Button-click of decimal "dot"."""
        if self.field_overwrite == True:
            self.put_field('0.')
            self.field_overwrite = False
        else:
            field_val = str(self.get_field())
            if '.' not in field_val:
                new_field_val = field_val + '.'
                self.put_field(new_field_val) # current val concatenation handled before put_field()

    def clear_field(self):
        """
        Clear window field and all temporary values, restore to initial
        state.
        """
        self.put_field('0')
        self.temp_val = None
        self.temp_op = None
        self.last_num = None
        self.last_opr = None
        self.field_overwrite = True

    def equals(self, temp=False):
        """
        Finalize operation or chain of operations.

        :param temp: bool, if lower-order pending operation
        """
        self.field_overwrite = True
        temp = True if self.temp_val != None else temp
        cur_opr = self.opr if self.opr != None else self.last_opr
        if cur_opr == None:
            return None # no opr selected at all yet
        elif temp==False:
            self.val = cur_opr(self.val, self.last_num) # change to multi-digit num ability
            self.put_field(self.val)
            self.opr = None
        else:
            self.val = cur_opr(self.val, self.last_num)
            self.val = self.temp_opr(self.temp_val, self.val)
            self.put_field(self.val)
            self.opr = None

            # used temp_val, temp_opr, reset:
            self.temp_val = None
            self.temp_opr = None

    def add(self, num_1, num_2):
        return num_1 + num_2

    def subtract(self, num_1, num_2):
        return num_1 - num_2

    def multiply(self, num_1, num_2):
        return num_1 * num_2

    def divide(self, dividend, divisor):
        return dividend / divisor

    def plusMinus(self):
        """Set sign of field value in-place."""
        field_val = self.get_field()
        if field_val == 0:
            return None
        else:
            value = field_val * -1
            self.field_overwrite=True
            self.num_click(value)

    def percent(self):
        """Convert field value to fraction of 100."""
        field_val = self.get_field()
        percentage = field_val / 100
        self.put_field(percentage)
        self.field_overwrite = True

    def create_buttons(self):
        self.btn_1 = tk.Button(self, text="1", height=3, width=6,
                command=lambda: self.num_click(1))
        self.btn_2 = tk.Button(self, text="2", height=3, width=6,
                command=lambda: self.num_click(2))
        self.btn_3 = tk.Button(self, text="3", height=3, width=6,
                command=lambda: self.num_click(3))
        self.btn_4 = tk.Button(self, text="4", height=3, width=6,
                command=lambda: self.num_click(4))
        self.btn_5 = tk.Button(self, text="5", height=3, width=6,
                command=lambda: self.num_click(5))
        self.btn_6 = tk.Button(self, text="6", height=3, width=6,
                command=lambda: self.num_click(6))
        self.btn_7 = tk.Button(self, text="7", height=3, width=6,
                command=lambda: self.num_click(7))
        self.btn_8 = tk.Button(self, text="8", height=3, width=6,
                command=lambda: self.num_click(8))
        self.btn_9 = tk.Button(self, text="9", height=3, width=6,
                command=lambda: self.num_click(9))
        self.btn_0 = tk.Button(self, text="0", height=3, width=13,
                command=lambda: self.num_click(0))

        self.btn_c = tk.Button(self, text="C", height=3, width=6,
                command=self.clear_field)
        self.btn_e = tk.Button(self, text="=", height=3, width=6,
                command=self.equals)
        self.btn_a = tk.Button(self, text="+", height=3, width=6,
                command=lambda: self.opr_click(self.add))
        self.btn_s = tk.Button(self, text="-", height=3, width=6,
                command=lambda: self.opr_click(self.subtract))
        self.btn_m = tk.Button(self, text="x", height=3, width=6,
                command=lambda: self.opr_click(self.multiply))
        self.btn_d = tk.Button(self, text="/", height=3, width=6,
                command=lambda: self.opr_click(self.divide))
        self.btn_p = tk.Button(self, text=".", height=3, width=6,
                command=self.per_click)
        self.btn_pm = tk.Button(self, text="+/-", height=3, width=6,
                command=self.plusMinus)
        self.btn_pc = tk.Button(self, text="%", height=3, width=6,
                command=self.percent)

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
        self.btn_pm.grid(row=1, column=1)
        self.btn_pc.grid(row=1, column=2)


root = tk.Tk()
calc = Calculator(root)
calc.mainloop()

