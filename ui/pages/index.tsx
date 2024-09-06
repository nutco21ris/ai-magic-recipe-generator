import { GetServerSideProps, NextPage } from 'next'
import { useState } from 'react'
import { Box, Typography, TextField, Button, Grid } from '@mui/material'
import Layout from '../components/Layout'
import { generateRecipe, searchRecipes } from '../lib/api'
import { Recipe, RecipeGeneration } from '../types'

interface HomeProps {
  initialRecipes: Recipe[]
}

const Home: NextPage<HomeProps> = ({ initialRecipes }) => {
  const [recipes, setRecipes] = useState<Recipe[]>(initialRecipes)
  const [ingredients, setIngredients] = useState<string>('')
  const [effect, setEffect] = useState<string>('')

  const handleGenerateRecipe = async () => {
    const recipeGen: RecipeGeneration = {
      ingredients: ingredients.split(',').map(i => i.trim()),
      effect: effect
    }
    const newRecipe = await generateRecipe(recipeGen)
    setRecipes([newRecipe, ...recipes])
  }

  const handleSearch = async () => {
    const searchResults = await searchRecipes({ query: effect, top_k: 5 })
    setRecipes(searchResults)
  }

  return (
    <Layout>
      <Box sx={{ my: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Harry Potter Magic Recipe Generator
        </Typography>
        <Grid container spacing={2} sx={{ mb: 4 }}>
          <Grid item xs={12} sm={6}>
            <TextField
              fullWidth
              label="Ingredients (comma-separated)"
              value={ingredients}
              onChange={(e) => setIngredients(e.target.value)}
            />
          </Grid>
          <Grid item xs={12} sm={6}>
            <TextField
              fullWidth
              label="Desired Effect"
              value={effect}
              onChange={(e) => setEffect(e.target.value)}
            />
          </Grid>
          <Grid item xs={6}>
            <Button variant="contained" onClick={handleGenerateRecipe}>
              Generate Recipe
            </Button>
          </Grid>
          <Grid item xs={6}>
            <Button variant="outlined" onClick={handleSearch}>
              Search Recipes
            </Button>
          </Grid>
        </Grid>
        {recipes.map((recipe, index) => (
          <Box key={index} sx={{ mb: 2, p: 2, border: '1px solid #ccc', borderRadius: 2 }}>
            <Typography variant="h6">{recipe.name}</Typography>
            <Typography variant="body1">{recipe.content}</Typography>
          </Box>
        ))}
      </Box>
    </Layout>
  )
}

export const getServerSideProps: GetServerSideProps<HomeProps> = async () => {
  const initialRecipes = await searchRecipes({ query: '', top_k: 5 })
  return { props: { initialRecipes } }
}

export default Home