<script setup lang="ts">
declare global {
  interface Window {
    onTelegramAuth: any;
  }
}

import { defineProps, defineEmits, onMounted, ref } from "vue"

const telegram = ref();
const script = document.createElement("script");
const emit = defineEmits(["callback"]);
const props = defineProps({
    size: {
        type: String,
        default: () => "large"
    },
    onAuth: {
        type: Function,
        default: () => {}
    },
    botName: {
        type: String,
        default: () => "ETUTestingBot"
    },
    requestAccess: {
        type: String,
        default: () => "write"
    }
});

function onTelegramAuth(user: any) {
    emit('callback', user);
}

window.onTelegramAuth = onTelegramAuth;

script.async = true;
script.src = "https://telegram.org/js/telegram-widget.js?22";
script.setAttribute("data-size", props.size);
script.setAttribute("data-telegram-login", props.botName);
script.setAttribute("data-request-access", props.requestAccess);
script.setAttribute("data-onauth", "window.onTelegramAuth(user)");

onMounted(() => {
    telegram.value.appendChild(script)
});
</script>

<template>
    <div id="telegramAuth" ref="telegram"></div>
</template>
