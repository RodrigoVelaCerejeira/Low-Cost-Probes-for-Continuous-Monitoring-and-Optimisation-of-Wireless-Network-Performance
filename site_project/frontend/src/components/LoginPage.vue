<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const enterApp = () => {
  router.push('/home'); // Redireciona para a página inicial
};
</script>

<template>
  <div class="login-container">
    <h1>Welcome</h1>
    <p>Monitor and optimize your wireless network with ease.</p>
    <button @click="enterApp">Enter</button>
  </div>
</template>

<style scoped>
.login-container {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: #17072b;
  color: white;
  text-align: center;
}

h1 {
  font-size: 32px;
  margin-bottom: 10px;
}

p {
  font-size: 18px;
  margin-bottom: 30px;
}

button {
  padding: 10px 20px;
  font-size: 18px;
  border: none;
  background: #5a189a;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background: #7b2cbf;
}
</style>
