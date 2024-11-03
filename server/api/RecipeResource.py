from flask import Flask, jsonify, request
from data.extractIngredients import getIngredientsnameByCupCode
from data.extractRecipes import getRecipesInformations


class RecipeResource:
    
    def __init__(self, app: Flask) -> None:
        self.__app = app
        self.register_routes()

    def register_routes(self):
        self.__app.add_url_rule('/ingredients', view_func=self.getIngredientsNamesByIngredientsCupCode, methods=['GET'])
        self.__app.add_url_rule('/recipes', view_func=self.getRecipesByIngredientsNames, methods=['GET'])


    def getIngredientsNamesByIngredientsCupCode(self):
        args = request.args
        ingredientsCupCodes = args.getlist("ingredientsCodes")

        ingredientsNames = getIngredientsnameByCupCode(ingredientsCupCodes)

        return jsonify({"ingredients": ingredientsNames})
    

    def getRecipesByIngredientsNames(self):
        args = request.args
        ingredients = args.getlist("ingredients")

        recipes = getRecipesInformations(ingredients)

        return jsonify({"recipes": recipes})



            
