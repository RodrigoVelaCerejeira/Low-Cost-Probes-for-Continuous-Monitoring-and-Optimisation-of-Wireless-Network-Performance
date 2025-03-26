<script setup>
import CurrentTime from './components/CurrentTime.vue';
import RaspberrySelector from './components/RaspberrySelector.vue';
</script>

<template>
  <div class="page">
    <h1>Low Cost Probes for Continuous Monitoring and Optimisation of Wireless Network Performance</h1>
    <div class="boxes">
      <div class="box_clock">
        <CurrentTime />
      </div>
      <div class="box_rp">
        <RaspberrySelector />
      </div>
    </div>
  </div>
</template>

<style scoped>
.page {
  min-height: 100vh; /* Garante que a página ocupe toda a altura */
  background-color: #17072b; /* Fundo da página */
  text-align: center; /* Centraliza o texto */
  padding: 20px; /* Espaçamento interno */
}


h1 {
  color: #FFFFFF;
  font-size: 50px;
  margin-bottom: 50px;
  font-family: 'Roboto', sans-serif;
}

.boxes {
  display: flex; /* Coloca as caixas lado a lado */
  justify-content: flex-start;
  gap: 20px;
  flex-wrap: wrap;
}


.box_clock{
  width: 300px;
  padding: 15px;
  border-radius: 25px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  background: #fff;
}

.box_rp {
  width: 300px;
  height: 120px;
  padding: 15px;
  border-radius: 25px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  background: #fff;
}

</style>

<style>
html, body {
  background-color: #17072b;
  margin: 0;
  padding: 0;
}
</style>