<!-- eslint-disable vue/multi-word-component-names -->

<script setup>
import { ref, watch } from 'vue';
import RaspberrySelector from '../components/RaspberrySelector.vue';


const selectedRaspberry = ref(null)

watch(selectedRaspberry, (newVal) => {
    console.log(newVal);
});
</script>

<template>
    <div class="dashboard-page">
        <h1>Raspberry Pi Network Monitoring Overview</h1>
        <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 2rem;">
            <div class="boxes">
                <div class="box_rp">
                    <RaspberrySelector @selected="selectedRaspberry = $event" />
                </div>
            </div>
            <div v-if="selectedRaspberry" class="box_rp">
                <h3 class="font-bold">Dados do Raspberry Pi:</h3>
                <p><strong>Nome:</strong> {{ selectedRaspberry.name }}</p>
                <p><strong>ID:</strong> {{ selectedRaspberry.id }}</p>
                <p><strong>IP:</strong> {{ selectedRaspberry.price }}</p>
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
  background-color: white;
  color: black;
  padding: 24px;
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  font-size: 1.1rem;
  line-height: 1.6;
}
.box_rp p {
  margin-bottom: 12px;
}
.box_rp h3 {
  margin-bottom: 16px;
  font-size: 1.25rem;
}
</style>
