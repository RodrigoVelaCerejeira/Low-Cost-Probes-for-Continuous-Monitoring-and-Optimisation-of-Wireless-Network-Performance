<!-- src/components/CurrentTime.vue -->
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
  <div class="time-container">
    <p class="welcome-message">Welcome</p>
    <div class="time">
      <p>{{ currentTime }}</p>
    </div>
  </div>
</template>

<style scoped>
.time-container {
  text-align: center;
}

.welcome-message {
  font-size: 25px;
  font-weight: bold;
  color: #333;
  margin-bottom: 5px;
  font-family: 'Roboto', sans-serif;
}

.time {
  font-size: 30px;
  color: #FFFFFF;
  font-family: 'Roboto', sans-serif;
  background: rgba(36, 60, 230, 0.8);
  padding: 3px;
  border-radius: 25px;
  display: inline-block;
}
</style>