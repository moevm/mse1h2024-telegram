<script setup lang="ts">
<<<<<<< HEAD
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "@/config/defaultAxios";
import TelegramLogin from "@/components/TelegramLogin.vue";

const router = useRouter();
const errorMessage = ref("");
const botName = ref(import.meta.env.VITE_TELEGRAM_BOT_NAME);

async function authenticateUser(user: any) {
  await axios.get("/auth/login", {
=======
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from '@/config/defaultAxios';
import TelegramLogin from '@/components/TelegramLogin.vue';

const router = useRouter();
const errorMessage = ref('');
const botName = ref(import.meta.env.VITE_TELEGRAM_BOT_NAME);

async function authenticateUser(user: any) {
  await axios.get('/auth/login', {
>>>>>>> 0b583128bfe77ebe54a88a7a44e614543cc2985a
    withCredentials: true,
    params: {
      id: user.id,
      first_name: user.first_name,
      last_name: user.last_name,
      username: user.username,
      photo_url: user.photo_url,
      auth_date: user.auth_date,
      hash: user.hash
    }
    }).then((response) => {
<<<<<<< HEAD
      router.push("/admin");
=======
      router.push('/admin');
>>>>>>> 0b583128bfe77ebe54a88a7a44e614543cc2985a
    }).catch((error) => {
      errorMessage.value = `Error: ${error.response.status} ${error.response.statusText}`;
  });
}
</script>

<template>
  <div id="centered-content">
    <h1 id="centered-text">
      Админ панель<br/>Бота напоминаний
    </h1>
    <TelegramLogin
      size="large"
      :bot-name="botName"
      requestAccess="write"
      @callback="authenticateUser"
      id="telegramAuth" />
    <p id="error">{{ errorMessage }}</p>
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
  margin-bottom: 50px;
  text-align: center;
  font-weight: 470;
<<<<<<< HEAD
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
=======
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
>>>>>>> 0b583128bfe77ebe54a88a7a44e614543cc2985a
}
#telegramAuth {
  transform: scale(1.5);
}
#error {
  margin-top: 15px;
  color: darkred;
  font-weight: 600;
  font-size: medium;
}
</style>
