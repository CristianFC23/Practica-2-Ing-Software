<template>
  <div class="page-container">
    <div class="dashboard-cards">
      <div class="card resultadoes-card">
        <div class="card-header">
          <div class="card-icon resultadoes-icon">
            <span>📊</span>
          </div>
          <div class="card-title">
            <h3>Resultados Médicos</h3>
            <p>Buscar, editar o eliminar resultados médicos</p>
          </div>
        </div>

        <div class="card-body">
          <input
            type="text"
            v-model="searchQuery"
            placeholder="Ingrese código de ingreso del paciente"
            class="search-input"
          />
          <button @click="refrescarLista" class="refresh-btn" :disabled="loading">
            {{ loading ? 'Cargando...' : 'Refrescar' }}
          </button>

          <router-link to="/resultados/nuevo" class="btn btn-primary">
            <span class="btn-icon">+</span> Nuevo Resultado
          </router-link>
        </div>

        <div v-if="loading" class="loading-state">
          <p>Cargando resultadoss...</p>
        </div>

        <div v-if="error" class="error-state">
          <p>{{ error }}</p>
          <button @click="refrescarLista" class="retry-btn">Reintentar</button>
        </div>

        <div v-if="!loading && !error" class="card-body resultadoes-list">
          <div v-if="resultadosFiltrados.length === 0" class="no-results">
            <p>
              {{ searchQuery
                ? 'No se encontraron resultadoss que coincidan con la búsqueda'
                : 'No hay resultadoss registrados' }}
            </p>
          </div>

          <div v-else>
            <p class="results-count">
              {{ resultadosFiltrados.length }} resultados(s) encontrado(s)
            </p>
            <div
              v-for="resultados in resultadosFiltrados"
              :key="resultados.id"
              class="resultado-item"
            >
              <div class="resultado-info">
                <p class="resultado-nombre"><strong>Codigo ingreso:</strong> {{ resultados.cod_ing_r }}</p>
                <p class="resultado-detalle"><strong>Cedula:</strong> {{ resultados.cedula }} </p>
                <p class="resultado-detalle"><strong>Colesterol Total:</strong> {{ resultados.col_tot }}</p>
                <p class="resultado-detalle"><strong>Colesterol HDL:</strong> {{ resultados.col_hdl }}</p>
                <p class="resultado-detalle"><strong>Colesterol LDL:</strong> {{ resultados.col_ldl }}</p>
              </div>
              <div class="acciones">
                <button class="edit-btn" @click.stop="abrirModalEditar(resultados)">EDITAR</button>
                <button class="delete-btn" @click.stop="eliminarresultados(resultados.id)">ELIMINAR</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal de edición -->
    <div v-if="mostrarModal" class="modal-overlay">
      <div class="modal-content">
        <h3>Editar resultados Médico</h3>
        
        <label>Código</label>
        <input v-model="resultadosEditando.codigo" placeholder="Ej: EQ-001" />
        
        <label>Nombre del resultados</label>
        <input v-model="resultadosEditando.nombre" placeholder="Ej: Monitor de Signos Vitales" />
        
        <label>Marca</label>
        <input v-model="resultadosEditando.marca" placeholder="Ej: Philips" />
        
        <label>Modelo</label>
        <input v-model="resultadosEditando.modelo" placeholder="Ej: IntelliVue MX40" />
        
        <label>Serial</label>
        <input v-model="resultadosEditando.serial" placeholder="Ej: SN123456789" />
        
        <label>Ubicación</label>
        <select v-model="resultadosEditando.resultado" required>
          <option disabled value="">Seleccione una ubicación</option>
          <option 
            v-for="resultado in resultadoes" 
            :key="resultado.id" 
            :value="resultado.id"
          >
            {{ resultado.nombre }}
          </option>
        </select>
        
        <label>Responsable</label>
        <select v-model="resultadosEditando.responsable" required>
          <option disabled value="">Seleccione un responsable</option>
          <option 
            v-for="responsable in responsables" 
            :key="responsable.id" 
            :value="responsable.id"
          >
            {{ responsable.nombre }} {{ responsable.apellido }}
          </option>
        </select>

        <div class="modal-buttons">
          <button @click="guardarCambios" class="save-btn">Guardar Cambios</button>
          <button @click="cerrarModal" class="cancel-btn">Cancelar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      resultados: [],
      searchQuery: '',
      loading: false,
      error: null,
      mostrarModal: false,
      resultadosEditando: null,
      resultadoes: [],
      responsables: []
    }
  },
  created() {
    this.consultarResultados()
    this.consultarresultadoes()
    this.consultarResponsables()
  },
  computed: {
    resultadosFiltrados() {
      if (!this.searchQuery) return this.resultados
      const q = this.searchQuery.toLowerCase()
      return this.resultados.filter(e =>
        e.cod_ing_r?.toLowerCase().includes(q) ||
        e.cedula?.toLowerCase().includes(q)
      )
    }
  },
  methods: {
    async consultarResultados() {
      this.loading = true
      this.error = null
      try {
        const res = await fetch('http://127.0.0.1:8000/api/resultados/')
        if (!res.ok) throw new Error('Error al obtener resultados')
        const datos = await res.json()
        this.resultados = Array.isArray(datos) ? datos : []
      } catch (err) {
        console.error(err)
        this.error = 'Error al cargar los resultados'
        this.resultados = []
      } finally {
        this.loading = false
      }
    },

    async consultarresultadoes() {
      try {
        const res = await fetch('http://127.0.0.1:8000/api/pacientes/')
        this.resultadoes = await res.json()
      } catch (err) {
        console.error('Error al cargar resultadoes:', err)
        this.resultadoes = []
      }
    },

    async consultarResponsables() {
      try {
        const res = await fetch('http://127.0.0.1:8000/api/laboratoristas/')
        this.responsables = await res.json()
      } catch (err) {
        console.error('Error al cargar responsables:', err)
        this.responsables = []
      }
    },

    refrescarLista() {
      this.consultarResultados()
    },

    async eliminarResultado(id) {
      if (!confirm('¿Seguro que quieres eliminar este resultado?')) return
      try {
        const res = await fetch(`http://127.0.0.1:8000/api/labresults/${id}/`, {
          method: 'DELETE'
        })
        if (res.ok) {
          alert('Resultado eliminado correctamente')
          this.consultarResultados()
        } else {
          alert('Error al eliminar el resultado')
        }
      } catch (err) {
        console.error('Error al eliminar:', err)
        alert('Error al eliminar el resultado')
      }
    },

    abrirModalEditar(resultados) {
      this.resultadosEditando = { ...resultados }
      this.mostrarModal = true
    },
    cerrarModal() {
      this.mostrarModal = false
      this.resultadosEditando = null
    },

    async guardarCambios() {
      if (!this.resultadosEditando) return
      try {
        const res = await fetch(`http://127.0.0.1:8000/api/labresults/${this.resultadosEditando.id}/`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.resultadosEditando)
        })
        if (res.ok) {
          alert('Resultado actualizado correctamente')
          this.cerrarModal()
          this.consultarResultados()
        } else {
          alert('Error al actualizar el resultado')
        }
      } catch (err) {
        console.error('Error al actualizar:', err)
      }
    }
  }
}
</script>

