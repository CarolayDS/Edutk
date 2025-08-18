<template>
  <div>
    <sign-up v-if="isSignUp" />
    <sign-in v-else />
    <button @click="isSignUp = !isSignUp">
      {{
        isSignUp
          ? "¿Ya tienes una cuenta? Inicia sesión."
          : "¿Aún no tienes una cuenta? Regístrate."
      }}
    </button>
  </div>
</template>

<script>
import { ref } from "vue";
import SignUp from "./SignUp.vue";
import SignIn from "./SignIn.vue";
export default {
  components: { SignUp, SignIn },
  setup() {
    const isSignUp = ref(true);

    return {
      isSignUp,
    };
  },
};
</script>

<style scoped>
button {
  width: 400px; 
  padding: 0.9rem;
  border: none;
  border-radius: 0.6rem;
  background: linear-gradient(to left, #06b5f8, #5878ee);
  color: white;
  font-weight: bold;
  font-size: 1rem;
  cursor: pointer;
  transition: 0.2s;
  display: block;        
  margin: 0.4rem auto 0;
}


button:hover {
  opacity: 0.9;
}
button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}



</style>