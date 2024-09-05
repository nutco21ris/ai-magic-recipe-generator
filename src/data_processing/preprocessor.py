from haystack.nodes import PreProcessor
import re

class HarryPotterRecipePreProcessor(PreProcessor):
    def process(self, document):
        text = document.content
        
        text = re.sub(r'\s+', ' ', text).strip()
        
        recipe_name, content = text.split("|", 1)
        
        document.content = content.strip()
        
        document.meta["recipe_name"] = recipe_name.strip()
        
        magic_effect = re.search(r'(?<=,)[^,]+(?=,)', document.meta["recipe_name"])
        if magic_effect:
            document.meta["magic_effect"] = magic_effect.group().strip()
        
        return document