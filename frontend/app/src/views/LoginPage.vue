<script setup lang="ts">
import { ref, type Ref } from 'vue'
import SignInAdmin from '@/components/SignInAdmin.vue'

const signInDialog: Ref<boolean> = ref(false)
</script>

<template>
  <v-dialog v-model="signInDialog" max-width="20%">
    <SignInAdmin @close-dialog="signInDialog = false" />
  </v-dialog>
  <div id="centered-content">
    <h1 id="centered-text">Админ панель<br />Бота напоминаний</h1>
    <v-btn
      class="outlined-button"
      id="sign-in-button"
      size="40px"
      variant="outlined"
      @click="signInDialog = true"
      >Вход</v-btn
    >
  </div>
</template>

<style scoped>
#centered-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 85vh;
}
#centered-text {
  margin-bottom: 35px;
  text-align: center;
  font-weight: 470;
  font-family:
    system-ui,
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    Oxygen,
    Ubuntu,
    Cantarell,
    'Open Sans',
    'Helvetica Neue',
    sans-serif;
}
</style>
