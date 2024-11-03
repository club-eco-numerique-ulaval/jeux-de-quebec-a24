<script setup>
import { ref } from "vue";
import { StreamBarcodeReader } from "vue-barcode-reader";

const emit = defineEmits(["use-ingredients"]);

const bar_codes = ref([]);
const ingredients = ref([]);

const onLoaded = () => {
  console.log("loaded");
};

const onDecode = (code) => {
  if (!bar_codes.value.includes(code)) {
    fetch(`http://127.0.0.1:5000/ingredients?ingredientsCodes=${code}`)
      .then((response) => {
        return response.json();
      })
      .then((body) => {
        ingredients.value.push(body.ingredients[0]);
        bar_codes.value.push(code);
      });
  }
};

const sendIngredients = () => {
  console.log("emitting");
  emit("use-ingredients", ingredients.value);
  console.log("emitted");
};

const eraseIngredients = () => {
  bar_codes.value = [];
  ingredients.value = [];
};
</script>

<template>
  <StreamBarcodeReader
    @decode="onDecode"
    @loaded="onLoaded"
  ></StreamBarcodeReader>
  <ul>
    <li style="font-size: x-large" v-for="ingredient in ingredients">
      {{ ingredient.name }} (Nutri-score: {{ ingredient.nutriscore_grade }}, Éco-score: {{  ingredient.ecoscore_grade }})
    </li>
  </ul>

  <div></div>
  <div style="align-content: center; font-size: large;">Les associations entre les codes barres et les noms d'ingrédients, ainsi que les éco-scores et nutri-scores, proviennent
  de la base de données Open Food Facts, qui est rendue disponible sous la licence Open
  Database License (ODbL) à <a href="https://fr-ca.openfoodfacts.org">https://fr-ca.openfoodfacts.org</a> </div>

  <button
    style="background-color: green; font-size: x-large"
    @click="sendIngredients"
  >
    Chercher des recettes
  </button>
  <button
    style="background-color: red; font-size: x-large"
    @click="eraseIngredients"
  >
    Effacer
  </button>
</template>
