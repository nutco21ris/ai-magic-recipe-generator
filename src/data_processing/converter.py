from haystack.nodes import FileConverter
import pandas as pd

class HarryPotterRecipeConverter(FileConverter):
    def convert(self, file_path: str, meta: None):
        df = pd.read_csv(file_path)
        
        documents = []
        for _, row in df.iterrows():
            content = f"Recipe: {row['Output']}\nIngredients: {row['Ingredients']}\nSteps: {row['Steps']}\nNotes: {row['Notes']}"
            document = {
                "content": content,
                "meta": {
                    "recipe_id": row["Input"],
                    "recipe_name": row["Output"].split("|")[0].strip()
                }
            }
            documents.append(document)
        
        return documents