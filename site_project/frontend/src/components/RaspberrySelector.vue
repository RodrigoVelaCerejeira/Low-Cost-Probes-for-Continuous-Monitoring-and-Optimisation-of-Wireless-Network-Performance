<script setup>
import { ref, onMounted } from 'vue';
import { defineEmits } from 'vue';
import { fetchRaspberryPis } from '@/services/raspberryService'; '@/services/raspberryService'

// Emitir evento para o componente pai
const emit = defineEmits(['selected']);

const raspberries = ref([]);
const selectedRaspberry = ref(null);

function handleChange(selectedRaspberry) {
  console.log('Selected value:', selectedRaspberry);
  emit('selected', selectedRaspberry);
}

onMounted(async () => raspberries.value = await fetchRaspberryPis())
</script>

<template>
  <div class="p-4">
    <h2 class="text-lg font-bold mb-2">Choose Raspberry Pi</h2>

    <select v-model="selectedRaspberry" @change="handleChange(selectedRaspberry)"
      class="w-full max-w-md border border-gray-300 p-2 rounded focus:outline-none focus:ring-2 focus:ring-blue-500">
      <option value="" disabled>Select a Raspberry Pi</option>
      <option v-for="rpi in raspberries" :key="rpi.id" :value="rpi">
        {{ rpi.mac }}
      </option>
    </select>

  </div>
</template>
