# Harry Potter Magic Recipe Generator: Comprehensive Data Collection Guide

## 1. Original Data Collection

### 1.1 Data Sources
- Harry Potter book series and official supplementary materials
- Fan-created magic recipes (mind copyright issues)
- Magical elements from other fantasy literature (for inspiration)

### 1.2 Data Structure
Each original entry should include the following fields:
- Magical Effect
- Recipe Name
- List of Ingredients
- Preparation Steps
- Additional Notes (optional)

### 1.3 Data Collection Template
```
Magical Effect: [Describe the magical effect]
Recipe Name: [Creative name]
Ingredients:
- [Ingredient 1]
- [Ingredient 2]
- ...
Steps:
1. [Step 1]
2. [Step 2]
...
Additional Notes: [Any extra information]
```

### 1.4 Data Collection Methods
1. Manual extraction: Carefully read the original books, noting all relevant magic recipes and potions.
2. Web scraping: Collect data from reliable Harry Potter fan websites (ensure compliance with website policies).
3. Crowdsourcing: Invite Harry Potter fans to submit their created magic recipes.

### 1.5 Data Quantity Goals
- Minimum: 500-1000 unique recipes
- Ideal: 2000-5000 unique recipes
- If possible: 10,000+ recipes for optimal results

## 2. Data Cleaning and Standardization

### 2.1 Cleaning Steps
1. Remove duplicate entries
2. Check and correct spelling errors
3. Ensure all necessary fields are filled for each entry
4. Standardize descriptions of magical effects (e.g., use consistent terminology)

### 2.2 Standardized Format
Ensure all entries follow a consistent format:
- Ingredients should use uniform units of measurement
- Steps should be concise and clearly numbered
- Magical effects should be clear and specific

## 3. Conversion to BART Model Format

### 3.1 BART Input-Output Format
Each converted entry should follow this format:

Input: Create a magic recipe for [magical effect].
Output: [Recipe Name] | Ingredients: [List of ingredients] | Steps: [Numbered steps] | Notes: [Additional notes]

### 3.2 Conversion Steps
1. Transform the magical effect into an input prompt
2. Combine other information into a continuous output string
3. Use the "|" symbol to separate different parts in the output

### 3.3 Conversion Example
Original Data:
```
Magical Effect: Invisibility
Recipe Name: Phantom Fizz Elixir
Ingredients:
- 3 drops of chameleon blood
- 1 pinch of powdered Demiguise hair
- 2 moonstone shavings
- 1 sprig of ghostly mint
- 500ml carbonated water from a hidden spring
Steps:
1. In a silver cauldron, mix chameleon blood and Demiguise hair under a new moon.
2. Slowly stir in moonstone shavings, rotating wand counterclockwise 7 times.
3. Add ghostly mint and let simmer for 3 minutes.
4. Remove from heat and add carbonated water, causing a misty fizz.
5. Bottle immediately in clear glass vials.
Additional Notes: Effects last for 30 minutes per dose. Tastes like minty clouds.
```

Converted BART Format:
```
Input: Create a magic recipe for invisibility.
Output: Phantom Fizz Elixir | Ingredients: 3 drops of chameleon blood, 1 pinch of powdered Demiguise hair, 2 moonstone shavings, 1 sprig of ghostly mint, 500ml carbonated water from a hidden spring | Steps: 1. In a silver cauldron, mix chameleon blood and Demiguise hair under a new moon. 2. Slowly stir in moonstone shavings, rotating wand counterclockwise 7 times. 3. Add ghostly mint and let simmer for 3 minutes. 4. Remove from heat and add carbonated water, causing a misty fizz. 5. Bottle immediately in clear glass vials. | Notes: Effects last for 30 minutes per dose. Tastes like minty clouds.
```

## 4. Data Validation and Quality Control

### 4.1 Validation Steps
1. Randomly check 10% of converted data to ensure correct formatting
2. Check for logical consistency between magical effects, ingredients, and steps
3. Ensure no critical information is missing

### 4.2 Diversity Check
1. Ensure diversity in magical effects
2. Check for variety in ingredients, avoiding excessive repetition
3. Ensure variation in preparation steps

## 5. Data Storage and Management

### 5.1 Storage Format
- Use CSV or JSON format to store final data
- Include both original data and converted BART format data

### 5.2 File Structure Example (CSV)
```
original_effect,original_name,original_ingredients,original_steps,original_notes,bart_input,bart_output
Invisibility,Phantom Fizz Elixir,"3 drops of chameleon blood, 1 pinch of powdered Demiguise hair, ...",1. In a silver cauldron...,Effects last for 30 minutes...,Create a magic recipe for invisibility.,Phantom Fizz Elixir | Ingredients: 3 drops of chameleon blood...
```

### 5.3 Data Backup
- Regularly backup the dataset
- Use a version control system (like Git) to track data changes

## 6. Final Checklist
- [ ] Reached target data quantity
- [ ] All data cleaned and standardized
- [ ] Successfully converted to BART format
- [ ] Completed data validation and quality control
- [ ] Data safely stored and backed up
