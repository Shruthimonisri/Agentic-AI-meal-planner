# Agentic AI Meal Planner 🍽️🤖

**Agentic AI Meal Planner** is an intelligent, autonomous meal planning application powered by Python, Spoonacular's food API, and a user-friendly graphical interface (Tkinter). This project demonstrates a practical agentic AI system: it perceives user preferences, reasons about recipe data, and acts by generating customized meal plans and shopping lists—all with minimal input.

## Features

- **Personalized Meal Planning:**  
  Enter your dietary preferences and ingredients you want to avoid, and the bot finds recipe ideas tailored just for you.

- **Automated Shopping List:**  
  Instantly generates a consolidated shopping list from your meal plan’s ingredients.

- **Easy-to-Use GUI:**  
  Runs in a simple desktop window—no command line required!

- **Agentic Workflow:**  
  The meal planner senses (user input), reasons (queries and filters recipe data), and acts (outputs plan and list), all in a single click.

- **Extendable:**  
  Modular code structure makes it easy to add features, such as nutrition analysis or meal plan history.

## How It Works

1. **Input:**  
   Users specify dietary restrictions (e.g., vegetarian, vegan) and ingredients to avoid.

2. **Processing:**  
   The agent queries the Spoonacular API for recipes matching criteria, then fetches their full ingredient lists.

3. **Output:**  
   The agent displays today’s suggested meal plan and creates an aggregated, ready-to-use shopping list.

## Technologies

- **Python 3**
- **Tkinter** (built-in GUI)
- **Requests** (for API calls)
- **Spoonacular Food API** (external recipe/ingredient data)

## Getting Started

1. **Clone the repo and install requirements (`requests`).**
2. **Sign up for a free Spoonacular API key and add it to the script.**
3. **Run `python meal_planner_gui.py`.**
4. **Enter your preferences in the GUI and click “Generate Meal Plan”!**

## Why Agentic?

Unlike basic scripts, this project autonomously pursues a user-centered goal by:
- Accepting inputs and making decisions with minimal intervention.
- Acting on external data to solve a real-world need.
- Generating actionable, user-specific outputs.

**Perfect for beginners, hobbyists, and developers exploring practical agentic AI design in Python. Fork, customize, and enjoy healthy, hassle-free meal planning!**
