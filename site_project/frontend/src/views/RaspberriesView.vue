<template>
  <div class="min-h-screen  flex p-24 items-center justify-around">
    <div
      class="h-max w-max bg-white rounded-3xl shadow-2xl transition transform duration-500 ease-in-out hover:scale-105 p-8 text-gray-800">

      <h2 class="text-3xl font-bold">Choose Raspberry Pi</h2>

      <div class="h-max flex flex-col items-center">
        <RaspberrySelector @selected="selectedRaspberry = $event"
          class="w-full bg-indigo-100 border border-indigo-300 p-3 m-3 rounded-lg " />
        <div v-if="selectedRaspberry" class="p-3 bg-indigo-50 rounded-xl ">
          <h3 class="text-2xl font-semibold mb-4">Dados do Raspberry Pi</h3>
          <ul class="list-disc pl-4 list-inside text-lg text-gray-800 space-y-1">
            <li class="text-lg"><strong>ID:</strong> {{ selectedRaspberry.id }}</li>
            <li class="text-lg"><strong>MAC:</strong> {{ selectedRaspberry.mac }}</li>
            <li class="text-lg"><strong>Ultimo Registo:</strong> {{ selectedRaspberry.ultimo_registro }}</li>
          </ul>
        </div>
      </div>
    </div>
    <!-- Graphics -->
    <div v-if="selectedRaspberry" class="grid grid-cols-2 gap-6 mt-8">
      <iframe class="rounded-lg shadow-lg"
        :src="`http://192.92.147.85:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=1746156683173&to=1746199883173&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=1&__feature.dashboardSceneSolo`"
        width="450" height="200" />
      <iframe class="rounded-lg shadow-lg"
        :src="`http://192.92.147.85:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=1746156683173&to=1746199883173&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=4&__feature.dashboardSceneSolo`"
        width="450" height="200" frameborder="0" />
      <iframe class="rounded-lg shadow-lg"
        :src="`http://192.92.147.85:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=1746156683173&to=1746199883173&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=3&__feature.dashboardSceneSolo`"
        width="450" height="200" frameborder="0" />
      <iframe class="rounded-lg shadow-lg"
        :src="`http://192.92.147.85:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=1746156683173&to=1746199883173&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=2&__feature.dashboardSceneSolo`"
        width="450" height="200" frameborder="0" />
    </div>
  </div>
</template>


<script setup>
import { ref } from 'vue';
import RaspberrySelector from '@/components/RaspberrySelector.vue';

const selectedRaspberry = ref('');

</script>