<style scoped>
/* Copiar estilos de PersonalView.vue */
.page-container {
  display: flex;
  justify-content: center;
  align-items: first baseline;
  min-height: 100vh;
  /* background: #f5f7fa; */
  background: none;
  padding: 20px;
}
.dashboard-cards {
  display: grid;
  grid-template-columns: 1fr;
  max-width: 600px;
  width: 100%;
}
.card {
  background: rgba(255, 255, 255, 0.6);
  border-radius: 16px;
  padding: 25px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  border: 1px solid #e8ecf0;
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
.resultadoes-icon {
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: white;
}
.card-title h3 {
  font-size: 18px;
  font-weight: 600;
  margin: 0 0 5px 0;
  color: #2c3e50;
}
.card-title p {
  font-size: 14px;
  color: #7f8c8d;
  margin: 0;
  line-height: 1.4;
}
.search-input {
  width: 100%;
  padding: 12px;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  font-size: 14px;
  transition: all 0.2s ease;
  margin-bottom: 10px;
}
.search-input:focus {
  border-color: #667eea;
  outline: none;
  box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.3);
}
.refresh-btn,
.retry-btn {
  padding: 8px 16px;
  border: 1px solid #667eea;
  border-radius: 6px;
  background: white;
  color: #667eea;
  cursor: pointer;
  font-size: 13px;
  transition: all 0.2s ease;
}
.refresh-btn:hover,
.retry-btn:hover {
  background: #667eea;
  color: white;
}
.loading-state,
.error-state {
  text-align: center;
  padding: 20px;
  color: #7f8c8d;
}
.error-state {
  color: #e74c3c;
}
.resultadoes-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.results-count {
  font-size: 12px;
  color: #667eea;
  margin-bottom: 15px;
  font-weight: 500;
}
.no-results {
  text-align: center;
  padding: 30px;
  color: #7f8c8d;
}
.resultado-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #f8f9fa;
  border-radius: 10px;
  padding: 15px;
  transition: all 0.3s ease;
  border-left: 4px solid #667eea;
}
.resultado-item:hover {
  background: #e9ecef;
  transform: translateX(5px);
}
.resultado-info {
  flex: 1;
}
.resultado-nombre {
  font-weight: 600;
  color: #2c3e50;
  margin: 0 0 8px 0;
  font-size: 16px;
}
.resultado-detalle {
  font-size: 13px;
  color: #7f8c8d;
  margin: 0 0 5px 0;
}
.resultado-detalle strong {
  color: #667eea;
}
.acciones {
  display: flex;
  gap: 6px;
}
.edit-btn {
  background: #3498db;
  color: white;
  border: none;
  padding: 6px 12px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 12px;
}
.edit-btn:hover {
  background: #2980b9;
}
.delete-btn {
  background: #e74c3c;
  color: white;
  border: none;
  padding: 6px 12px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 12px;
}
.delete-btn:hover {
  background: #c0392b;
}

/* Modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}
.modal-content {
  background: #fff;
  padding: 20px;
  border-radius: 12px;
  width: 400px;
  max-width: 90%;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  max-height: 90vh;
  overflow-y: auto;
}
.modal-content h3 {
  margin-top: 0;
  color: #2c3e50;
}
.modal-content label {
  font-size: 13px;
  color: #7f8c8d;
  margin-top: 10px;
  display: block;
  font-weight: 500;
}
.modal-content input,
.modal-content select {
  width: 100%;
  padding: 8px;
  margin-top: 4px;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  font-size: 14px;
  box-sizing: border-box;
}
.modal-content input:focus,
.modal-content select:focus {
  border-color: #667eea;
  outline: none;
  box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
}
.modal-buttons {
  margin-top: 15px;
  display: flex;
  justify-content: flex-end;
  gap: 8px;
}
.cancel-btn {
  background: #95a5a6;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 13px;
}
.cancel-btn:hover {
  background: #7f8c8d;
}
.save-btn {
  background: #3498db;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 13px;
}
.save-btn:hover {
  background: #2980b9;
}

.btn {
  flex: 1;
  padding: 10px 14px;
  margin: 10px 50px;
  border: none;
  border-radius: 10px;
  font-weight: 600;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items:center;
  justify-content: center;
  gap: 6px;
  text-decoration: none;
}

.btn-primary {
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: white;
}
</style>