<template>
  <div
    class="min-h-screen bg-gradient-to-b from-[#17072b] via-[#2c0e44] to-[#3a0d5b] flex items-center justify-start p-8">
    <div
      class="bg-white rounded-3xl shadow-2xl transition transform duration-500 ease-in-out hover:scale-105 p-8 w-full max-w-3xl text-gray-800">

      <h2 class="text-3xl font-bold text-center mb-6">Choose Raspberry Pi</h2>

      <RaspberrySelector @selected="selectedRaspberry = $event"
        class="block w-full bg-indigo-100 border border-indigo-300 p-3 rounded-lg focus:outline-none focus:ring-4 focus:ring-indigo-400 text-lg mb-6 transition-all" />

      <div v-if="selectedRaspberry" class="mt-6 p-6 bg-indigo-50 rounded-xl shadow-inner">
        <ul class="list-disc list-inside text-lg text-gray-800">
          <h3 class="text-2xl font-semibold mb-4 text-indigo-700">Dados do Raspberry Pi</h3>
          <li class="text-lg"><strong>ID:</strong> {{ selectedRaspberry.id }}</li>
          <li class="text-lg"><strong>MAC:</strong> {{ selectedRaspberry.mac }}</li>
          <li class="text-lg"><strong>Ultimo Registo:</strong> {{ selectedRaspberry.ultimo_registro }}</li>
        </ul>
      </div>
    </div>
    <!-- Graphics -->
    <div v-if="selectedRaspberry" class="mt-8 grid grid-cols-2 gap-6">
    <div class="mt-8 grid grid-cols-2 gap-6">
      <iframe src="http://192.92.147.85:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=1746156683173&to=1746199883173&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=1&__feature.dashboardSceneSolo" width="450" height="200" frameborder="0"></iframe>
      <iframe src="http://localhost:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=1746156683173&to=1746199883173&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=4&__feature.dashboardSceneSolo" width="450" height="200" frameborder="0"></iframe>
      <iframe src="http://localhost:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=1746156683173&to=1746199883173&timezone=browser&var-raspberry={selectedRaspberry.id}&panelId=3&__feature.dashboardSceneSolo" width="450" height="200" frameborder="0"></iframe>
      <iframe src="http://localhost:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=1746156683173&to=1746199883173&timezone=browser&var-raspberry={selectedRaspberry.id}&panelId=2&__feature.dashboardSceneSolo" width="450" height="200" frameborder="0"></iframe>
    </div>

    </div>
  </div>
</template>


<script setup>
import { ref } from 'vue';
import RaspberrySelector from '@/components/RaspberrySelector.vue';

const selectedRaspberry = ref('');

</script>
