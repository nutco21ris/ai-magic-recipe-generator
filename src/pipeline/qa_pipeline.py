from haystack import Pipeline
from haystack.nodes import PromptNode, PromptTemplate
from typing import List, Dict, Any

from ..document_store import HarryPotterDocumentStore
from ..retrieval import HarryPotterRetriever, HarryPotterRanker
from ..generation import HarryPotterRecipeGenerator, HarryPotterPromptTemplates

class HarryPotterQAPipeline:
    def __init__(self, document_store: HarryPotterDocumentStore):
        self.document_store = document_store
        self.retriever = HarryPotterRetriever(document_store=self.document_store)
        self.ranker = HarryPotterRanker()
        self.generator = HarryPotterRecipeGenerator()
        self.prompt_templates = HarryPotterPromptTemplates()

        self.pipe = self._build_pipeline()

    def _build_pipeline(self) -> Pipeline:
        return Pipeline()

    def run(self, query: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        if params is None:
            params = {}
        return self.pipe.run(query=query, params=params)

    def answer_question(self, question: str) -> str:
        retriever_results = self.retriever.retrieve(question)
        ranked_results = self.ranker.rank(question, retriever_results)
        answer = self.generator.answer_question(question, ranked_results[:3])  # Use top 3 results
        return answer.content if answer else "I'm sorry, I couldn't find an answer to that question."

    def generate_recipe(self, ingredients: List[str], effect: str) -> str:
        recipe = self.generator.generate_recipe(ingredients, effect)
        return recipe.content if recipe else "I'm sorry, I couldn't generate a recipe with those ingredients and effect."

    def modify_recipe(self, original_recipe: str, new_effect: str) -> str:
        modified_recipe = self.generator.modify_recipe(original_recipe, new_effect)
        return modified_recipe.content if modified_recipe else "I'm sorry, I couldn't modify the recipe to achieve the new effect."

    def suggest_ingredient_substitution(self, recipe_name: str, ingredient: str) -> str:
        substitution = self.generator.suggest_ingredient_substitution(recipe_name, ingredient)
        return substitution.content if substitution else "I'm sorry, I couldn't suggest a substitution for that ingredient."

    def search_recipes(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        retriever_results = self.retriever.retrieve(query, top_k=top_k)
        ranked_results = self.ranker.rank(query, retriever_results)
        return [{"content": doc.content, "score": doc.score} for doc in ranked_results]

    def get_recipe_by_id(self, recipe_id: str) -> Dict[str, Any]:
        recipe = self.document_store.get_recipe_by_id(recipe_id)
        return {"content": recipe.content, "meta": recipe.meta} if recipe else None