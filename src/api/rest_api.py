from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional

from ..document_store import HarryPotterDocumentStore
from ..pipeline import HarryPotterQAPipeline

app = FastAPI(title="Harry Potter Magic Recipe API")

# Pydantic models for request/response
class Recipe(BaseModel):
    id: str
    content: str
    meta: dict

class RecipeQuery(BaseModel):
    query: str
    top_k: int = 5

class RecipeGeneration(BaseModel):
    ingredients: List[str]
    effect: str

class RecipeModification(BaseModel):
    original_recipe: str
    new_effect: str

class IngredientSubstitution(BaseModel):
    recipe_name: str
    ingredient: str

# Dependency to get the QA pipeline
def get_qa_pipeline():
    document_store = HarryPotterDocumentStore()  # You might want to use a singleton pattern here
    return HarryPotterQAPipeline(document_store)

@app.post("/answer_question")
async def answer_question(question: str, pipeline: HarryPotterQAPipeline = Depends(get_qa_pipeline)):
    answer = pipeline.answer_question(question)
    return {"question": question, "answer": answer}

@app.post("/generate_recipe")
async def generate_recipe(recipe_gen: RecipeGeneration, pipeline: HarryPotterQAPipeline = Depends(get_qa_pipeline)):
    recipe = pipeline.generate_recipe(recipe_gen.ingredients, recipe_gen.effect)
    return {"recipe": recipe}

@app.post("/modify_recipe")
async def modify_recipe(recipe_mod: RecipeModification, pipeline: HarryPotterQAPipeline = Depends(get_qa_pipeline)):
    modified_recipe = pipeline.modify_recipe(recipe_mod.original_recipe, recipe_mod.new_effect)
    return {"modified_recipe": modified_recipe}

@app.post("/suggest_ingredient_substitution")
async def suggest_ingredient_substitution(substitution: IngredientSubstitution, pipeline: HarryPotterQAPipeline = Depends(get_qa_pipeline)):
    suggestion = pipeline.suggest_ingredient_substitution(substitution.recipe_name, substitution.ingredient)
    return {"suggestion": suggestion}

@app.post("/search_recipes")
async def search_recipes(query: RecipeQuery, pipeline: HarryPotterQAPipeline = Depends(get_qa_pipeline)):
    results = pipeline.search_recipes(query.query, query.top_k)
    return {"results": results}

@app.get("/recipe/{recipe_id}")
async def get_recipe(recipe_id: str, pipeline: HarryPotterQAPipeline = Depends(get_qa_pipeline)):
    recipe = pipeline.get_recipe_by_id(recipe_id)
    if recipe:
        return Recipe(id=recipe_id, content=recipe["content"], meta=recipe["meta"])
    raise HTTPException(status_code=404, detail="Recipe not found")

@app.post("/add_recipe")
async def add_recipe(recipe: Recipe, pipeline: HarryPotterQAPipeline = Depends(get_qa_pipeline)):
    pipeline.document_store.add_recipes([{
        "content": recipe.content,
        "meta": recipe.meta
    }])
    return {"message": "Recipe added successfully"}

@app.put("/update_recipe/{recipe_id}")
async def update_recipe(recipe_id: str, recipe: Recipe, pipeline: HarryPotterQAPipeline = Depends(get_qa_pipeline)):
    existing_recipe = pipeline.get_recipe_by_id(recipe_id)
    if not existing_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    pipeline.document_store.update_recipe(recipe_id, {
        "content": recipe.content,
        "meta": recipe.meta
    })
    return {"message": "Recipe updated successfully"}

@app.delete("/delete_recipe/{recipe_id}")
async def delete_recipe(recipe_id: str, pipeline: HarryPotterQAPipeline = Depends(get_qa_pipeline)):
    existing_recipe = pipeline.get_recipe_by_id(recipe_id)
    if not existing_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    pipeline.document_store.delete_recipe(recipe_id)
    return {"message": "Recipe deleted successfully"}