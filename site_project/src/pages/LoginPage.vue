<template>
    <div class="login-page">
      <h1>Low Cost Probes for Continuous Monitoring and Optimisation of Wireless Network Performance</h1>
      <button @click="login">Enter</button>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  
  const login = () => {
    router.push('/main'); // Redireciona para a página principal
  };
  </script>
  
  <style scoped>
  .login-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background-color: #17072b;
    color: white;
  }

  h1 {
  color: #FFFFFF;
  font-size: 50px;
  margin: 50px;
  font-family: 'Roboto', sans-serif;
  text-align: center;
 }
  
  button {
    padding: 10px 20px;
    border: none;
    border-radius: 15px;
    background-color: #4CAF50;
    color: white;
    cursor: pointer;
    font-size: 40px;
  }
  </style>