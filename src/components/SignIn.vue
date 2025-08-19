<template>
  <div class="login-container">

    <img
      class="login-logo"
      src="../assets/edutk.png" alt="Logo EDUTK" 
    />
    <h1>Iniciar Sesión </h1>
    <form @submit.prevent="handleSignin">
      <div>
        <label for="email">Email</label>
        <input
          id="email"
          type="email"
          v-model.trim="email"
          placeholder="you@example.com"
          required
        />
      </div>

      <div>
        <label for="password">Password</label>
        <input
          id="password"
          type="password"
          v-model="password"
          placeholder="••••••••"
          required
        />
      </div>

      <div>
        <button type="submit" :disabled="loading">
          {{ loading ? "Ingresando..." : "Ingresar" }}
        </button>
      </div>
    </form>
  </div>
</template>


<script>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { supabase } from "../../supabase";

export default {
  setup() {
    const email = ref("");
    const password = ref("");
    const loading = ref(false);
    const router = useRouter();

    const handleSignin = async () => {
      if (!email.value || !password.value) {
        alert("Please enter both email and password.");
        return;
      }

      loading.value = true;
      try {
        const { data, error } = await supabase.auth.signInWithPassword({
          email: email.value,
          password: password.value
        });

        if (error) throw error;

        console.log("✅ Usuario logueado:", data.user);

        // Redirigir al inicio
        router.push("/");
      } catch (error) {
        console.error("❌ Error al iniciar sesión:", error.message);
        alert(error.message || "Error al iniciar sesión.");
      } finally {
        loading.value = false;
      }
    };

    return {
      email,
      password,
      loading,
      handleSignin,
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
  font-family: 'Great Vibes', cursive;
}

label {
  display: block;
  text-align: left;
  font-size: 1.0rem;
  font-weight: 500;
  color: #374151;
  margin-bottom: 0.4rem;
    font-family: 'Great Vibes', cursive;
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
  background: linear-gradient(to right, #06b5f8,#4f74f9);
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
