import { Recipe, RecipeQuery, RecipeGeneration, RecipeModification, IngredientSubstitution } from '../types'

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api'

async function fetchFromAPI<T>(endpoint: string, method: string = 'GET', body?: any): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    method,
    headers: {
      'Content-Type': 'application/json',
    },
    body: body ? JSON.stringify(body) : undefined,
  })

  if (!response.ok) {
    throw new Error(`API call failed: ${response.statusText}`)
  }

  return response.json()
}

export async function generateRecipe(recipeGen: RecipeGeneration): Promise<Recipe> {
  return fetchFromAPI<Recipe>('/generate_recipe', 'POST', recipeGen)
}

export async function modifyRecipe(recipeMod: RecipeModification): Promise<Recipe> {
  return fetchFromAPI<Recipe>('/modify_recipe', 'POST', recipeMod)
}

export async function suggestIngredientSubstitution(substitution: IngredientSubstitution): Promise<string> {
  const response = await fetchFromAPI<{ suggestion: string }>('/suggest_ingredient_substitution', 'POST', substitution)
  return response.suggestion
}

export async function searchRecipes(query: RecipeQuery): Promise<Recipe[]> {
  const response = await fetchFromAPI<{ results: Recipe[] }>('/search_recipes', 'POST', query)
  return response.results
}

export async function getRecipe(recipeId: string): Promise<Recipe> {
  return fetchFromAPI<Recipe>(`/recipe/${recipeId}`)
}

export async function addRecipe(recipe: Recipe): Promise<void> {
  await fetchFromAPI<void>('/add_recipe', 'POST', recipe)
}

export async function updateRecipe(recipeId: string, recipe: Recipe): Promise<void> {
  await fetchFromAPI<void>(`/update_recipe/${recipeId}`, 'PUT', recipe)
}

export async function deleteRecipe(recipeId: string): Promise<void> {
  await fetchFromAPI<void>(`/delete_recipe/${recipeId}`, 'DELETE')
}