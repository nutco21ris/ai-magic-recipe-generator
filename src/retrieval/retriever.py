from haystack.nodes import BM25Retriever
from haystack.schema import Document
from typing import List, Optional

class HarryPotterRetriever(BM25Retriever):
    def __init__(self, document_store):
        super().__init__(document_store)

    def retrieve(self, query: str, filters: Optional[dict] = None, top_k: int = 10) -> List[Document]:
        retrieved_docs = super().retrieve(query, filters=filters, top_k=top_k)
        

        processed_docs = []
        for doc in retrieved_docs:
            if 'magic_effect' in doc.meta:
                processed_docs.append(doc)
            
        return processed_docs

    def retrieve_by_effect(self, effect: str, top_k: int = 10) -> List[Document]:
        filters = {"magic_effect": effect}
        return self.retrieve("", filters=filters, top_k=top_k)