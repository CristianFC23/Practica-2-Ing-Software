<template>
  <!-- Dashboard Cards -->
  <div class="dashboard-cards">
    <!-- Pacientes -->
    <div class="card pacientes-card" :class="{ loading: loading.pacientes }">
      <div class="card-header">
        <div class="card-icon pacientes-icon">
          <span>🧍‍♂️</span>
        </div>
        <div class="card-title">
          <h3>Pacientes</h3>
          <p>Registro y control de pacientes</p>
        </div>
      </div>

      <div class="card-body">
        <div class="card-number">{{ pacientesTotal }}</div>
        <div class="card-label">Total</div>
      </div>

      <div class="card-actions">
        <button @click="nuevoPaciente" class="btn btn-primary">
          <span class="btn-icon">+</span> Nuevo Paciente
        </button>
        <button @click="irAPacientes" class="btn btn-secondary">
          <span class="btn-icon">📋</span> Ver Todos
        </button>
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
        <div class="card-number">{{ laboratoristasTotal }}</div>
        <div class="card-label">Total</div>
      </div>

      <div class="card-actions">
        <button @click="nuevoLaboratorista" class="btn btn-primary">
          <span class="btn-icon">+</span> Nuevo Laboratorista
        </button>
        <button @click="irALaboratoristas" class="btn btn-secondary">
          <span class="btn-icon">📋</span> Ver Todos
        </button>
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
          <button @click="buscarResultado" class="btn btn-search">
            🔍 Buscar
          </button>
        </div>
      </div>

      <div class="card-actions">
        <button @click="nuevoResultado" class="btn btn-primary">
          <span class="btn-icon">+</span> Nuevo Resultado
        </button>
        <button @click="irAResultados" class="btn btn-secondary">
          <span class="btn-icon">📋</span> Ver Todos
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HospitalHome',
  data() {
    return {
      documentoId: '',
      loading: {
        pacientes: false,
        laboratoristas: false,
        resultados: false
      },
      pacientes: { total: 0 },
      laboratoristas: { total: 0 },
      resultados: { total: 0 }
    }
  },
  methods: {
    buscarResultado() {
      if (!this.documentoId) {
        alert('Por favor, ingrese un número de documento.');
        return;
      }
      console.log('Buscando resultados para documento:', this.documentoId);
      // Aquí puedes agregar la lógica para consultar la base de datos
    }
  },
  computed: {
    pacientesTotal() {
      return this.loading.pacientes ? '...' : this.pacientes.total;
    },
    laboratoristasTotal() {
      return this.loading.laboratoristas ? '...' : this.laboratoristas.total;
    },
    resultadosTotal() {
      return this.loading.resultados ? '...' : this.resultados.total;
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
  margin: 0 auto;
}

.resultados-card {
  grid-column: 1 / 3;
}

/* Campos de búsqueda */
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
  justify-content: center;
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

.btn-search {
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: white;
  border: none;
  padding: 10px 18px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-search:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

/* Tarjetas base */
.card {
  background: white;
  border-radius: 16px;
  padding: 25px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  border: 1px solid #e8ecf0;
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
  font-size: 20px;
  margin-right: 15px;
}

.card-body {
  text-align: center;
  margin: 25px 0;
}

.card-actions {
  display: flex;
  gap: 12px;
}

/* Responsive */
@media (max-width: 768px) {
  .dashboard-cards {
    grid-template-columns: 1fr;
  }
  .resultados-card {
    grid-column: auto;
  }
}
</style>