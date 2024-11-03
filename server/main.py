from flask import Flask

from api.HealthResource import HealthResource
from api.RecipeResource import RecipeResource
import pandas as pd

OFF_EXPORT_PATH = "off_exports/combined_export.csv"

app = Flask(__name__)
    
off_export = pd.read_csv(OFF_EXPORT_PATH, delimiter="\t", dtype={"code": str})

health = HealthResource(app)
recipe = RecipeResource(app, off_export)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)