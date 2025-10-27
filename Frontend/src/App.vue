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

    <!-- Dashboard principal -->
    <main class="main-content">
      <div class="dashboard-grid">
        <!-- Pacientes -->
        <div class="card pacientes-card">
          <div class="card-header">
            <div class="card-icon pacientes-icon">🧍‍♂️</div>
            <div class="card-title">
              <h3>Pacientes</h3>
              <p>Gestión de pacientes registrados</p>
            </div>
          </div>
          <div class="card-body">
            <div class="card-number">{{ pacientesTotal }}</div>
            <div class="card-label">Total</div>
          </div>
          <div class="card-actions">
            <button class="btn btn-primary">+ Nuevo Paciente</button>
            <button class="btn btn-secondary">Ver Todos</button>
          </div>
        </div>

        <!-- Laboratoristas -->
        <div class="card laboratoristas-card">
          <div class="card-header">
            <div class="card-icon laboratoristas-icon">🧪</div>
            <div class="card-title">
              <h3>Laboratoristas</h3>
              <p>Gestión del personal de laboratorio</p>
            </div>
          </div>
          <div class="card-body">
            <div class="card-number">{{ laboratoristasTotal }}</div>
            <div class="card-label">Total</div>
          </div>
          <div class="card-actions">
            <button class="btn btn-primary">+ Nuevo Laboratorista</button>
            <button class="btn btn-secondary">Ver Todos</button>
          </div>
        </div>

        <!-- Resultados (grande) -->
        <div class="card resultados-card">
          <div class="card-header">
            <div class="card-icon resultados-icon">📊</div>
            <div class="card-title">
              <h3>Resultados</h3>
              <p>Consulta y gestión de resultados clínicos</p>
            </div>
          </div>

          <div class="resultados-search">
            <input
              type="text"
              v-model="documentoId"
              placeholder="Documento de identificación..."
              class="input-search"
            />
            <button class="btn btn-search" @click="buscarResultados">
              🔍 Buscar
            </button>
          </div>

          <div class="card-body">
            <div class="card-number">{{ resultadosTotal }}</div>
            <div class="card-label">Resultados Totales</div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'HospitalHome',
  data() {
    return {
      pacientesTotal: 120,
      laboratoristasTotal: 35,
      resultadosTotal: 480,
      documentoId: ''
    };
  },
  methods: {
    buscarResultados() {
      if (!this.documentoId.trim()) {
        alert('Por favor, ingresa un número de documento.');
        return;
      }
      console.log('Buscando resultados para:', this.documentoId);
      // Aquí iría la lógica de búsqueda
    }
  }
};
</script>

<style scoped>
/* Fondo general */
#app {
  min-height: 100vh;
  background: linear-gradient(135deg, #7e5bef 0%, #10b981 100%);
  background-attachment: fixed;
  font-family: 'Inter', sans-serif;
  color: #1f2937;
}

/* Header */
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

.header-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo {
  height: 50px;
  width: auto;
  border-radius: 10px;
}

.company-info {
  display: flex;
  flex-direction: column;
}

.company-name {
  font-size: 20px;
  font-weight: 700;
  color: #ffffff;
}

.system-name {
  font-size: 14px;
  font-weight: 400;
  color: #f3f4f6;
  opacity: 0.9;
}

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

/* Main Content */
.main-content {
  flex: 1;
  padding: 40px;
  background: rgba(255, 255, 255, 0.25);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  margin: 40px auto;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
  color: #1f2937;
  max-width: 1200px;
}

/* Grid Dashboard */
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: auto auto;
  gap: 24px;
}

.resultados-card {
  grid-column: span 2;
}

/* Cards */
.card {
  background: rgba(255, 255, 255, 0.6);
  border-radius: 16px;
  padding: 25px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.3);
  transition: all 0.3s ease;
}

.card:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
}

/* Card Header */
.card-header {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.card-icon {
  width: 50px;
  height: 50px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  margin-right: 15px;
}

.pacientes-icon {
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: white;
}

.laboratoristas-icon {
  background: linear-gradient(135deg, #11998e, #38ef7d);
  color: white;
}

.resultados-icon {
  background: linear-gradient(135deg, #fc7c7c, #ffb347);
  color: white;
}

.card-title h3 {
  font-size: 18px;
  font-weight: 600;
  margin: 0 0 4px 0;
  color: #2c3e50;
}

.card-title p {
  font-size: 13px;
  color: #6b7280;
  margin: 0;
}

/* Card Body */
.card-body {
  text-align: center;
  margin: 20px 0;
}

.card-number {
  font-size: 42px;
  font-weight: 700;
  color: #1f2937;
}

.card-label {
  font-size: 14px;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 1px;
}

/* Card Buttons */
.card-actions {
  display: flex;
  gap: 10px;
}

.btn {
  flex: 1;
  padding: 10px 14px;
  border: none;
  border-radius: 10px;
  font-weight: 600;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-primary {
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: white;
}

.btn-primary:hover {
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.8);
  color: #374151;
  border: 1px solid rgba(209, 213, 219, 0.8);
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.95);
}

/* Resultados Search */
.resultados-search {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.input-search {
  flex: 1;
  padding: 10px 14px;
  border-radius: 8px;
  border: 1px solid rgba(209, 213, 219, 0.6);
  background: rgba(255, 255, 255, 0.7);
  outline: none;
  font-size: 14px;
}

.input-search:focus {
  border-color: #7e5bef;
  background: white;
}

.btn-search {
  background: linear-gradient(135deg, #7e5bef, #10b981);
  color: white;
  padding: 10px 18px;
  border-radius: 8px;
  font-weight: 600;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-search:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(126, 91, 239, 0.4);
}
</style>
