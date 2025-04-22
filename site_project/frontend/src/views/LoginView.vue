<template>
    <div class="min-h-screen bg-gradient-to-b from-[#17072b] via-[#2c0e44] to-[#3a0d5b] flex items-center justify-center p-6">
    <div class="text-center text-white space-y-8">
        <img 
                src="@/assets/logo.png" 
                alt="Logo" 
                class="mx-auto mb-8 w-32 h-auto" 
            />
        <header class="mb-6">
            <h1 class="text-5xl font-bold text-center" style="color: #f3f4f6;">
                Low Cost Probes for Continuous Monitoring 
                and Optimisation of Wireless Network Performance
            </h1>
            <button 
            @click="login"
            class="mt-10 bg-indigo-600 hover:bg-indigo-700 hover:scale-105 transform text-white text-xl font-semibold py-2 px-6 rounded-lg transition duration-300"
            >  Enter
</button>
        </header>
    </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const login = () => {
    router.push('/dashboard');
};

</script>