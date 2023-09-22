import tkinter as tk

def UpiLinkGenerator(upi_address, name, amount, text):
    # Your UPI link generation logic here
    return f"upi://pay?pa={upi_address}&pn={name}&cu=INR&tn={text}&am={amount}"

def show_resource_input():
    upi_address = upi_address_entry.get()
    name = upi_name_entry.get()
    
    # Hide UPI input frame
    upi_frame.pack_forget()
    
    # Show resource input frame
    resource_frame.pack(padx=10, pady=10, fill='both', expand=True)
    resource_name.focus_set()  # Set focus on the resource_name Entry field

def add_resource():
    name = resource_name.get()
    price = resource_price.get()
    if name and price:
        resources_list.append((name, price))
        update_resource_list()
        resource_name.delete(0, tk.END)
        resource_price.delete(0, tk.END)

def remove_resource_entry():
    resource_name.delete(0, tk.END)
    resource_price.delete(0, tk.END)

def generate_upi_link():
    upi_address = upi_address_entry.get()
    name = upi_name_entry.get()
    total_amount = sum([int(price) for _, price in resources_list])
    upi_link = UpiLinkGenerator(upi_address, name, total_amount, "Resource Payment")
    link_label.config(text=upi_link)

def show_resource_tiles():
    resource_frame.pack_forget()
    remove_button.pack_forget()  # Remove the "Resource Added" button
    generate_upi_link()
    update_tiles()  # Display resource tiles
    generate_link_button.pack(side='top', anchor='ne', padx=10, pady=10)
    final_amount_label.pack()

app = tk.Tk()
app.title("Resource Tracker")

# UPI input frame
upi_frame = tk.Frame(app)
upi_frame.pack(padx=10, pady=10, fill='both', expand=True)

upi_address_label = tk.Label(upi_frame, text="UPI Address:")
upi_address_label.grid(row=0, column=0, padx=10, pady=5)

upi_address_entry = tk.Entry(upi_frame)
upi_address_entry.grid(row=0, column=1, padx=10, pady=5)

upi_name_label = tk.Label(upi_frame, text="Your Name:")
upi_name_label.grid(row=1, column=0, padx=10, pady=5)

upi_name_entry = tk.Entry(upi_frame)
upi_name_entry.grid(row=1, column=1, padx=10, pady=5)

enter_button = tk.Button(upi_frame, text="Enter", command=show_resource_input)
enter_button.grid(row=2, columnspan=2, padx=10, pady=10)

# Resource input frame (Initially hidden)
resource_frame = tk.Frame(app)

resource_name_label = tk.Label(resource_frame, text="Resource Name:")
resource_name_label.grid(row=0, column=0, padx=10, pady=5)

resource_name = tk.Entry(resource_frame)
resource_name.grid(row=0, column=1, padx=10, pady=5)

resource_price_label = tk.Label(resource_frame, text="Resource Price (Rs.):")
resource_price_label.grid(row=1, column=0, padx=10, pady=5)

resource_price = tk.Entry(resource_frame)
resource_price.grid(row=1, column=1, padx=10, pady=5)

add_button = tk.Button(resource_frame, text="Add Resource", command=add_resource)
add_button.grid(row=2, column=0, padx=10, pady=10)

resource_listbox = tk.Listbox(resource_frame, font=("Helvetica", 12), selectmode=tk.SINGLE, height=5)
resource_listbox.grid(row=3, columnspan=2, padx=10, pady=10)

remove_button = tk.Button(resource_frame, text="Resource Added", command=show_resource_tiles)
remove_button.grid(row=4, columnspan=2, padx=10, pady=10)

resource_list_label = tk.Label(resource_frame, text="Resource List:", font=("Helvetica", 14))
resource_list_label.grid(row=5, columnspan=2, padx=10, pady=10)

link_label = tk.Label(app, text="", font=("Helvetica", 12))

generate_link_button = tk.Button(app, text="Generate Link", command=generate_upi_link)

final_amount_label = tk.Label(app, text="Total Amount: Rs.0", font=("Helvetica", 14))

resources_list = []  # List to store resources (name, price) tuples
resource_tiles = []  # List to store resource tiles

def update_resource_list():
    resource_listbox.delete(0, tk.END)
    for name, price in resources_list:
        resource_listbox.insert(tk.END, f"{name} - Rs.{price}")

def update_tiles():
    for tile in resource_tiles:
        tile.destroy()
    
    for i, (name, price) in enumerate(resources_list):
        row_num = i // 4
        col_num = i % 4
        
        tile = tk.Frame(app, width=200, height=100, relief=tk.RAISED, borderwidth=2)
        tile.pack(side='left', padx=10, pady=10, fill='both', expand=True)
        
        name_label = tk.Label(tile, text=name, font=("Helvetica", 12), padx=10, pady=10)
        name_label.pack(fill='both', expand=True)
        
        price_label = tk.Label(tile, text=f"Price: Rs.{price}", font=("Helvetica", 10), padx=10, pady=5)
        price_label.pack(side='bottom', anchor='se')
        
        quantity_label = tk.Label(tile, text="Quantity: 0", font=("Helvetica", 10), padx=10, pady=5)
        quantity_label.pack(side='bottom', anchor='sw')
        
        tile.bind("<Button-1>", lambda event, index=i: on_tile_click(index, quantity_label))

def on_tile_click(index, quantity_label):
    name, price = resources_list[index]
    resources_list[index] = (name, price)
    current_quantity = int(quantity_label.cget("text").split(":")[1])
    new_quantity = current_quantity + 1
    quantity_label.config(text=f"Quantity: {new_quantity}")
    update_final_amount()

def update_final_amount():
    total_amount = sum([int(price) for _, price in resources_list])
    final_amount_label.config(text=f"Total Amount: Rs.{total_amount}")

app.mainloop()
