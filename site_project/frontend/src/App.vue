<template>
  <div>
    <!-- Menu de Navegação (exibido em todas as páginas, exceto na página de login) -->
    <nav v-if="route.path !== '/'" class="menu">
      <div class="menu-links">
        <router-link to="/main" class="menu-item">Dashboard</router-link>
        <router-link to="/raspberry" class="menu-item">Raspberry</router-link>
        <router-link to="/info" class="menu-item">Info</router-link>
      </div>
      <button class="logout-button" @click="logout">Logout</button>
    </nav>

    <!-- Conteúdo da Página -->
    <RouterView />
  </div>
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router';

const route = useRoute();
const router = useRouter();

const logout = () => {
  router.push('/'); // Redireciona para a página de login
};
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  height: 100%;
}

.menu {
  display: flex;
  justify-content: space-between; /* Espaça os itens do menu e o botão de logout */
  align-items: center;
  background-color: #1e1e2f;
  padding: 10px 20px; /* Adiciona espaçamento interno */
  margin: 20px; /* Adiciona margem ao redor do menu */
  border-radius: 15px; /* Bordas arredondadas */
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); /* Adiciona sombra para o efeito flutuante */
  position: fixed; /* Torna o menu flutuante */
  top: 10px; /* Posiciona o menu no topo */
  left: 10px; /* Posiciona o menu à esquerda */
  right: 10px; /* Posiciona o menu à direita */
  z-index: 1000; /* Garante que o menu fique acima de outros elementos */
}

.menu-links {
  display: flex;
  gap: 15px; /* Espaçamento entre os links */
}

.menu-item {
  color: white;
  text-decoration: none;
  font-size: 18px;
  font-family: 'Roboto', sans-serif;
  padding: 10px 15px;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.menu-item:hover {
  background-color: #4CAF50;
}

.logout-button {
  background-color: #e74c3c; /* Cor de fundo vermelha */
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 15px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.logout-button:hover {
  background-color: #c0392b; /* Cor de fundo ao passar o mouse */
}
</style>
