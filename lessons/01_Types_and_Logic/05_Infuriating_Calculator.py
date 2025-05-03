"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

from tkinter import messagebox, simpledialog, Tk  # Import required modules

window = Tk()        # Create a window object
window.withdraw()    # Hide the window; we just want to see pop ups

# Ask the user for the first number
number1 = simpledialog.askfloat("Very Nice Calculator", "Enter the first number:")

# Ask the user for the second number
number2 = simpledialog.askfloat("Very Nice Calculator", "Enter the second number:")

# Ask the user for the math operation
operation = simpledialog.askstring("Very Nice Calculator", "Enter the operation (add, subtract, multiply, divide):")

# Use if-elif-else statements to perform the operation
if operation == "add":
    result = number1 + number2
    messagebox.showinfo("Result", f"The result is: {result}")

elif operation == "subtract":
    result = number1 - number2
    messagebox.showinfo("Result", f"The result is: {result}")

elif operation == "multiply":
    result = number1 * number2
    messagebox.showinfo("Result", f"The result is: {result}")

elif operation == "divide":
    if number2 ==  0:
        messagebox.showerror("nuh uh.")
    else:
         result = number1 / number2
         messagebox.showinfo("Result", f"The result is: {result}")
else:
    messagebox.showerror("Error", f"Unknown operation: {operation}")

window.mainloop()

