import tkinter as tk
from tkinter import ttk

# Define the application's window
root = tk.Tk()
root.title("TFT Probability Calculator")
root.geometry("500x300")
root.attributes("-topmost", True)

# Styling
style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', background='#333', foreground='#FFF', font=('Helvetica', 12))
style.configure('TButton', background='#333', foreground='#FFF', font=('Helvetica', 12))
style.configure('TEntry', foreground='#333', font=('Helvetica', 12))
root.configure(bg='#333')

# Updated rolling odds for TFT
rolling_odds = {
    1: [100, 0, 0, 0, 0],
    2: [100, 0, 0, 0, 0],
    3: [75, 25, 0, 0, 0],
    4: [55, 30, 15, 0, 0],
    5: [45, 30, 20, 2, 0],
    6: [30, 40, 25, 5, 0],
    7: [19, 35, 35, 10, 1],
    8: [18, 25, 36, 18, 3],
    9: [10, 20, 25, 35, 10],
    10: [5, 10, 20, 40, 25],
    11: [1, 2, 12, 50, 35]
}

# Updated pool sizes based on standard TFT set information
pool_size = {
    1: 29,
    2: 22,
    3: 18,
    4: 12,
    5: 10
}

def calculate_probability():
    try:
        level = int(level_entry.get())
        tier = int(tier_entry.get())
        taken = int(taken_entry.get())

        odds = rolling_odds[level][tier - 1] / 100
        remaining = pool_size[tier] - taken
        probability = odds * remaining / pool_size[tier]
        probability_percent = round(probability * 100, 2)
        result_label.config(text=f"Probability: {probability_percent}%")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers only.")

# UI Layout
level_label = ttk.Label(root, text="Your Level (1-11):", background='#333')
level_label.pack(padx=10, pady=5)

level_entry = ttk.Entry(root)
level_entry.pack(padx=10, pady=5)

tier_label = ttk.Label(root, text="Champion Tier (1-5):", background='#333')
tier_label.pack(padx=10, pady=5)

tier_entry = ttk.Entry(root)
tier_entry.pack(padx=10, pady=5)

taken_label = ttk.Label(root, text="Champs Taken by Others:", background='#333')
taken_label.pack(padx=10, pady=5)

taken_entry = ttk.Entry(root)
taken_entry.pack(padx=10, pady=5)

calculate_button = ttk.Button(root, text="Calculate", command=calculate_probability)
calculate_button.pack(padx=10, pady=10)

result_label = ttk.Label(root, text="Probability: ", background='#333')
result_label.pack(padx=10, pady=5)

root.mainloop()
