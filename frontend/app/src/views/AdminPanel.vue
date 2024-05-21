<script setup lang="ts">
import { onMounted } from 'vue'
import { RouterView } from 'vue-router'
import RouteBar from '@/components/RouteBar.vue'
import { useTablesStore } from '@/stores/tablesStore'
import { useTeachersStore } from '@/stores/teachersStore'
import { useLogsStore } from "@/stores/logsStore";
import { useStatisticsStore } from "@/stores/statisticsStore";

const tablesStore = useTablesStore()
const teachersStore = useTeachersStore()
const logsStore = useLogsStore()
const statisticsStore = useStatisticsStore()

onMounted(() => {
  tablesStore.getTables()
  teachersStore.getTeachers()
  logsStore.getLogs()
  statisticsStore.getStatistics()
})
</script>

<template>
  <div id="admin-panel">
    <RouteBar></RouteBar>
    <RouterView />
  </div>
</template>

<style scoped>
#admin-panel {
  margin: 0;
  display: flex;
  height: 100%;
}
</style>
