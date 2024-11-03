import requests
import os
from dotenv import load_dotenv

BASE_URL = "https://api.spoonacular.com/recipes/findByIngredients?"

def getRecipes(ingredients):
    load_dotenv()
    params = {"ingredients": ingredients}
    header = {"Content-Type": "application/json"}

    SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")
    NUMBER_OF_RECIPES = 10
    response = requests.get(f"{BASE_URL}apiKey={SPOONACULAR_API_KEY}&number={NUMBER_OF_RECIPES}", params=params, headers=header)

    recipes = {}
    if response.status_code == 200:
        recipes = response.json()

    else:
        print('Request failed with status code:', response.status_code)
    
    return recipes
