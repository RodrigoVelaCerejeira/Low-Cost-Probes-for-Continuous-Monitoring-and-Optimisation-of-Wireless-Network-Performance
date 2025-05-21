<template>
  <!-- Menu -->
  <nav v-if="route.path !== '/'"
    class="fixed top-4 left-1/2 transform -translate-x-1/2 z-50 flex items-center justify-between bg-gray-800 text-white px-8 py-4 rounded-full shadow-lg">
    <div class="flex gap-6">
      <router-link to="/dashboard" :class="[
        'px-4 py-2 rounded-full transition',
        route.path === '/dashboard' ? 'bg-green-500 text-white' : 'hover:bg-green-500 hover:text-white'
      ]">
        Dashboard
      </router-link>
      <router-link to="/raspberries" :class="[
        'px-4 py-2 rounded-full transition',
        route.path.startsWith('/raspberries') ? 'bg-green-500 text-white' : 'hover:bg-green-500 hover:text-white'
      ]">
        Raspberry
      </router-link>
      <router-link to="/info" :class="[
        'px-4 py-2 rounded-full transition',
        route.path === '/info' ? 'bg-green-500 text-white' : 'hover:bg-green-500 hover:text-white'
      ]">
        Info
      </router-link>
    </div>
    <button class="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-full transition ml-20" @click="logout">
      Logout
    </button>
  </nav>

  <RouterView />
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router';

const route = useRoute();
const router = useRouter();

const logout = () => {
  router.push('/');
};
</script>
