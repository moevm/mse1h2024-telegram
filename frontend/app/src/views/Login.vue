<script setup lang="ts">
import axios from 'axios';
import TelegramLogin from '../components/TelegramLogin.vue';

function authenticateUser(user: any) {
    axios.get('http://localhost:8000/auth/login', {
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
            botName="Tet1ngbot"
            requestAccess="write"
            @callback="authenticateUser"
            id="telegramAuth"
        />
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
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
#telegramAuth {
    transform: scale(1.5);
}
</style>
