<script setup lang="ts">
import { ref, type Ref } from 'vue'
import SignInAdmin from '@/components/SignInAdmin.vue'

const signInDialog: Ref<boolean> = ref(false)
</script>

<template>
  <v-dialog id="sign-in-dialog" v-model="signInDialog" data-testid="sign-in-dialog" max-width="20%">
    <SignInAdmin @close-dialog="signInDialog = false" />
  </v-dialog>
  <div id="centered-content">
    <h1 id="centered-text">Админ панель<br />Бота напоминаний</h1>
    <v-btn
      class="outlined-button"
      data-testid="sign-in-button"
      id="sign-in-button"
      size="auto"
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
}
</style>
