import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 
class RestrauntOrderManagenent:
    def __init__(self, root):
        self.root= root
        self.root.title('Restraunt Management System')
        self.menu_items = {
            'fries meal': '4',
            'lunch meal': '4',
            'burger meal': '3',
            'pizza meal': '6',
            'cheese burger meal': '3.5',
            'drinks': '1'
        }
        self.exchange_rate = 82
        self.setup_background(root)
        frame= tk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor= tk.CENTER)
        ttk.Label(
            frame,
            text='Restraunt Management System',
            font=('Arial', 20, 'bold')
        ).grid(row=0, columnspan=3, padx=10, pady=10)

        self.menu_labels= {}
        self.menu_quantities= {}
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label= ttk.Label(
            frame,
            text= f'{item}, ${price}',
            font = ('Arial', 12)
            )
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item]= label
            quantity_entry= ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item]= quantity_entry
        self.currency_var= tk.StringVar
        ttk.Label(
            frame,
            text= 'Currency',
            font= ('Arial', 10)
        ).grid(
            row= len(self.menu_items),
            column=0,
            padx=10,
            pady=5
            )
        currency_dropdown= ttk.Combobox(
            frame,
            textvariable= self.currency_var,
            state= 'readonly',
            width= 18,
            values = ['USD', 'INR']
        )
        currency_dropdown.grid(
            row = len(self.menu_items) + 1,
            column= 1,
            padx = 10,
            pady= 5
        )
        currency_dropdown.current(0)
        self.currency_var.trace('w', self.update_menu_prices)
        order_button= ttk.Button(
            frame,
            text= 'place order',
            command=self.place_order
        )
        order_button.grid(
            row= len(self.menu_items)+ 2,
            columnspan=3,
            padx=10,
            pady=10
        )
    def setup_background(self, root):
        bg_width, bg_height= 800, 600
        canvas = tk.Canvas(root, width=bg_width, height=bg_height)
        canvas.pack()
        original_image = tk.PhotoImage(file = 'background.jpeg')
        background_image = original_image.subsample(
            original_image.width // bg_width,
            original_image.height // bg_height,
        )
    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = '₹' if currency == 'INR' else '$'
        rate = self.exchange_rate if currency == 'INR' else 1
        for items, price in self.menu_labels.items():
            price = self.menu_items[items] * rate
    def place_order(self):
        total_cost = 0
        order_summary = ' Order Summary:\n'
        currency = self.currency_var.get()
        symbol = '₹' if currency == 'INR' else '$'
        rate = self.exchange_rate if currency == 'INR' else 1
        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                if quantity > 0:
                    price = self.menu_items[item] * rate
                    cost = quantity * price
                    total_cost += cost
                    if quantity > 0:
                        order_summary += (
                            f'{item}: {quantity} x {symbol}{price:2f} = {symbol}{cost}\n'
                        )
        if total_cost > 0:
            order_summary += f'Total Cost: {symbol}{total_cost}'
            messagebox.showinfo('Order Summary', order_summary)
        else:
            messagebox.showwarning('ERROR', 'Please order atleast one item')
if __name__ == '__main__':
    root = tk.Tk()
    app = RestrauntOrderManagenent(root)
    root.geometry('800x600')
    root.mainloop()
                    


        


