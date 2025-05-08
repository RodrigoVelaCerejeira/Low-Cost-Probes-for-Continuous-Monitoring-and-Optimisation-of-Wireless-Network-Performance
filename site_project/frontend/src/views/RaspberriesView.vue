<template>
  <div class="min-h-screen flex p-24 items-center justify-around">
    <div
      class="h-max w-max bg-white rounded-3xl shadow-2xl transition transform duration-500 ease-in-out hover:scale-105 p-8 text-gray-800">

      <h2 class="text-3xl font-bold mb-6">Raspberry Pi</h2>
      
      <div class="h-max flex flex-col items-center">
      <RaspberrySelector @selected="onRaspberrySelected"
      class="w-full bg-indigo-100 border border-indigo-300 p-3 m-3 rounded-lg" />


    </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import RaspberrySelector from '@/components/RaspberrySelector.vue';

const router = useRouter();

function onRaspberrySelected(selectedRaspberry) {
  if (selectedRaspberry && selectedRaspberry.id) {
    router.push({ name: 'raspberry-details', params: { id: selectedRaspberry.id } });
  }
}
</script>