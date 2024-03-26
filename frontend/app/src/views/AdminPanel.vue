<script setup lang="ts">
import { onMounted } from 'vue';
import { RouterView } from 'vue-router';
import RouteBar from "@/components/RouteBar.vue";
import { useTablesStore } from '@/stores/tablesStore';

const tablesStore = useTablesStore();

onMounted(() => {
  tablesStore.getTables();
});
</script>

<template>
  <div style="margin: 0; display: flex; height: 100%">
    <RouteBar></RouteBar>
    <RouterView />
  </div>
</template>

<style scoped>
</style>