<template>
  <div class="min-h-screen flex flex-col p-36 items-center justify-around">
    <div class="h-[400px] flex gap-8 w-full">

      <div
        class="flex-2 h-full w-1/3 bg-white rounded-3xl shadow-2xl transition transform duration-500 ease-in-out hover:scale-105 p-8 text-gray-800">
        <h2 class="text-3xl font-bold">Raspberry Pi</h2>

        <div class="h-max flex flex-col items-center">
          <RaspberrySelector v-model:selected="selectedRaspberry" @selected="onRaspberrySelected"
            class="w-full bg-indigo-100 border border-indigo-300 p-3 m-3 rounded-lg" />
        </div>

        <div v-if="selectedRaspberry" class="p-2 bg-indigo-50 rounded-xl">
          <h3 class="text-2xl font-semibold mb-4">Raspberry Pi Data</h3>
          <ul class="list-disc pl-4 list-inside text-lg text-gray-800 space-y-1">
            <li class="text-lg"><strong>ID:</strong> {{ selectedRaspberry.id }}</li>
            <li class="text-lg"><strong>MAC:</strong> {{ selectedRaspberry.mac }}</li>
            <li class="text-lg"><strong>Last Record:</strong> {{ selectedRaspberry.ultimo_registro }}</li>
          </ul>
        </div>
        <button @click="exportExcelById(selectedRaspberry.id)"
          class="mt-4 bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700 transition duration-300">Export Data</button>
      </div>

      <div
        class="overscroll-none flex-3 h-full w-full bg-white text-gray-800 rounded-3xl shadow-xl transition transform duration-500 ease-in-out hover:scale-105 overflow-x-hidden overflow-y-scroll mx-4">
        <h2 class="m-4 text-2xl font-semibold ">APs</h2>
        <table class="min-w-full divide-y divide-gray-700 bg-white rounded-xl shadow overflow-hidden">
          <thead class="bg-indigo-50 ext-gray-700 sticky top-0">
            <tr>
              <th class="px-6 py-3 text-left text-sm font-medium uppercase">ssid</th>
              <th class="px-6 py-3 text-left text-sm font-medium uppercase">raspberrypi_id</th>
              <th class="px-6 py-3 text-left text-sm font-medium uppercase">bssid</th>
              <th class="px-6 py-3 text-left text-sm font-medium uppercase">rate</th>
              <th class="px-6 py-3 text-left text-sm font-medium uppercase">signal</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-300 text-gray-800">
            <tr v-for="ap in raspberryAPs" :key="ap.ssid">
              <td class="px-6 py-4"> {{ ap.ssid }} </td>
              <td class="px-6 py-4"> {{ ap.raspberrypi_id }} </td>
              <td class="px-6 py-4"> {{ ap.bssid }} </td>
              <td class="px-6 py-4"> {{ ap.rate }} Mbits/s</td>
              <td class="px-6 py-4"> {{ ap.signal }} </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div v-if="selectedRaspberry" class="grid grid-cols-1 gap-6 mt-8 w-full">
      <iframe class="rounded-lg shadow-lg"
        :src="`http://192.92.147.85:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=1746156683173&to=1746199883173&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=1&__feature.dashboardSceneSolo`"
        width="100%" height="400"></iframe>
      <iframe class="rounded-lg shadow-lg"
        :src="`http://192.92.147.85:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=1746156683173&to=1746199883173&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=4&__feature.dashboardSceneSolo`"
        width="100%" height="400"></iframe>
      <iframe class="rounded-lg shadow-lg"
        :src="`http://192.92.147.85:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=1746138776000&to=1746191135000&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=5&__feature.dashboardSceneSolo`"
        width="100%" height="400"></iframe>
      <iframe class="rounded-lg shadow-lg"
        :src="`http://192.92.147.85:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=1746156683173&to=1746199883173&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=3&__feature.dashboardSceneSolo`"
        width="100%" height="400"></iframe>
      <iframe class="rounded-lg shadow-lg"
        :src="`http://192.92.147.85:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=1746156683173&to=1746199883173&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=2&__feature.dashboardSceneSolo`"
        width="100%" height="400"></iframe>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRoute } from 'vue-router';
import { useRouter } from 'vue-router';
import { fetchRaspberryById, fetchAPsById, fetchRaspberryDataById } from '@/services/raspberryService'; '@/services/raspberryService'
import RaspberrySelector from '@/components/RaspberrySelector.vue';

const selectedRaspberry = ref(null);
const raspberryAPs = ref([]);
const raspberryId = ref(null);

const route = useRoute();
const router = useRouter();
const initialId = route.params.id;

const exportExcelById = async (raspberryId) => {
  if (!raspberryId) {
    alert('Select a Raspberry Pi first');
    return;
  }

  try {
    await fetchRaspberryDataById(raspberryId);
  } catch (error) {
    alert('Error exporting data');
  }
};

async function onRaspberrySelected(raspberry) {
  selectedRaspberry.value = await fetchRaspberryById(raspberry.id);
  raspberryAPs.value = await fetchAPsById(raspberry.id)
  if (raspberry && raspberry.id) {
    router.push({ name: 'raspberry-details', params: { id: raspberry.id } });
  }
}

onRaspberrySelected({ id: initialId });
</script>
