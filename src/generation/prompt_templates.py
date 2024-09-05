from string import Template

class HarryPotterPromptTemplates:
    RECIPE_GENERATION = Template("""
Generate a Harry Potter magic recipe with the following details:

Ingredients: $ingredients

Desired Effect: $effect

Please provide the recipe in the following format:
Recipe Name: [A creative name for the potion or spell]
Ingredients: [List of ingredients, including quantities]
Instructions: [Step-by-step instructions for creating the potion or casting the spell]
Magical Effect: [Detailed description of the magical effect]
Warnings: [Any precautions or side effects to be aware of]

Be creative and ensure the recipe aligns with the Harry Potter universe.
""")

    QUESTION_ANSWERING = Template("""
You are an expert on Harry Potter potions and spells. Please answer the following question based on the provided context:

Question: $question

Context:
$context

Please provide a detailed and accurate answer, citing specific information from the context where possible. If the answer is not directly available in the context, use your knowledge of the Harry Potter universe to provide a plausible response.
""")

    RECIPE_MODIFICATION = Template("""
Modify the following Harry Potter magic recipe to achieve a different effect:

Original Recipe:
$original_recipe

Desired New Effect: $new_effect

Please provide the modified recipe in the following format:
Recipe Name: [A new creative name for the modified potion or spell]
Ingredients: [List of ingredients, including any new additions or removals]
Instructions: [Updated step-by-step instructions]
Magical Effect: [Detailed description of the new magical effect]
Warnings: [Any new precautions or side effects]

Ensure the modifications are creative yet consistent with the Harry Potter universe.
""")

    INGREDIENT_SUBSTITUTION = Template("""
Suggest a substitution for the following ingredient in a Harry Potter magic recipe:

Recipe: $recipe_name
Ingredient to Replace: $ingredient

Please provide the following:
1. Suggested Substitute: [Name of the substitute ingredient]
2. Reason for Substitution: [Explanation of why this substitute works]
3. Effect on Potion: [How the substitution might slightly alter the potion's effects]
4. Adjustment to Instructions: [Any changes needed in the brewing process]

Ensure the substitution is plausible within the Harry Potter universe and maintains the general effect of the original recipe.
""")