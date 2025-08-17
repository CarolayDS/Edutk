<template>
  <div>
    <h2>Sign in to your account</h2>
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
          {{ loading ? "Signing in..." : "Sign in" }}
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
