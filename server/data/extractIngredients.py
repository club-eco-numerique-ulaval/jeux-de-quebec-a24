import pandas as pd


def getIngredientsnameByCupCode(ingredientsCodes):
    OFF_EXPORT_PATH = "D:\Projet_programmation\Projet_CEN\jeux-de-quebec-a24\server\openfoodfacts_export.csv"
    
    df = pd.read_csv(OFF_EXPORT_PATH, delimiter="\t", dtype={"code": str})
    ingredientsCodes = ingredientsCodes[0].split(",")
    
    ingredientsNames = []
    for code in range(len(ingredientsCodes)):
        
        res = df[df["code"] == ingredientsCodes[code]]
        
        productCode = res.code
        productNameEn = res.product_name_en
        genericNameEn = res.generic_name_en

        if not productNameEn.empty:
            ingredientsNames.append(productNameEn.values[0].replace(",", ""))

        elif not genericNameEn.empty:
            ingredientsNames.append(genericNameEn.values[0].replace(",", ""))
        
        else:
            ingredientsNames.append(f"unknown product name: {productCode.values[0]}")
    
    return ingredientsNames

