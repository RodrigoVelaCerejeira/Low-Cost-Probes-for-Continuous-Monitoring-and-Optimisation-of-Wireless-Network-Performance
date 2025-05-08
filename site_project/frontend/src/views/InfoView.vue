<template>
  <div
    class="min-h-screen bg-gradient-to-b from-[#17072b] via-[#2c0e44] to-[#3a0d5b] flex flex-col items-left font-roboto p-5 text-center gap-8 pt-36">

    <div class="flex flex-col lg:flex-row gap-8 w-full justify-left">
      <!-- About this PIC -->
      <div
        class="h-max max-w-5xl text-left p-8 rounded-2xl bg-white shadow-2xl transition transform duration-500 ease-in-out hover:scale-105">
        <h1 class="text-5xl font-bold text-green-500 mb-5">About this PIC</h1>
        <p class="text-2xl mb-4 leading-relaxed tracking-wide"> <strong>Project Theme:</strong> Low-Cost Probes for
          Continuous Monitoring and Optimisation of Wireless Network Performance
        </p>
        <p class="text-2xl mb-4 leading-relaxed tracking-wide"> <strong>Degree:</strong> Telecommunications and
          Informatics Engineering
        </p>
        <p class="text-2xl mb-4 leading-relaxed tracking-wide"> <strong>Professor:</strong> Dr. Fernando Mira da
          Silva
        </p>
        <p class="text-2xl mb-4 leading-relaxed tracking-wide"> <strong>Students:</strong>
        </p>

        <ul class="list-disc pl-8 text-2xl space-y-4 marker:text-green-500">
          <li>
            ist1107246 - João Simões -
            <a href="mailto:joaoasimoes@tecnico.ulisboa.pt" class="text-blue-800 hover:underline">
              joaoasimoes@tecnico.ulisboa.pt
            </a>
          </li>
          <li>
            ist1106885 - João Mendonça -
            <a href="mailto:joao.pedro.mendonca@tecnico.ulisboa.pt" class="text-blue-800 hover:underline">
              joao.pedro.mendonca@tecnico.ulisboa.pt
            </a>
          </li>
          <li>
            ist1103193 - Rodrigo Cerejeira -
            <a href="mailto:rodrigo.vela.cerejeira@tecnico.ulisboa.pt" class="text-blue-800 hover:underline">
              rodrigo.vela.cerejeira@tecnico.ulisboa.pt
            </a>
          </li>
        </ul>
      </div>

      <!-- Main Goals e botão -->
      <div class="flex flex-col flex-grow">
        <!-- Main Goals -->
        <div
          class="h-max text-left p-8 rounded-2xl bg-white shadow-2xl transition transform duration-500 ease-in-out hover:scale-105">
          <h1 class="text-5xl font-bold text-blue-500 mb-5">Main Goals</h1>
          <ul class="list-disc pl-8 text-2xl space-y-4 marker:text-blue-500">
            <li>Desing and implementation of a database structure;</li>
            <li>Setup and configuration of Raspberry Pi devices for data collection;</li>
            <li>Development and configuration of a website for data presentation.</li>
          </ul>
        </div>

        <!-- Button -->
        <div class="mt-4">
          <a href="https://www.canva.com/design/DAGfpF_VQ7E/b5BENSIHwRL8Y3xnTMMymQ/view?utm_content=DAGfpF_VQ7E&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h6af9bbb92c"
            target="_blank" rel="noopener noreferrer">
            <button
              class="bg-purple-500 text-white px-6 py-3 rounded-lg shadow-lg hover:bg-purple-600 transition transform hover:scale-105 hover:shadow-xl focus:outline-none focus:ring-4 focus:ring-purple-300">
              View Presentation
            </button>
          </a>
        </div>

      </div>
    </div>

    <!-- With this project -->
    <div
      class="h-max max-w-5xl text-left p-8 rounded-2xl bg-white shadow-2xl transition transform duration-500 ease-in-out hover:scale-105">
      <h1 class="text-5xl font-bold text-purple-500 mb-5">Graphs and Metrics You Can Explore</h1>
      <ul class="list-disc pl-8 text-2xl space-y-4 marker:text-purple-500">
        <li>Download Speed Over Time;</li>
        <li>Upload Speed Over Time;</li>
        <li>Packet Loss;</li>
        <li>Latency;</li>
        <li>Jitter;</li>
        <li>Round-Trip Time (RTT).</li>

      </ul>
    </div>
  </div>
</template>