<template>
  <div class="min-h-screen flex flex-col p-36 items-center justify-around">
    <div class="h-[500px] flex gap-8 w-full">

      <div class="flex-2 h-full w-1/3 bg-white rounded-3xl p-8 text-gray-800">
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
      </div>

      <div class="bg-white text-gray-800 rounded-3xl p-8 w-full h-full flex flex-col">
        <h2 class="m-4 text-2xl font-semibold">APs</h2>
        <p class="text-sm">Last Record: {{ selectedRaspberry.ultimo_registro }}</p>
        <div class="flex-1 overflow-y-auto rounded-xl shadow">
          <table class="min-w-full divide-y divide-gray-700 bg-white">
            <thead class="bg-indigo-50 text-gray-700 sticky top-0">
              <tr>
                <th @click="toggleSort('ssid')"
                  class="px-6 py-3 text-left text-sm font-medium uppercase cursor-pointer select-none">ssid
                </th>
                <th @click="toggleSort('bssid')"
                  class="px-6 py-3 text-left text-sm font-medium uppercase cursor-pointer select-none">bssid</th>
                <th @click="toggleSort('rate')"
                  class="px-6 py-3 text-left text-sm font-medium uppercase cursor-pointer select-none">rate</th>
                <th @click="toggleSort('signal')"
                  class="px-6 py-3 text-left text-sm font-medium uppercase cursor-pointer select-none">signal</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-300 text-gray-800">
              <tr v-for="ap in sortedRaspberryAPs" :key="ap.ssid">
                <td class="px-6 py-4"> {{ ap.ssid }} </td>
                <td class="px-6 py-4"> {{ ap.bssid }} </td>
                <td class="px-6 py-4"> {{ ap.rate }} Mbits/s</td>
                <td class="px-6 py-4"> {{ ap.signal }} </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div v-if="selectedRaspberry" class="grid grid-cols-1 gap-6 mt-8 w-full">
      <iframe class="rounded-lg shadow-lg"
        :src="`http://192.92.147.85:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=now-24h&to=now&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=1&__feature.dashboardSceneSolo`"
        width="100%" height="400"></iframe>

      <iframe class="rounded-lg shadow-lg"
        :src="`http://192.92.147.85:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=now-24h&to=now&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=4&__feature.dashboardSceneSolo`"
        width="100%" height="400"></iframe>

      <iframe class="rounded-lg shadow-lg"
        :src="`http://192.92.147.85:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=now-24h&to=now&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=5&__feature.dashboardSceneSolo`"
        width="100%" height="400"></iframe>

      <iframe class="rounded-lg shadow-lg"
        :src="`http://192.92.147.85:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=now-24h&to=now&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=3&__feature.dashboardSceneSolo`"
        width="100%" height="400"></iframe>

      <iframe class="rounded-lg shadow-lg"
        :src="`http://192.92.147.85:3000/d-solo/dekod82b0yyo0b/raspberry-pis?orgId=1&from=now-24h&to=now&timezone=browser&var-raspberry=${selectedRaspberry.id}&panelId=2&__feature.dashboardSceneSolo`"
        width="100%" height="400"></iframe>

    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRoute } from 'vue-router';
import { useRouter } from 'vue-router';
import { fetchRaspberryById, fetchAPsById, fetchRaspberryDataById } from '@/services/raspberryService'; '@/services/raspberryService'
import RaspberrySelector from '@/components/RaspberrySelector.vue';

const selectedRaspberry = ref(null);
const raspberryAPs = ref([]);
const sortKey = ref('ssid');
const sortAsc = ref(true);

const route = useRoute();
const router = useRouter();
const initialId = route.params.id;

const toggleSort = (key) => {
  if (sortKey.value === key) {
    sortAsc.value = !sortAsc.value;
  } else {
    sortKey.value = key;
    sortAsc.value = true;
  }
};

const sortedRaspberryAPs = computed(() => {
  return [...raspberryAPs.value].sort((a, b) => {
    const key = sortKey.value;
    let aVal = a[key];
    let bVal = b[key];

    // Normalize case for strings
    if (typeof aVal === 'string') aVal = aVal.toLowerCase();
    if (typeof bVal === 'string') bVal = bVal.toLowerCase();

    // Convert to numbers if both look numeric
    if (!isNaN(aVal) && !isNaN(bVal)) {
      aVal = Number(aVal);
      bVal = Number(bVal);
    }

    if (aVal < bVal) return sortAsc.value ? -1 : 1;
    if (aVal > bVal) return sortAsc.value ? 1 : -1;
    return 0;
  });
});

async function onRaspberrySelected(raspberry) {
  selectedRaspberry.value = await fetchRaspberryById(raspberry.id);
  raspberryAPs.value = await fetchAPsById(raspberry.id)
  if (raspberry && raspberry.id) {
    router.push({ name: 'raspberry-details', params: { id: raspberry.id } });
  }
}

onRaspberrySelected({ id: initialId });
</script>
