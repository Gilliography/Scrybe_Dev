import tkinter as tk
from tkinter import *
import tkinter.messagebox
from forex_python.converter import CurrencyRates

# Function to perform real-time currency conversion
def RealTimeCurrencyConversion():
    c = CurrencyRates()
    from_currency = variable1.get()
    to_currency = variable2.get()

    try:
        if Amount1_field.get() == "":
            tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please enter a valid amount.")
        elif from_currency == "currency" or to_currency == "currency":
            tkinter.messagebox.showinfo("Error !!", "Currency Not Selected.\n Please select FROM and TO currencies from the menu.")
        else:
            new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
            new_amount = float("{:.4f}".format(new_amt))
            Amount2_field.delete(0, tk.END)  # Clear any previous value
            Amount2_field.insert(0, str(new_amount))
    except Exception as e:
        tkinter.messagebox.showinfo("Error !!", f"An error occurred: {str(e)}")

# Clearing all the data entered by the user
def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Currency Converter: GeeksForGeeks")
root.configure(background='#e6e5e5')
root.geometry("700x400")

# Header
Tops = Frame(root, bg='#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)
headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text='Currency Converter: GeeksForGeeks', bg='#e6e5e5', fg='black')
headlabel.grid(row=1, column=0, sticky=W)

# Currency variables
variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)
variable1.set("currency")
variable2.set("currency")

# Labels and Entries
labels_texts = ["Amount:", "From Currency:", "To Currency:", "Converted Amount:"]
for i, text in enumerate(labels_texts, start=2):
    label = tk.Label(root, font=('lato black', 15, 'bold'), text=f"\t{text} ", bg="#e6e5e5", fg="black")
    label.grid(row=i, column=0, sticky=W)

# Currency selection options
CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR", "KES"]
FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)
FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky=E)
ToCurrency_option.grid(row=4, column=0, ipadx=45, sticky=E)

# Input and output fields
Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)
Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)

# Buttons
convert_button = Button(root, font=('arial', 15, 'bold'), text="Convert", padx=2, pady=2, bg="lightblue", fg="white", command=RealTimeCurrencyConversion)
convert_button.grid(row=6, column=0)
clear_button = Button(root, font=('arial', 15, 'bold'), text="Clear All", padx=2, pady=2, bg="lightblue", fg="white", command=clear_all)
clear_button.grid(row=10, column=0)

root.mainloop()
