<template>
  <div id="app">
    <!-- Header -->
    <header class="header">
      <div class="header-left">
        <img src="@/assets/logo.png" alt="Logo" class="logo" />
        <div class="company-info">
          <h1 class="company-name">Fedora INC</h1>
          <p class="system-name">Sistema de gestión hospitalaria</p>
        </div>
      </div>

      <nav class="header-nav">
        <router-link to="/">Home</router-link>
        <router-link to="/pacientes">Pacientes</router-link>
        <router-link to="/laboratoristas">Laboratoristas</router-link>
        <router-link to="/resultados">Resultados</router-link>
      </nav>
    </header>

    <!-- Contenedor para las vistas -->
    <main class="main-container">
      <router-view />
    </main>
  </div>
</template>

<script>
export default {
  name: 'HospitalHome'
};
</script>

<style>
/* --- RESET GLOBAL --- */
html, body, #app {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
}

* {
  box-sizing: border-box;
}

/* --- Layout general --- */
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  width: 100vw;
  background: linear-gradient(135deg, #7e5bef 0%, #10b981 100%);
  background-attachment: fixed;
  font-family: 'Inter', sans-serif;
  color: #1f2937;
  overflow: hidden;
}

/* --- Header --- */
.header {
  backdrop-filter: blur(15px);
  background: rgba(255, 255, 255, 0.25);
  color: #f9fafb;
  padding: 16px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
  height: 70px;
  border-radius: 0 0 16px 16px;
}

/* --- Logo e información --- */
.header-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo {
  height: 45px;
  width: auto;
  border-radius: 10px;
}

.company-info {
  display: flex;
  flex-direction: column;
}

.company-name {
  font-size: 18px;
  font-weight: 700;
  color: #ffffff;
  margin: 0;
}

.system-name {
  font-size: 13px;
  font-weight: 400;
  color: #f3f4f6;
  opacity: 0.9;
  margin: 0;
}

/* --- Navegación --- */
.header-nav {
  display: flex;
  gap: 16px;
}

.header-nav a {
  color: #f9fafb;
  text-decoration: none;
  font-weight: 600;
  font-size: 14px;
  padding: 8px 14px;
  border-radius: 12px;
  transition: all 0.3s ease;
}

.header-nav a:hover {
  background: rgba(255, 255, 255, 0.2);
}

.header-nav a.router-link-exact-active {
  background: #10b981;
  color: white;
}

/* --- Contenedor principal (router-view) --- */
.main-container {
  flex: 1;
  padding: 0;
  margin: 0;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: start;
}

/* --- Responsividad --- */
@media (max-width: 768px) {
  .header {
    flex-direction: column;
    align-items: flex-start;
    height: auto;
    padding: 12px 16px;
  }

  .header-left {
    width: 100%;
    justify-content: space-between;
  }

  .company-name {
    font-size: 16px;
  }

  .system-name {
    font-size: 12px;
  }

  .header-nav {
    width: 100%;
    justify-content: space-around;
    flex-wrap: wrap;
    margin-top: 10px;
  }

  .header-nav a {
    font-size: 13px;
    padding: 6px 10px;
  }
}
</style>
