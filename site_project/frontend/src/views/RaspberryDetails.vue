<template>
  <div class="min-h-screen flex flex-col p-36 items-center justify-around">
    <div class="flex gap-8 w-full">

      <div
        class="h-max w-1/3 bg-white rounded-3xl shadow-2xl transition transform duration-500 ease-in-out hover:scale-105 p-8 text-gray-800">
        <h2 class="text-3xl font-bold">Raspberry Pi</h2>

        <div class="h-max flex flex-col items-center">
          <RaspberrySelector v-model:selected="selectedRaspberry" @selected="onRaspberrySelected"
            class="w-full bg-indigo-100 border border-indigo-300 p-3 m-3 rounded-lg" />

          <div v-if="selectedRaspberry" class="p-3 bg-indigo-50 rounded-xl">
            <h3 class="text-2xl font-semibold mb-4">Raspberry Pi Data</h3>
            <ul class="list-disc pl-4 list-inside text-lg text-gray-800 space-y-1">
              <li class="text-lg"><strong>ID:</strong> {{ selectedRaspberry.id }}</li>
              <li class="text-lg"><strong>MAC:</strong> {{ selectedRaspberry.mac }}</li>
              <li class="text-lg"><strong>Last Record:</strong> {{ selectedRaspberry.last_record }}</li>
            </ul>
          </div>
        </div>
      </div>

      <div
        class="h-max w-full bg-white text-gray-800 rounded-3xl shadow-xl transition transform duration-500 ease-in-out hover:scale-105 p-8 overflow-y-scroll mx-4">
        <h2 class="text-2xl font-semibold mb-4">APs</h2>
      </div>
    </div>

    <!-- Gráficos -->
    <div v-if="selectedRaspberry" class="grid grid-cols-1 gap-6 mt-8 w-full">
      <iframe class="rounded-lg shadow-lg"
        :src="`http://192.92.147.85:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=1746156683173&to=1746199883173&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=1&__feature.dashboardSceneSolo`"
        width="100%" height="400"></iframe>
      <iframe class="rounded-lg shadow-lg"
        :src="`http://192.92.147.85:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=1746156683173&to=1746199883173&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=4&__feature.dashboardSceneSolo`"
        width="100%" height="400"></iframe>
      <iframe class="rounded-lg shadow-lg"
        :src="`http://192.92.147.85:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=1746156683173&to=1746199883173&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=3&__feature.dashboardSceneSolo`"
        width="100%" height="400"></iframe>
      <iframe class="rounded-lg shadow-lg"
        :src="`http://192.92.147.85:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=1746156683173&to=1746199883173&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=2&__feature.dashboardSceneSolo`"
        width="100%" height="400"></iframe>
      <iframe class="rounded-lg shadow-lg"
        :src="`http://192.92.147.85:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=1746138776000&to=1746191135000&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=5&__feature.dashboardSceneSolo`"
        width="100%" height="400"></iframe>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRoute } from 'vue-router';
import { useRouter } from 'vue-router';
import RaspberrySelector from '@/components/RaspberrySelector.vue';

const selectedRaspberry = ref(null);

const route = useRoute();
const router = useRouter();
const initialId = route.params.id;

async function fetchRaspberryDetails(id) {
  const data = [
    { id: 1, mac: '00:1B:44:11:3A:B7', last_record: '2023-05-01 12:00' },
    { id: 2, mac: '00:1B:44:11:3A:B8', last_record: '2023-05-01 13:00' },
    { id: 3, mac: '00:1B:44:11:3A:B9', last_record: '2023-05-01 14:00' },
  ];
  return data.find((rpi) => rpi.id === parseInt(id));
}

async function onRaspberrySelected(raspberry) {
  selectedRaspberry.value = await fetchRaspberryDetails(raspberry.id);
  if (raspberry && raspberry.id) {
    router.push({ name: 'raspberry-details', params: { id: raspberry.id } });
  }
}

onRaspberrySelected({ id: initialId });
</script>