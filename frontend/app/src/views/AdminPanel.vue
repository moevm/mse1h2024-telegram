<script setup lang="ts">
import { onMounted } from 'vue';
import { RouterView } from 'vue-router';
import RouteBar from "@/components/RouteBar.vue";
import { useTablesStore } from '@/stores/tablesStore';
import { useTeachersStore } from "@/stores/teachersStore";
import axios from "@/config/defaultAxios";
import type TeacherItem from "@/entities/TeacherEntity";

const tablesStore = useTablesStore();
const teachersStore = useTeachersStore();


onMounted(() => {
  tablesStore.getTables();
  teachersStore.getTeachers();
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