import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

def change_color():
    # Change the foreground color randomly
    import random
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
    random_color = random.choice(colors)
    label.config(foreground=random_color)
    label.after(5000, change_color)  # Change color every 5000 milliseconds (5 seconds)

# Create the main window
root = tk.Tk()
root.title("Creative Digital Clock")

# Set the window background color
root.configure(bg='black')

# Create a label to display the time
label = tk.Label(root, font=('Helvetica', 60, 'bold'), background='black', foreground='white')

# Pack the label to the center of the window
label.pack(anchor='center')

# Call the update_time function to display the time and update it every second
update_time()

# Call the change_color function to change the text color every 5 seconds
change_color()

# Run the main loop
root.mainloop()
