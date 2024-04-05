import tkinter as tk

# Function to generate code
def generate_code(event=None):  # Added event parameter for binding
    cost = cost_entry.get()
    list_of_digits = [int(i) for i in str(cost)]
    code = ""
    linkage = {}
    for i in range(1, len(word)):
        linkage[i] = word[i - 1]
    linkage[0] = word[len(word) - 1]
    for i in list_of_digits:
        code += linkage[i]
    code_label.config(text=code, font=("Arial", 25, "bold"))  # Set font properties

# Create main window
root = tk.Tk()
root.title("Code Generator")
root.geometry("300x150")  # Setting window size to 300x150 pixels

# Word
word = "MOTHERLAND"

# Cost entry
cost_label = tk.Label(root, text="Enter the cost:")
cost_label.pack()
cost_entry = tk.Entry(root)
cost_entry.pack()

# Set focus to entry widget
cost_entry.focus()

# Bind event to generate code instantly when typing
cost_entry.bind("<KeyRelease>", generate_code)

# Label to display generated code
code_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
code_label.pack()

root.mainloop()
