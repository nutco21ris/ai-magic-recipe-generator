from haystack.nodes import SentenceTransformersRanker
from haystack.schema import Document
from typing import List

class HarryPotterRanker(SentenceTransformersRanker):
    def __init__(self, model_name_or_path: str = "all-MiniLM-L6-v2", top_k: int = 10):
        super().__init__(model_name_or_path=model_name_or_path, top_k=top_k)

    def rank(self, query: str, documents: List[Document], top_k: Optional[int] = None) -> List[Document]:
        ranked_docs = super().rank(query, documents, top_k=top_k)
        

        for doc in ranked_docs:
            if 'magic_effect' in doc.meta:
                if doc.meta['magic_effect'].lower() in query.lower():
                    doc.score += 0.1 

        ranked_docs = sorted(ranked_docs, key=lambda x: x.score, reverse=True)
        
        return ranked_docs[:top_k] if top_k else ranked_docs