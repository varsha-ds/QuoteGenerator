import tkinter as tk
import random

# List of quotes
quotes = [
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt",
    "Life is what happens when you're busy making other plans. - John Lennon"
]

def generate_random_quote():
    """
    Generate a random quote from the list of quotes.
    """
    return random.choice(quotes)

def generate_quote():
    """
    Callback function to generate and display a random quote.
    """
    quote = generate_random_quote()
    quote_label.config(text=quote)

# Create main window
root = tk.Tk()
root.title("Quote Generator")

# Create quote label
quote_label = tk.Label(root, text="", wraplength=300, font=("Arial", 12))
quote_label.pack(pady=20)

# Create generate button
generate_button = tk.Button(root, text="Generate Quote", command=generate_quote)
generate_button.pack(pady=10)

# Run the application
root.mainloop()
