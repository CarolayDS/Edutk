<template>
  <div>
    <h2>Sign up for an account</h2>
    <form @submit.prevent="handleSignup">
      <div>
        <label for="email">Email</label>
        <input id="email" type="email" v-model="email" required />
      </div>
      <div>
        <label for="password">Password</label>
        <input id="password" type="password" v-model="password" required minlength="6" />
      </div>
      <div>
        <button type="submit">Sign up</button>
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
