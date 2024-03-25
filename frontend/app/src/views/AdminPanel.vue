<script setup lang="ts">
import { RouterView } from 'vue-router'
import RouteBar from "@/components/RouteBar.vue"
</script>

<template>
  <div style="margin: 0; display: flex; height: 100%">
    <RouteBar></RouteBar>
    <RouterView />
  </div>
</template>

<style scoped>
</style>