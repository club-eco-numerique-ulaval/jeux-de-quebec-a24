<script setup>
defineProps({
  recipes: Array,
  n_ingredients: Number
});
</script>

<template>
  <h1 style="font-size: 7em;">Recettes:</h1>

  <ul>
    <li style="font-size: xx-large" v-for="recipe in recipes">
      <a :href=recipe.url target="_blank" rel="noopener noreferrer">{{ recipe.name }} <br> ({{ recipe.n_used_ingredients }}/{{ n_ingredients }} ingrédients)</a>
    </li>    
  </ul>
  <br>
  <div style="font-size: large;">
    <br>Recherche de recettes par Spoonacular: <br> <a href="https://spoonacular.com/food-api/">https://spoonacular.com/food-api/</a></div>
</template>
