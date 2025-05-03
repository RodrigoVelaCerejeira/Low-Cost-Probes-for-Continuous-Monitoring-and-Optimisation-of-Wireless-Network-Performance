<script setup>
import { ref, onMounted } from 'vue';
import { fetchNullRaspberries, fetchRaspberryPis } from '@/services/raspberryService'; '@/services/raspberryService'

const nullIds = ref([])
const raspberries = ref([]);

function is_online(rpi) {
  const time = new Date(rpi.ultimo_registro).getTime()
  const currTime = new Date().getTime()
  return (currTime - time) < (5 * 60 * 1000)
}

function has_null(rpi) {
  return nullIds.value.includes(rpi.id)
}


onMounted(async () => {
  nullIds.value = await fetchNullRaspberries();
  raspberries.value = await fetchRaspberryPis();
});

console.log(nullIds)
console.log(raspberries)
</script>
<template>
  <h1 class="text-5xl font-roboto py-24 text-white text-center ">Overview of Connected Raspberry Pis</h1>
  <div class="flex justify-between items-start px-8 pb-24 gap-8">
    <div
      class="bg-white text-gray-800 rounded-3xl shadow-xl transition transform duration-500 ease-in-out hover:scale-105 p-8 w-full h-full overflow-y-scroll">
      <h2 class="text-2xl font-semibold mb-4">Raspberry Pi Status</h2>
      <table class="min-w-full divide-y divide-gray-700 bg-white rounded-xl shadow overflow-hidden">
        <thead class="bg-gray-100 text-gray-700">
          <tr>
            <th class="px-6 py-3 text-left text-sm font-medium uppercase">Name</th>
            <th class="px-6 py-3 text-left text-sm font-medium uppercase">Status</th>
            <th class="px-6 py-3 text-left text-sm font-medium uppercase">Last Connection</th>
            <th class="px-6 py-3 text-left text-sm font-medium uppercase">Location</th>
            <th class="px-6 py-3 text-left text-sm font-medium uppercase">Failures (Last 24h)</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-300 text-gray-800">
          <tr v-for="rpi in raspberries" :key="rpi.id" :value="rpi">
            <td class="px-6 py-4">{{ rpi.mac }}</td>
            <td v-if="is_online(rpi)" class="px-6 py-4">
              <span class="inline-block px-2 py-1 text-xs font-semibold text-green-800 bg-green-100 rounded-full">
                Online
              </span>
            </td>
            <td v-else class="px-6 py-4">
              <span class="inline-block px-2 py-1 text-xs font-semibold text-red-800 bg-red-100 rounded-full">
                Offline
              </span>
            </td>
            <td class="px-6 py-4"> {{ rpi.ultimo_registro }}</td>
            <td class="px-6 py-4">AQUARIO</td>

            <td v-if="has_null(rpi)" class="px-6 py-4">
              Yes
            </td>
            <td v-else class="px-6 py-4">
              No
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Right side -->
    <div class="flex flex-col gap-6 w-1/2">
      <iframe
        src="http://192.92.147.85:3000/d-solo/eehucflethslca/graficos-iniciais?orgId=1&from=1743642384000&to=1743642385000&timezone=browser&panelId=1&__feature.dashboardSceneSolo"
        width="100%" height="200" frameborder="0" class="rounded-lg shadow-lg"></iframe>
      <iframe
        src="http://192.92.147.85:3000/d-solo/deklyiib84pvka/rtt-info?orgId=1&from=1738363070265&to=1746135470265&timezone=browser&panelId=1&__feature.dashboardSceneSolo"
        width="100%" height="200" frameborder="0" class="rounded-lg shadow-lg"></iframe>
      <iframe
        src="http://192.92.147.85:3000/d-solo/deklapqx0pclcc/latencia?orgId=1&from=1743642384000&to=1743642385000&timezone=browser&panelId=1&__feature.dashboardSceneSolo"
        width="100%" height="200" frameborder="0" class="rounded-lg shadow-lg"></iframe>
      <iframe
        src="http://192.92.147.85:3000/d-solo/deklx7j72vfuod/perda-de-pacot?orgId=1&from=1746166173709&to=1746187773709&timezone=browser&panelId=1&__feature.dashboardSceneSolo"
        width="100%" height="200" frameborder="0" class="rounded-lg shadow-lg"></iframe>
    </div>
  </div>
</template>
