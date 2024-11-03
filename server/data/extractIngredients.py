import pandas as pd


def getIngredientsnameByCupCode(ingredientsCodes, off_export: pd.DataFrame):
    ingredientsCodes = ingredientsCodes[0].split(",")
    
    ingredientsNames = []
    for code in range(len(ingredientsCodes)):
        
        res = off_export[off_export["code"] == ingredientsCodes[code]]
        
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

