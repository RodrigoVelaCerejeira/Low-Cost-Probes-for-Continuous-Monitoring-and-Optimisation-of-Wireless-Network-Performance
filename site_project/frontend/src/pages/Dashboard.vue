<!-- eslint-disable vue/multi-word-component-names -->

<script setup>
import CurrentTime from '../components/CurrentTime.vue';
</script>

<template>
  <div class="dashboard-page">
    <h1>Overview of Connected Raspberry Pis</h1>
    <div class="boxes">
      <div class="box_clock">
        <CurrentTime />
      </div>
    </div>
    <div class="all_rp">
      <iframe
        src="http://192.92.147.85:3000/d-solo/eehucflethslca/graficos-iniciais?orgId=1&from=1743642384000&to=1743642385000&timezone=browser&panelId=1&__feature.dashboardSceneSolo"
        width="450" height="200" frameborder="0"></iframe>
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

.box_clock {
  width: 300px;
  padding: 15px;
  border-radius: 25px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  background: #fff;
}
</style>
