<script setup>
import { ref, onMounted } from 'vue';
import { defineEmits } from 'vue';
import axios from 'axios';

// Emitir evento para o componente pai
const emit = defineEmits(['selected']);

const raspberries = ref([]);
const selectedRaspberry = ref(null);
const raspberryData = ref(null);

// Buscar lista de Raspberry Pis
const fetchRaspberryPis = async () => {
  try {
    const response = await axios.get('http://192.92.147.85:3001/raspberry/devices');
    raspberries.value = response.data;
  } catch (error) {
    console.error('Error finding Raspberry Pis:', error);
  }
};

// Buscar os dados do Raspberry Pi selecionado
const fetchRaspberryData = async () => {
  if (selectedRaspberry.value) {
    try {
      const response = await axios.get(`http://192.92.147.85:3001/raspberry/${selectedRaspberry.value}`);
      raspberryData.value = response.data;
      emit('selected', raspberryData.value);
    } catch (error) {
      console.error('Error getting data from Raspberry Pi:', error);
    }
  }
};

onMounted(fetchRaspberryPis);
</script>

<template>
  <div class="p-4">
    <h2 class="text-lg font-bold mb-2">Choose Raspberry Pi</h2>

    <select v-model="selectedRaspberry" @change="fetchRaspberryData"
      class="w-full max-w-md border border-gray-300 p-2 rounded focus:outline-none focus:ring-2 focus:ring-blue-500">
      <option value="" disabled>Select a Raspberry Pi</option>
      <option v-for="rpi in raspberries" :key="rpi.id" :value="rpi.id">
        {{ rpi.mac }}
      </option>
    </select>

  </div>
</template>
