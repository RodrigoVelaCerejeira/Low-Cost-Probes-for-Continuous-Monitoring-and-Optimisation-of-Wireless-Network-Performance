<!-- filepath: /home/joao/Secretária/pic/pic-project/site_project/frontend/src/views/DashbordView.vue -->
<template>
  <div class="min-h-screen bg-gradient-to-b from-[#17072b] via-[#2c0e44] to-[#3a0d5b] text-white text-center py-20">
    <h1 class="text-5xl font-roboto mb-12 mt-16">Overview of Connected Raspberry Pis</h1>


    <div class="flex justify-between items-start px-8 gap-8">
      <!-- Left side -->
      <div class="flex flex-col gap-8 w-1/2">
        <!-- Welcome Box -->

        <!-- Info -->
        <div
          class="bg-white text-gray-800 rounded-3xl shadow-xl transition transform duration-500 ease-in-out hover:scale-105 p-8 w-full h-80 overflow-y-scroll">
          <h2 class="text-2xl font-semibold mb-4">Dashboard bla bla</h2>
          <p class="text-lg">bla bla bla bla bla bla bla bla bla bla</p>
          <p class="text-lg mt-4">bla bla bla</p>
          <p class="text-lg mt-4">bla</p>
          <p class="text-lg mt-4">bla</p>
          <p class="text-lg mt-4">bla</p>
          <p class="text-lg mt-4">bla</p>
        </div>
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
  </div>
</template>
