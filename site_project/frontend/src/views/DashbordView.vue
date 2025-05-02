<!-- eslint-disable vue/multi-word-component-names -->

<script setup>
import CurrentTime from '../components/CurrentTime.vue';
</script>

<template>
  <div class="min-h-screen bg-gradient-to-b from-[#17072b] via-[#2c0e44] to-[#3a0d5b] text-white text-center py-20">
    <h1 class="text-5xl font-roboto mb-12 mt-16">Overview of Connected Raspberry Pis</h1>

    <!-- Boxes Section -->
    <div class="flex justify-start gap-6 flex-wrap">
      <div
        class="w-80 p-6 rounded-3xl shadow-xl transition transform duration-500 ease-in-out hover:scale-105 bg-white mx-4">
        <CurrentTime />
      </div>
    </div>

    <!-- Graphics -->
    <div class="mt-8 grid grid-cols-2 gap-6">
      <iframe
        src="http://192.92.147.85:3000/d-solo/eehucflethslca/graficos-iniciais?orgId=1&from=1743642384000&to=1743642385000&timezone=browser&panelId=1&__feature.dashboardSceneSolo"
        width="450" height="200" frameborder="0" class="mx-auto"></iframe>
      <iframe
        src="http://192.92.147.85:3000/d-solo/deklyiib84pvka/rtt-info?orgId=1&from=1738363070265&to=1746135470265&timezone=browser&panelId=1&__feature.dashboardSceneSolo"
        width="450" height="200" frameborder="0" class="mx-auto"></iframe>
      <iframe
        src="http://192.92.147.85:3000/d-solo/deklapqx0pclcc/latencia?orgId=1&from=1743642384000&to=1743642385000&timezone=browser&panelId=1&__feature.dashboardSceneSolo"
        width="450" height="200" frameborder="0" class="mx-auto"></iframe>
      <iframe
        src="http://192.92.147.85:3000/d-solo/deklx7j72vfuod/perda-de-pacot?orgId=1&from=1746166173709&to=1746187773709&timezone=browser&panelId=1&__feature.dashboardSceneSolo"
        width="450" height="200" frameborder="0" class="mx-auto"></iframe>
    </div>
  </div>
</template>
