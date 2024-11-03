from flask import Flask, jsonify, request
from data.extractIngredients import getIngredientsnameByCupCode
from data.extractRecipes import getRecipes
import pandas as pd


class RecipeResource:
    
    CORS_HEADER = "Access-Control-Allow-Origin"
    CORS_EXPRESSION = "*"

    def __init__(self, app: Flask, off_export: pd.DataFrame) -> None:
        self.__app = app
        self.off_export = off_export
        self.register_routes()

    def register_routes(self):
        self.__app.add_url_rule('/ingredients', view_func=self.getIngredientsNamesByIngredientsCupCode, methods=['GET'])
        self.__app.add_url_rule('/recipes', view_func=self.getRecipesByIngredientsNames, methods=['GET'])


    def getIngredientsNamesByIngredientsCupCode(self):
        args = request.args
        ingredientsCupCodes = args.getlist("ingredientsCodes")

        ingredientsNames = getIngredientsnameByCupCode(ingredientsCupCodes, self.off_export)

        response = jsonify({"ingredients": ingredientsNames})
        response.headers.add(self.CORS_HEADER, self.CORS_EXPRESSION)
        return response
    

    def getRecipesByIngredientsNames(self):
        args = request.args
        ingredients = args.getlist("ingredients")

        recipes = getRecipes(ingredients)

        response = jsonify({"recipes": recipes})
        response.headers.add(self.CORS_HEADER, self.CORS_EXPRESSION)
        return response



            
