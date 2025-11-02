<template>
  <div class="form-container">

    <div class="card-header">
      <div class="card-icon ubicaciones-icon">
        <span>📊</span>
      </div>
      <div class="card-title">
        <h3>Nuevo resultado laboratorio</h3>
        <p>Ingresar resultados de laboratorio de un paciente</p>
      </div>
    </div>


    <form @submit.prevent="enviarUbicacion">
      <div class="form-group">
        <label for="codigo">Codigo Ingreso:</label>
        <input type="text" id="codigo" v-model="form.codigo" required />
      </div>

      <div class="form-group">
        <label for="cedula">Cedula del paciente:</label>
        <input type="text" id="cedula" v-model="form.cedula" required />
      </div>

      <div class="form-group">
        <label for="col_total">Resultados Colesterol Total:</label>
        <input type="text" id="col_total" v-model="form.col_total" required />
      </div>

      <div class="form-group">
        <label for="col_rhdl">Resultados Colesterol HDL:</label>
        <input type="text" id="col_rhdl" v-model="form.col_rhdl" required />
      </div>

      <div class="form-group">
        <label for="col_rldl">Resultados Colesterol LDL:</label>
        <input type="text" id="col_rldl" v-model="form.col_rldl" required />
      </div>

      <div class="form-group">
        <label for="trigliceridos">Resultados Trigliceridos:</label>
        <input type="text" id="trigliceridos" v-model="form.trigliceridos" required />
      </div>

      <button type="submit" class="btn btn-primary">Guardar resultado</button>
    </form>

    <p v-if="mensaje" :class="{ 'success': exito, 'error': !exito }">
      {{ mensaje }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'NuevaUbicacion',
  data() {
    return {
      form: {
        codigo: '',
        nombre: '',
        ubicacion: '',
        telefono: ''
      },
      mensaje: '',
      exito: false
    }
  },
  methods: {
    async enviarUbicacion() {
      try {
        const respuesta = await fetch('http://localhost/pacientes/ubicaciones.php?insertar=1', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.form)
        });

        const datos = await respuesta.json();
        this.mensaje = datos.message || 'Sin mensaje';
        this.exito = datos.success === 1;

        if (this.exito) {
          // limpiar formulario
          this.form = { codigo: '', nombre: '', ubicacion: '', telefono: '' };
          // opcional: redirigir al listado de ubicaciones
          // this.$router.push('/ubicacion');
        }
      } catch (error) {
        console.error(error);
        this.mensaje = 'Error al conectar con el servidor';
        this.exito = false;
      }
    }
  }
}
</script>

<style scoped>
.form-container {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  margin-top: 25px;
  background: rgba(255, 255, 255, 0.6);
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  margin-bottom: 20px;
  color: #2c3e50;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
  color: #34495e;
}

input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
}

.btn {
  display: inline-block;
  width: 100%;
  padding: 10px;
  font-size: 16px;
  background-color: #667eea;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.btn:hover {
  background-color: #556cd6;
}

.success {
  color: green;
  text-align: center;
  margin-top: 10px;
}

.error {
  color: red;
  text-align: center;
  margin-top: 10px;
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
.ubicaciones-icon {
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: white;
}
.card-title h3 {
  font-size: 18px;
  font-weight: 600;
  margin: 0 0 5px 0;
  color: #2c3e50;
}
</style>