<!-- filepath: /home/joao/Secretária/pic/Low-Cost-Probes-for-Continuous-Monitoring-and-Optimisation-of-Wireless-Network-Performance/site_project/src/pages/RaspberryPage.vue -->
<!-- eslint-disable vue/multi-word-component-names -->

<script setup>
import { ref } from 'vue';
import RaspberrySelector from '../components/RaspberrySelector.vue';

// Dados fictícios para simular os Raspberry Pis
const raspberryList = [
  { id: 1, name: 'Raspberry Pi 1', ip: '192.168.1.101', lastSeen: '2025-03-30 18:45:00' },
  { id: 2, name: 'Raspberry Pi 2', ip: '192.168.1.102', lastSeen: '2025-03-30 19:00:00' },
  { id: 3, name: 'Raspberry Pi 3', ip: '192.168.1.103', lastSeen: '2025-03-30 19:15:00' },
];

// Estado para armazenar o Raspberry Pi selecionado
const selectedRaspberry = ref(null);

// Função chamada quando um Raspberry Pi é selecionado
const onRaspberrySelected = (raspberryId) => {
  selectedRaspberry.value = raspberryList.find((r) => r.id === raspberryId);
};
</script>

<template>
  <div class="dashboard-page">
    <h1>Raspberry Pi Network Monitoring Overview</h1>
    <div class="boxes">
      <!-- Caixa para selecionar o Raspberry Pi -->
      <div class="box_rp">
        <RaspberrySelector @select="onRaspberrySelected" />
      </div>

      <!-- Caixa para exibir informações do Raspberry Pi selecionado -->
      <div class="box_rp" v-if="selectedRaspberry">
        <h3>{{ selectedRaspberry.name }}</h3>
        <p><strong>IP Address:</strong> {{ selectedRaspberry.ip }}</p>
        <p><strong>Last Seen:</strong> {{ selectedRaspberry.lastSeen }}</p>
      </div>
    </div>
    <div class="all_rp">
      <h2>Overview of Connected Raspberry Pis:</h2>
    </div>
  </div>
</template>

<style scoped>
.dashboard-page {
  min-height: 100vh;
  background-color: #17072b;
  text-align: center;
  padding: 20px;
  padding-top: 80px;
}

h1 {
  color: #FFFFFF;
  font-size: 50px;
  margin-bottom: 50px;
  font-family: 'Roboto', sans-serif;
}

h2 {
  color: #FFFFFF;
  font-size: 25px;
  text-align: left;
  margin-left: 10px;
  margin-bottom: 25px;
  font-family: 'Roboto', sans-serif;
}

.boxes {
  display: flex;
  justify-content: flex-start;
  gap: 20px;
  flex-wrap: wrap;
}

.box_rp {
  width: 300px;
  height: auto;
  padding: 15px;
  border-radius: 25px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  background: #fff;
  text-align: left;
}

.box_rp h3 {
  margin-bottom: 10px;
  font-size: 18px;
  color: #4CAF50;
}

.box_rp p {
  margin: 5px 0;
  font-size: 14px;
  color: #333;
}
</style>