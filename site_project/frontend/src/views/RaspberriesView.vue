<template>
    <div
        class="min-h-screen bg-gradient-to-b from-[#17072b] via-[#2c0e44] to-[#3a0d5b] flex items-center justify-center p-8">
        <div
            class="bg-white rounded-3xl shadow-2xl transition transform duration-500 ease-in-out hover:scale-105 p-8 w-full max-w-3xl text-gray-800">

            <h2 class="text-3xl font-bold text-center mb-6">Choose Raspberry Pi</h2>

            <select v-model="selectedRaspberry" @change="fetchRaspberryData"
                class="block w-full bg-indigo-100 border border-indigo-300 p-3 rounded-lg focus:outline-none focus:ring-4 focus:ring-indigo-400 text-lg mb-6 transition-all">
                <option value="" disabled>Select a Raspberry Pi</option>
                <option v-for="rpi in raspberries" :key="rpi.id" :value="rpi.id">
                    {{ rpi.mac }}
                </option>
            </select>

            <div v-if="raspberryData" class="mt-6 p-6 bg-indigo-50 rounded-xl shadow-inner">
                <h3 class="text-2xl font-semibold mb-4 text-indigo-700">Dados do Raspberry Pi</h3>
                <p class="text-lg"><strong>Nome:</strong> {{ raspberryData.name }}</p>
                <p class="text-lg"><strong>ID:</strong> {{ raspberryData.id }}</p>
                <p class="text-lg"><strong>IP:</strong> {{ raspberryData.price }}</p>
                <p class="text-lg"><strong>Status:</strong> {{ raspberryData.status }}</p>
            </div>

        </div>
    </div>
</template>
  

<script setup>
import { ref } from 'vue';

const raspberries = ref([
  { id: '1', mac: 'B8:27:EB:45:12:34' },
  { id: '2', mac: 'B8:27:EB:67:89:01' }
]);

const selectedRaspberry = ref('');
const raspberryData = ref(null);

const fetchRaspberryData = () => {
  raspberryData.value = {
    name: 'Mocked Raspberry Pi',
    id: selectedRaspberry.value,
    ip: '192.168.1.100',
    status: 'Online'
  };
};
</script>
