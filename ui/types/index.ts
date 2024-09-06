export interface Recipe {
  id: string;
  name: string;
  ingredients: string[];
  instructions: string[];
  magicalEffect: string;
  warnings: string;
}

export interface RecipeQuery {
  query: string;
  topK: number;
}

export interface RecipeGeneration {
  ingredients: string[];
  effect: string;
}

export interface RecipeModification {
  originalRecipe: string;
  newEffect: string;
}

export interface IngredientSubstitution {
  recipeName: string;
  ingredient: string;
}

export interface ApiResponse<T> {
  data: T;
  error?: string;
}