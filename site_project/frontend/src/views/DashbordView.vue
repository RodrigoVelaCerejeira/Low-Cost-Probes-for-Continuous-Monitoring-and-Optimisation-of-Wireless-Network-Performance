<template>
  <h1 class="text-5xl font-roboto py-24 text-white text-center mt-8">Overview of Connected Raspberry Pis</h1>
  <div class="flex flex-col gap-8 px-8 pb-24">
    <div
      class="bg-white text-gray-800 rounded-3xl shadow-xl transition transform duration-500 ease-in-out hover:scale-105 p-8 w-full h-full overflow-y-scroll">
      <h2 class="text-2xl font-semibold mb-4">Raspberry Pi Status</h2>
      <table class="min-w-full divide-y divide-gray-700 bg-white rounded-xl shadow overflow-hidden">
        <thead class="bg-gray-100 text-gray-700">
          <tr>
            <th class="px-6 py-3 text-left text-sm font-medium uppercase">Select</th>
            <th class="px-6 py-3 text-left text-sm font-medium uppercase">MAC Address</th>
            <th class="px-6 py-3 text-left text-sm font-medium uppercase">Status</th>
            <th class="px-6 py-3 text-left text-sm font-medium uppercase">Last Connection</th>
            <th class="px-6 py-3 text-left text-sm font-medium uppercase">Location</th>
            <th class="px-6 py-3 text-left text-sm font-medium uppercase">Failures (Last 24h)</th>
            <th class="px-6 py-3 text-left text-sm font-medium uppercase">Last hour</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-300 text-gray-800">
          <tr v-for="rpi in raspberries" :key="rpi.id" class="hover:bg-gray-100 cursor-pointer"
            @click="navigateToRaspberry(rpi.id)">
            <td class="px-6 py-4">
              <input type="checkbox" :value="rpi.id" v-model="selectedRaspberries"
                class="form-checkbox h-7 w-7 text-indigo-600" @click.stop="limijtSelection" />
            </td>
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
            <td class="px-6 py-4">
              <span v-if="!is_online(rpi) || rpi.has_error" class="inline-block w-4 h-4 bg-red-500 rounded-full"
                title="Error"></span>
              <span v-else class="inline-block w-4 h-4 bg-green-500 rounded-full" title="No Error"></span>
            </td>
          </tr>
        </tbody>
      </table>

      <div class="p-4 mt-4 bg-blue-50 border border-blue-300 text-blue-800 rounded-md">
        <p> ℹ️ Select 1 raspberry to view failures.</p>
      </div>
      <div class="p-4 mt-1 bg-blue-50 border border-blue-300 text-blue-800 rounded-md">
        <p> ℹ️ Select at least 1 raspberries and no more than 3.</p>
      </div>


      <div class="mt-4 flex justify-end">

        <button @click="openPopup(rpi)" :disabled="selectedRaspberries.length != 1" class="px-6 py-2 rounded-lg shadow transition duration-300 ease-in-out
            hover:scale-105
            disabled:bg-transparent disabled:text-gray-400 disabled:border disabled:border-gray-400
            bg-indigo-600 text-white hover:bg-indigo-700 mr-4">
          View Failures
        </button>

        <button @click="viewSelectedData" :disabled="selectedRaspberries.length === 0" class="px-6 py-2 rounded-lg shadow transition duration-300 ease-in-out
            hover:scale-105
            disabled:bg-transparent disabled:text-gray-400 disabled:border disabled:border-gray-400
            bg-indigo-600 text-white hover:bg-indigo-700">
          View Selected Data
        </button>

      </div>
    </div>

    <div
      class="bg-white text-gray-800 rounded-3xl shadow-xl transition transform duration-500 ease-in-out hover:scale-105 p-8 w-full h-full overflow-y-scroll">
      <h2 class="text-2xl font-semibold mb-4">APs</h2>
    </div>

    <div v-if="isPopupVisible" class="fixed inset-0 bg-gray-800 bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-lg shadow-lg p-6 w-1/3">
        <h2 class="text-xl font-semibold mb-4">Raspberry Pi Failures in the Last Hour</h2>
        <div v-if="!is_online(selectedRaspberries[0])" class="px-6 py-4">
          Raspberry Pi {{ selectedRaspberries[0] }} is offline.
        </div>
        <ul>
          <li v-for="(failureList, failureType) in selectedFailures" :key="failureType">
            <strong>{{ failureType }}:</strong> {{ failureList.join(', ') }}
          </li>
        </ul>
        <button @click="closePopup" class="mt-4 px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700">
          Close
        </button>
      </div>
    </div>

    <div v-if="graphsVisible" class="mt-6">

      <div class="w-1/3">
        <iframe
          src="http://192.92.147.85:3000/d-solo/deklx7j72vfuod/perda-de-pacot?orgId=1&from=1746166173709&to=1746187773709&timezone=browser&panelId=1&__feature.dashboardSceneSolo"
          width="100%" height="330" frameborder="0" class="rounded-lg shadow-lg"></iframe>
      </div>

      <div class="flex gap-6">
        <iframe
          src="http://192.92.147.85:3000/d-solo/eehucflethslca/graficos-iniciais?orgId=1&from=1744120391807&to=1746712391807&timezone=browser&panelId=2&__feature.dashboardSceneSolo"
          class="w-1/2 h-96 rounded-lg shadow-lg"></iframe>

        <iframe
          src="http://192.92.147.85:3000/d-solo/eehucflethslca/graficos-iniciais?orgId=1&from=1743642384000&to=1743642385000&timezone=browser&panelId=1&__feature.dashboardSceneSolo"
          class="w-1/2 h-96 rounded-lg shadow-lg"></iframe>
      </div>
      <iframe
        src="http://192.92.147.85:3000/d-solo/eehucflethslca/graficos-iniciais?orgId=1&from=1746138776000&to=1746762000000&timezone=browser&panelId=4&__feature.dashboardSceneSolo"
        class="w-1/2 h-96 rounded-lg shadow-lg"></iframe>

      <div class="mt-6">
        <iframe
          src="http://192.92.147.85:3000/d-solo/deklyiib84pvka/rtt-info?orgId=1&from=1738363070265&to=1746135470265&timezone=browser&panelId=1&__feature.dashboardSceneSolo"
          class="w-full h-96 rounded-lg shadow-lg"></iframe>
      </div>

    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { ref, onMounted } from 'vue';
