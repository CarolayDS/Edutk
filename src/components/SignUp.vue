<template>
  <div class="login-container"s>
    <img
      class="login-logo"
      src="../assets/edutk.png" alt="Logo EDUTK" 
    />
    <h1>Regístrese para obtener una cuenta</h1>
    <form @submit.prevent="handleSignup">
      <div>
        <label for="email">Correo</label>
        <input id="email" type="email" v-model="email" required />
      </div>
      <div>
        <label for="password">Contraseña</label>
        <input id="password" type="password" v-model="password" required minlength="6" />
      </div>
      <div>
        <button type="submit">Registrarse</button>
      </div>
    </form>
  </div>
</template>

<script>
import { ref } from "vue";
import { supabase } from "../../supabase";

export default {
  setup() {
    const email = ref("");
    const password = ref("");

    const handleSignup = async () => {
      try {
        // Validaciones antes de enviar
        if (!email.value || !password.value) {
          alert("Por favor ingresa un email y contraseña.");
          return;
        }

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email.value)) {
          alert("Por favor ingresa un email válido.");
          return;
        }

        if (password.value.length < 6) {
          alert("La contraseña debe tener al menos 6 caracteres.");
          return;
        }

        const { data, error } = await supabase.auth.signUp({
          email: email.value,
          password: password.value,
        });

        if (error) throw error;

        alert("Registro exitoso. Revisa tu correo para confirmar tu cuenta.");
        console.log("Usuario registrado:", data.user);
      } catch (error) {
        alert(error.error_description || error.message);
      }
    };

    return {
      email,
      password,
      handleSignup,
    };
  },
};
</script>


<style scoped>
.login-container {
  max-width: 400px;
  margin: 2rem auto;   
  padding: 2.8rem;    
  background: #ffffff;
  border-radius: 1rem;
  box-shadow: 0 8px 35px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.login-logo {
  width: 280px;
  margin: 0 auto 1.2rem;
  display: block;
  filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.15));
}

h1 {
  font-size: 1.6rem;
  font-weight: bold;
  color: #06b5f8;
  margin-bottom: 1.8rem;
}

label {
  display: block;
  text-align: left;
  font-size: 1.0rem;
  font-weight: 500;
  color: #374151;
  margin-bottom: 0.4rem;
}

input {
  width: 90%;
  padding: 0.8rem 1rem;
  border: 1px solid #d1d5db;
  border-radius: 0.6rem;
  outline: none;
  transition: all 0.2s;
  font-size: 0.95rem;
  margin-bottom: 1.2rem;
}
input:focus {
  border-color: #06b5f8;
  box-shadow: 0 0 0 3px rgba(6, 181, 248, 0.25);
}

button {
  width: 100%;
  padding: 0.9rem;
  border: none;
  border-radius: 0.6rem;
  background: linear-gradient(to right, #06b5f8, #5878ee);
  color: white;
  font-weight: bold;
  font-size: 1rem;
  cursor: pointer;
  transition: 0.2s;
}
button:hover {
  opacity: 0.9;
}
button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>

