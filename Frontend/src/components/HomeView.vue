<template>
  <!-- Dashboard Cards -->
  <div class="dashboard-cards">
    <!-- Pacientes -->
    <div class="card pacientes-card" :class="{ loading: loading.pacientes }">
      <div class="card-header">
        <div class="card-icon pacientes-icon">
          <span>😷</span>
        </div>
        <div class="card-title">
          <h3>Pacientes</h3>
          <p>Registro y control de pacientes</p>
        </div>
      </div>

      <div class="card-body">
        <div class="card-number">Cantidad</div>
        <div class="card-label">Total</div>
      </div>

      <div class="card-actions">
        <router-link to="/paciente/nuevo" class="btn btn-primary">
          <span class="btn-icon">+</span> Nuevo Paciente
        </router-link>
        <router-link to="/pacientes" class="btn btn-secondary">
          <span class="btn-icon">📋</span> Ver Todos
        </router-link>
      </div>
    </div>

    <!-- Laboratoristas -->
    <div class="card laboratoristas-card" :class="{ loading: loading.laboratoristas }">
      <div class="card-header">
        <div class="card-icon laboratoristas-icon">
          <span>🧪</span>
        </div>
        <div class="card-title">
          <h3>Laboratoristas</h3>
          <p>Gestión del personal de laboratorio</p>
        </div>
      </div>

      <div class="card-body">
        <div class="card-number">Cantidad</div>
        <div class="card-label">Total</div>
      </div>

      <div class="card-actions">
        <router-link to="/laboratorista/nuevo" class="btn btn-primary">
          <span class="btn-icon">+</span> Nuevo Laboratorista
        </router-link>
        <router-link to="/laboratoristas" class="btn btn-secondary">
          <span class="btn-icon">📋</span> Ver Todos
        </router-link>
      </div>
    </div>

    <!-- Resultados -->
    <div class="card resultados-card" :class="{ loading: loading.resultados }">
      <div class="card-header">
        <div class="card-icon resultados-icon">
          <span>📊</span>
        </div>
        <div class="card-title">
          <h3>Resultados</h3>
          <p>Consulta de resultados clínicos</p>
        </div>
      </div>

      <div class="card-body">
        <label class="input-label" for="docId">Documento de Identificación</label>
        <div class="input-group">
          <input
            id="docId"
            type="text"
            v-model="documentoId"
            placeholder="Ej: 12345678"
            class="input-field"
          />
          <router-link to="/resultados" class="btn btn-search">
            <span class="btn-icon">🔍 Buscar</span> 
          </router-link>
          

          <!-- <button @click="buscarResultado" class="btn btn-search">
            🔍 Buscar
          </button> -->
        </div>
      </div>
      <router-link to="/resultados" class="btn btn-secondary">
            <span class="btn-icon">📋</span> Ver Todos
          </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data() {
    return {
      documentoId: '',
      loading: {
        pacientes: false,
        laboratoristas: false,
        resultados: false
      }
    }
  },
  methods: {
    buscarResultado() {
      if (!this.documentoId.trim()) {
        alert('Por favor, ingrese un número de documento.');
        return;
      }
      console.log('Buscando resultados para documento:', this.documentoId);
      // Aquí podrías hacer una redirección, por ejemplo:
      // this.$router.push(`/resultados/${this.documentoId}`);
    }
  }
}
</script>

<style scoped>
.dashboard-cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: auto auto;
  gap: 30px;
  max-width: 1200px;
  margin: 40px auto;
  padding: 0 20px;
  width: 100%;
}

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

.card-header {
  display: flex;
  align-items: flex-start;
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

.card-title h3 {
  margin: 0;
  font-size: 18px;
  font-weight: 600;
  color: #2c3e50;
}

.card-title p {
  margin: 4px 0 0;
  font-size: 14px;
  color: #6b7280;
}

.card-body {
  text-align: center;
  margin: 25px 0;
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

.card-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
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
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  text-decoration: none;
}

.btn-primary {
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: white;
}

.btn-primary:hover {
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
  transform: translateY(-1px);
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.8);
  color: #374151;
  border: 1px solid rgba(209, 213, 219, 0.8);
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.95);
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

.input-label {
  display: block;
  text-align: left;
  margin-bottom: 8px;
  font-weight: 600;
  color: #2c3e50;
}

.input-group {
  display: flex;
  gap: 10px;
  align-items: center;
}

.input-field {
  flex: 1;
  padding: 10px 14px;
  border-radius: 8px;
  border: 1px solid #ccc;
  font-size: 15px;
  outline: none;
  transition: all 0.3s ease;
}

.input-field:focus {
  border-color: #764ba2;
  box-shadow: 0 0 4px rgba(118, 75, 162, 0.3);
}

.resultados-card {
  grid-column: 1 / 3;
}

@media (max-width: 768px) {
  .dashboard-cards {
    grid-template-columns: 1fr;
  }

  .resultados-card {
    grid-column: auto;
  }
}
</style>
