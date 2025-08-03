import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests


API_KEY = 'b11b18c31821432f902b85a4cd94caac'

def get_recipes(diet, disliked, number=3):
    API_URL = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        'diet': diet if diet else None,
        'excludeIngredients': disliked if disliked else None,
        'number': number,
        'apiKey': API_KEY,
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    if response.status_code != 200 or "results" not in data:
        return []
    recipes = [(r['title'], r['id']) for r in data.get('results', [])]
    return recipes

def get_ingredients(recipe_id):
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    params = {'apiKey': API_KEY}
    response = requests.get(url, params=params)
    data = response.json()
    if response.status_code != 200:
        return []
    return [ing['original'] for ing in data.get('extendedIngredients', [])]

def generate_plan():
    diet = diet_var.get().strip()
    disliked = dislike_var.get().strip()
    recipes = get_recipes(diet, disliked)
    output_text.delete(1.0, tk.END)
    if not recipes:
        messagebox.showerror("No Recipes", "No recipes found. Try fewer restrictions or check your API key.")
        return
    plan = []
    shopping = []
    for title, rid in recipes:
        ings = get_ingredients(rid)
        plan.append({'title': title, 'ingredients': ings})
        shopping.extend(ings)
    # Display plan
    output_text.insert(tk.END, "Today's Meal Plan:\n")
    for meal in plan:
        output_text.insert(tk.END, f"- {meal['title']}\n")
    output_text.insert(tk.END, "\nShopping List:\n")
    for item in set(shopping):
        output_text.insert(tk.END, f"- {item}\n")

# --- Tkinter GUI setup ---
root = tk.Tk()
root.title("Agentic AI Meal Planner")

tk.Label(root, text="Meal Planner", font=("Arial", 16, "bold")).pack(pady=10)

form = tk.Frame(root)
form.pack(pady=5)

tk.Label(form, text="Diet (optional):").grid(row=0, column=0, sticky=tk.E)
diet_var = tk.StringVar()
tk.Entry(form, textvariable=diet_var, width=30).grid(row=0, column=1)

tk.Label(form, text="Exclude ingredients (comma-separated, optional):").grid(row=1, column=0, sticky=tk.E)
dislike_var = tk.StringVar()
tk.Entry(form, textvariable=dislike_var, width=30).grid(row=1, column=1)

tk.Button(root, text="Generate Meal Plan", command=generate_plan).pack(pady=10)

output_text = scrolledtext.ScrolledText(root, width=50, height=15, wrap=tk.WORD)
output_text.pack(padx=10, pady=5)

root.mainloop()
