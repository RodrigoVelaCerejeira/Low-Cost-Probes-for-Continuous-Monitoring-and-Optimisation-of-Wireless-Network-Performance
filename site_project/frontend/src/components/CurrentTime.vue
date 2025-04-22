<script setup>
import { ref, onMounted } from 'vue';

const currentTime = ref(new Date().toLocaleString());

onMounted(() => {
  setInterval(() => {
    currentTime.value = new Date().toLocaleString();
  }, 1000);
});
</script>

<template>
  <div class="text-center">
    <p class="text-2xl font-bold text-gray-800 mb-1 font-roboto">Welcome</p>
    <div class="text-3xl text-white font-roboto bg-blue-600 bg-opacity-80 px-2 py-1 rounded-full inline-block">
      <p>{{ currentTime }}</p>
    </div>
  </div>
</template>