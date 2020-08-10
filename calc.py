"""
Free Code Camp calculator app
"""
import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

e = tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

temp_vals = []
temp_func = None

# Math funcs:
def adder(vals):
	result = 0
	for val in vals:
		result += val
	return result

def subtracter(vals):
	pass

# Math applier:
def operate(f, vals=temp_vals):
	return f(vals)

# Other funcs:
def button_click(num, temp=False, func=None, op=False):

	current = e.get()

	if temp:
		temp_vals.append(int(current))
		global temp_func
		temp_func = func
		e.delete(0, tk.END)
	elif op:
		temp_vals.append(int(current))
		result = operate(temp_func)
		e.delete(0, tk.END)
		e.insert(0, str(result))

	else:
		e.delete(0, tk.END)
		e.insert(0, str(current) + str(num))

	print(temp_vals)
	print(temp_func)

def button_clear():
	# reset field:
	e.delete(0, tk.END)
	
	# reset temp values & operator
	global temp_vals
	temp_vals = []
	global temp_func
	temp_func = None




# Define buttons:
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=90, pady=20, command=lambda: button_click(0))

button_add = tk.Button(root, text='+', padx=39, pady=20, command=lambda: button_click(None, temp=True, func=adder))
button_equal = tk.Button(root, text='=', padx=39, pady=20, command=lambda: button_click(None, op=True))
button_clear = tk.Button(root, text='C', padx=39, pady=20, command=button_clear)


# Put the buttons on the screen:
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0, columnspan=2)

button_add.grid(row=4, column=3)
button_equal.grid(row=5, column=3)
button_clear.grid(row=1, column=0)

root.mainloop()