import { fetchNullRaspberries, fetchRaspberryPis, fetchFailuresLastHour } from '@/services/raspberryService';
import { toast } from 'vue3-toastify';

const nullIds = ref([]);
const raspberries = ref([]);
const router = useRouter();
const selectedRaspberries = ref([]);
const graphsVisible = ref(false);
const previousStatuses = ref({}); 

function is_online(rpi) {
  const time = new Date(rpi.ultimo_registro).getTime();
  const currTime = new Date().getTime();
  return currTime - time < 8 * 60 * 1000; 
}

function has_null(rpi) {
  return nullIds?.value?.includes?.(rpi.id) ?? false;
}

function navigateToRaspberry(id) {
  router.push({ name: 'raspberry-details', params: { id } });
}

function viewSelectedData() {
  graphsVisible.value = selectedRaspberries.value.length > 0;
}

function limitSelection(event) {
  if (selectedRaspberries.value.length > 3) {
    event.preventDefault();
    alert('You can only select up to 3 Raspberry Pis.');
  }
}

function checkStatusChange() {
  raspberries.value.forEach((rpi) => {
    const currentStatus = is_online(rpi);
    const previousStatus = previousStatuses.value[rpi.id]; 

    if (previousStatus === true && currentStatus === false) {
      toast.error(`Raspberry Pi ${rpi.mac} is now offline!`);
    }

    previousStatuses.value[rpi.id] = currentStatus;
  });
}

async function checkLastHourRecords(raspberryId) {
  try {
    const failures = await fetchFailuresLastHour();
    const hasFailures = Object.values(failures).some((failureList) => failureList.includes(raspberryId));
    return hasFailures; // true -> exist failures, false -> no failures
  } catch (error) {
    console.error(`Error checking last hour records for Raspberry Pi ${raspberryId}:`, error);
    return false;
  }
}

async function getSpecificFailures(raspberryId) {
  try {
    const failures = await fetchFailuresLastHour(); 
    const specificFailures = {}; 

    for (const [failureType, failureList] of Object.entries(failures)) {
      if (failureList.includes(raspberryId)) {
        specificFailures[failureType] = failureList; 
      }
    }

    return specificFailures; 
  } catch (error) {
    console.error(`Error fetching specific failures for Raspberry Pi ${raspberryId}:`, error);
    return {};
  }
}

const isPopupVisible = ref(false);
const selectedFailures = ref({});

async function openPopup(raspberryId) {
  selectedFailures.value = await getSpecificFailures(raspberryId); 
  isPopupVisible.value = true;
}

function closePopup() {
  isPopupVisible.value = false;
}


onMounted(async () => {
  nullIds.value = await fetchNullRaspberries();
  const response = await fetchRaspberryPis();
  raspberries.value = response;


  for (const rpi of raspberries.value) {
    rpi.has_error = await checkLastHourRecords(rpi.id); 
    rpi.failures = await getSpecificFailures(rpi.id); 
  }

  raspberries.value.forEach((rpi) => {
    previousStatuses.value[rpi.id] = is_online(rpi);
  });

  setInterval(checkStatusChange, 5000);
});
</script>
