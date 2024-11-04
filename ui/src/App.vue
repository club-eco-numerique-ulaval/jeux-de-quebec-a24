<script setup>
import { ref } from "vue";
import BarCodeScanner from "./components/BarCodeScanner.vue";
import { computed } from "vue";
import RecipeList from "./components/RecipeList.vue";

const recipes = ref([]);
const n_ingredients = ref(0);

const displayScanner = computed(() => {
  return recipes.value.length === 0;
});

const handleUseIngredients = (ingredients) => {
  ingredients = ingredients.map(a => a.name)
  n_ingredients.value = ingredients.length;

  fetch(`http://127.0.0.1:5000/recipes?ingredients=${ingredients.toString()}`)
    .then((response) => {
      return response.json();
    })
    .then((body) => {
      console.log(body)

      const ui_recipes = [];

      for (const recipe of body.recipes) {
        ui_recipes.push({
          name: recipe.recipeInfo.title,
          url: recipe.recipeInfo.sourceUrl,
          n_used_ingredients: recipe.usedIngredientCount,
        });
      }

      recipes.value = ui_recipes;
    });
};
</script>

<template>
  <BarCodeScanner @use-ingredients="handleUseIngredients" v-if="displayScanner">
  </BarCodeScanner>
  <RecipeList :recipes="recipes" :n_ingredients="n_ingredients" v-if="!displayScanner"></RecipeList>
</template>
