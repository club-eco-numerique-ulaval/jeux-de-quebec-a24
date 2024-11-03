import requests
import os
from dotenv import load_dotenv

BASE_URL = "https://api.spoonacular.com/recipes/"

load_dotenv()
SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")

def getRecipesInformations(ingredients):
    params = {"ingredients": ingredients}
    header = {"Content-Type": "application/json"}

    NUMBER_OF_RECIPES = "2"
    response = requests.get(f"{BASE_URL}findByIngredients?apiKey={SPOONACULAR_API_KEY}&number={NUMBER_OF_RECIPES}", params=params, headers=header)

    recipesInfo = []
    if response.status_code == 200:
        recipesResponse = response.json()
        
        for i in range(len(recipesResponse)):
            recipe = {}
            recipe["id"] = recipesResponse[i]["id"]
            recipe["usedIngredientCount"] = recipesResponse[i]["usedIngredientCount"]

            recipeId = recipesResponse[i]["id"]
            responseRecipesInfo = requests.get(f"{BASE_URL}{recipeId}/information?apiKey={SPOONACULAR_API_KEY}", headers=header)

            recipe["recipeInfo"] = responseRecipesInfo.json()

            recipesInfo.append(recipe)

        return recipesInfo

    else:
        print('Request failed with status code:', response.status_code)


# def getRecipesInformations(recipes):
#     header = {"Content-Type": "application/json"}

#     recipesInfoResults = []
#     for recipe in recipes:
#         recipeInfo = {}
#         recipeId = recipe["id"]
#         usedIngredientCount = recipe["usedIngredientCount"]

#         responseRecipesInfo = requests.get(f"{BASE_URL}{recipeId}/information?apiKey={SPOONACULAR_API_KEY}", headers=header)

#         if responseRecipesInfo.status_code == 200:
#             recipeInfo = recipeId
#             recipeInfo = usedIngredientCount
#             recipeInfo = responseRecipesInfo.json()

#             recipesInfoResults.append(recipeInfo)

#         else:
#             print('Request failed with status code:', responseRecipesInfo.status_code)
#             break
    
#     return recipesInfoResults
