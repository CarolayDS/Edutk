<script setup>
defineProps({
  title: String,
  description: String,
  image: String,
  buttons: {
    type: Array,
    default: () => [],
  },
})
</script>

<template>
  <div class="custom-banner">
    <img :src="image" alt="Banner" class="banner-img" />

    <div class="banner-overlay">
      <div class="banner-content">
        <h1>{{ title }}</h1>
        <p>{{ description }}</p>

        <div v-if="buttons.length" class="banner-buttons">
          <template v-for="(btn, index) in buttons" :key="index">
            <!-- ROUTER LINK DENTRO DE LA PAGINA -->
            <RouterLink
              v-if="btn.to"
              :to="btn.to"
              class="banner-btn"
            >
              {{ btn.label }}
            </RouterLink>

            <!-- RUTA EXTERNA DE LA PAGINA -->
            <a
              v-else-if="btn.href"
              :href="btn.href"
              class="banner-btn"
              target="_blank"
              rel="noopener"
            >
              {{ btn.label }}
            </a>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped>
.custom-banner {
  position: relative;
  width: 100%;
  height: 350px;
  overflow: hidden;
  margin-bottom: 2rem;
  border-radius: 10px;
}

.banner-img {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 1;
  top: 0;
  left: 0;
}

.banner-overlay {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 2;
  background-color: rgba(0, 0, 0, 0.5);
  height: 100%;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  box-sizing: border-box;
}

.banner-content {
  color: #fff;
  text-align: center;
  max-width: 800px;
}

.banner-content h1 {
  font-size: 2.3rem;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.banner-content p {
  font-size: 1.1rem;
  
  line-height: 1.6;
}

.banner-buttons {
  margin-top: 1.5rem;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
}

.banner-btn {
  background-color: #ffffff;
  color: #0731c6;
  border: none;
  padding: 0.7rem 1.5rem;
  font-size: 1rem;
  font-weight: bold;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
}

.banner-btn:hover {
  background-color: #0731c6;
  color: #ffffff;
}

/* RESPONSIVO */
@media (max-width: 768px) {
  .custom-banner {
    height: 400px;
  }

  .banner-content h1 {
    font-size: 1.8rem;
  }

  .banner-content p {
    font-size: 1rem;
  }
}

@media (max-width: 480px) {
  .custom-banner {
    height: 420px;
  }

  .banner-content h1 {
    font-size: 1.5rem;
  }

  .banner-content p {
    font-size: 0.95rem;
  }

  .banner-btn {
    font-size: 0.9rem;
    padding: 0.6rem 1.2rem;
  }
}
</style>
