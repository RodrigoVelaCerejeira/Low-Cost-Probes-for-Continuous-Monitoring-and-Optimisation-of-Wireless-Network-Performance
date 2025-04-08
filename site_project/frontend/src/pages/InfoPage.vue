<template>
    <div class="page">
      <div class="info-container">
        <h1>About this PIC</h1>
        <p><strong>Project Theme:</strong> Low-Cost Probes for Continuous Monitoring and Optimisation of Wireless Network Performance</p>
        <p><strong>Degree:</strong> Telecommunications and Informatics Engineering</p>
        <p><strong>Professor:</strong> Dr. Fernando Mira da Silva</p>
        <p><strong>Students:</strong></p>
        <ul>
          <li>ist1107246 - João Simões - 
            <a href="mailto:joaoasimoes@tecnico.ulisboa.pt">joaoasimoes@tecnico.ulisboa.pt</a>
          </li>
          <li>ist1106885 - João Mendonça -
            <a href="mailto:joao.pedro.mendonca@tecnico.ulisboa.pt">joao.pedro.mendonca@tecnico.ulisboa.pt</a>
          </li>
          <li>ist1103193 - Rodrigo Cerejeira - 
            <a href="mailto:rodrigo.vela.cerejeira@tecnico.ulisboa.pt">rodrigo.vela.cerejeira@tecnico.ulisboa.pt</a>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <style scoped>
.page {
  min-height: 100vh;
  background-color: #17072b;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: 'Roboto', sans-serif;
  padding: 20px;
  text-align: center; 
}

.info-container {
  max-width: 100%; 
  text-align: left;
  padding: 20px; 
  box-sizing: border-box; 
}

h1 {
  font-size: 50px;
  font-family: 'Roboto', sans-serif;
  color: #4CAF50;
  margin-bottom: 20px;
}

p, ul {
  font-size: 25px;
  font-family: 'Roboto', sans-serif;
  margin: 10px 0;
  line-height: 1.5;
}

ul {
  padding-left: 20px;
}

ul li {
  list-style-type: disc;
}

a {
  color: #FFD700; 
  text-decoration: none; 
}

a:hover {
  text-decoration: underline; 
}
</style>