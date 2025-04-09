<script setup>
import { ref, onMounted } from 'vue';
import { defineEmits } from 'vue';
import axios from 'axios';

//cena para mandar um evento
const emit = defineEmits(['selected'])

const raspberries = ref([]);
const selectedRaspberry = ref(null);
const raspberryData = ref(null);
//const pingData = ref([]);

//lanca o evento

// Buscar lista de Raspberry Pis
const fetchRaspberryPis = async () => {
    try {
        const response = await axios.get('http://192.92.147.85:3001/raspberry/devices');
        raspberries.value = response.data;
    } catch (error) {
        console.error('Error fonding Raspberry Pis:', error);
    }
};

//// Buscar os dados do Raspberry Pi selecionado
const fetchRaspberryData = async () => {
    if (selectedRaspberry.value) {
        try {
            const response = await axios.get(`http://192.92.147.85:3001/raspberry/${selectedRaspberry.value}`);
            raspberryData.value = response.data;

            // Buscar os dados de ping
            //const pingResponse = await axios.get(`http://192.92.147.85:3001/raspberry/${selectedRaspberry.value}/ping`);
            //pingData.value = pingResponse.data;
            emit('selected', raspberryData.value);
        } catch (error) {
            console.error('Error getting data from Raspberry Pi:', error);
        }
    }
};

onMounted(fetchRaspberryPis);
</script>

<template>
    <div class="p-4">
        <h2 class="text-lg font-bold mb-2">Choose Raspberry Pi</h2>

        <select v-model="selectedRaspberry" @change="fetchRaspberryData" class="border p-2 rounded">
            <option value="" disabled>Select a Raspberry Pi</option>
            <option v-for="rpi in raspberries" :key="rpi.id" :value="rpi.id">
                {{ rpi.mac }}
            </option>
        </select>
<!--
        <div v-if="raspberryData" class="mt-4 p-4 border rounded bg-gray-100">
            <h3 class="font-bold">Dados do Raspberry Pi:</h3>
            <p><strong>Nome:</strong> {{ raspberryData.name }}</p>
            <p><strong>ID:</strong> {{ raspberryData.id }}</p>
            <p><strong>IP:</strong> {{ raspberryData.price }}</p>
            <strong>Status:</strong> {{ raspberryData.status }}</p>
        </div>

        Tabela de Ping
        <div v-if="pingData.length > 0" class="mt-4 p-4 border rounded bg-white">
            <h3 class="font-bold mb-2">Histórico de Ping</h3>
            <table class="w-full border-collapse border border-gray-300">
                <thead>
                    <tr class="bg-gray-200">
                        <th class="border border-gray-300 p-2">Timestamp</th>
                        <th class="border border-gray-300 p-2">Latência (ms)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="ping in pingData" :key="ping.timestamp">
                        <td class="border border-gray-300 p-2">{{ ping.timestamp }}</td>
                        <td class="border border-gray-300 p-2">{{ ping.latency }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        -->
    </div>
</template>

<style scoped>
select {
    width: 100%;
    max-width: 300px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
}

th,
td {
    border: 1px solid #ccc;
    padding: 8px;
    text-align: center;
}
</style>
