from haystack.document_stores import ElasticsearchDocumentStore
from haystack.schema import Document
from typing import List, Optional, Union

class HarryPotterDocumentStore(ElasticsearchDocumentStore):
    def __init__(self, host: str = "localhost", port: int = 9200, index: str = "harry_potter_recipes"):
        super().__init__(host=host, port=port, index=index)

    def add_recipes(self, recipes: List[Union[dict, Document]]):
        documents = []
        for recipe in recipes:
            if isinstance(recipe, dict):
                doc = Document(
                    content=recipe['content'],
                    meta={
                        "recipe_id": recipe['meta']['recipe_id'],
                        "recipe_name": recipe['meta']['recipe_name'],
                        "magic_effect": recipe['meta'].get('magic_effect', '')
                    }
                )
            else:
                doc = recipe
            documents.append(doc)
        
        self.write_documents(documents)

    def search_recipes(self, query: str, filters: Optional[dict] = None, top_k: int = 10):
        return self.query(query, filters=filters, top_k=top_k)

    def get_recipe_by_id(self, recipe_id: str):
        return self.get_document_by_id(recipe_id)

    def update_recipe(self, recipe_id: str, updates: dict):
        self.update_document_meta(recipe_id, updates)

    def delete_recipe(self, recipe_id: str):
        self.delete_documents([recipe_id])