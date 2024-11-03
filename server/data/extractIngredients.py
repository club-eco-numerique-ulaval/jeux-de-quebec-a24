import pandas as pd
import numpy as np


def getIngredientsnameByCupCode(ingredientsCodes, off_export: pd.DataFrame):
    ingredientsCodes = ingredientsCodes[0].split(",")

    ingredientDetails = []
    for code in range(len(ingredientsCodes)):
        res = off_export[off_export["code"] == ingredientsCodes[code]]

        productCode = res.code
        productNameEn = res.product_name_en
        genericNameEn = res.generic_name_en

        current_ingredient = {}

        if not genericNameEn.empty and isinstance(genericNameEn.values[0], str):
            print(genericNameEn)
            current_ingredient["name"] = genericNameEn.values[0].replace(",", "")
        elif not productNameEn.empty and isinstance(productNameEn.values[0], str):
            current_ingredient["name"] = productNameEn.values[0].replace(",", "")
        else:
            current_ingredient["name"] = (
                f"nom de produit inconnu: {productCode.values[0]}"
            )

        if (
            not res["off:nutriscore_grade"].empty
            and len(res["off:nutriscore_grade"].values[0]) == 1
        ):
            current_ingredient["nutriscore_grade"] = (
                res["off:nutriscore_grade"].values[0].upper()
            )
        else:
            current_ingredient["nutriscore_grade"] = "?"

        if (
            not res["off:ecoscore_grade"].empty
            and len(res["off:ecoscore_grade"].values[0]) == 1
        ):
            current_ingredient["ecoscore_grade"] = (
                res["off:ecoscore_grade"].values[0].upper()
            )
        else:
            current_ingredient["ecoscore_grade"] = "?"

        ingredientDetails.append(current_ingredient)

    return ingredientDetails
