from haystack.nodes import HuggingFaceGenerator
from haystack.schema import Document
from typing import List, Optional, Union
from .prompt_templates import HarryPotterPromptTemplates

class HarryPotterRecipeGenerator(HuggingFaceGenerator):
    def __init__(self, model_name_or_path: str = "facebook/bart-large", **kwargs):
        super().__init__(model_name_or_path=model_name_or_path, **kwargs)
        self.templates = HarryPotterPromptTemplates()

    def generate(self, prompt: str, documents: List[Document], top_k: Optional[int] = None) -> List[Document]:
        generated = super().generate(prompt)
        
        results = []
        for gen in generated:
            doc = Document(
                content=gen["generated_text"],
                meta={
                    "prompt": prompt,
                    "generated": True,
                    "model": self.model.config.name_or_path
                }
            )
            results.append(doc)
        
        return results[:top_k] if top_k is not None else results

    def generate_recipe(self, ingredients: List[str], effect: str) -> Document:
        prompt = self.templates.RECIPE_GENERATION.substitute(
            ingredients=", ".join(ingredients),
            effect=effect
        )
        generated = self.generate(prompt, [])
        if generated:
            recipe = generated[0]
            recipe.meta["ingredients"] = ingredients
            recipe.meta["effect"] = effect
            return recipe
        return None

    def answer_question(self, question: str, documents: List[Document]) -> Document:
        context = "\n\n".join([doc.content for doc in documents])
        prompt = self.templates.QUESTION_ANSWERING.substitute(
            question=question,
            context=context
        )
        generated = self.generate(prompt, [])
        if generated:
            answer = generated[0]
            answer.meta["question"] = question
            return answer
        return None

    def modify_recipe(self, original_recipe: str, new_effect: str) -> Document:
        prompt = self.templates.RECIPE_MODIFICATION.substitute(
            original_recipe=original_recipe,
            new_effect=new_effect
        )
        generated = self.generate(prompt, [])
        if generated:
            modified_recipe = generated[0]
            modified_recipe.meta["original_recipe"] = original_recipe
            modified_recipe.meta["new_effect"] = new_effect
            return modified_recipe
        return None

    def suggest_ingredient_substitution(self, recipe_name: str, ingredient: str) -> Document:
        prompt = self.templates.INGREDIENT_SUBSTITUTION.substitute(
            recipe_name=recipe_name,
            ingredient=ingredient
        )
        generated = self.generate(prompt, [])
        if generated:
            substitution = generated[0]
            substitution.meta["recipe_name"] = recipe_name
            substitution.meta["original_ingredient"] = ingredient
            return substitution
        return None