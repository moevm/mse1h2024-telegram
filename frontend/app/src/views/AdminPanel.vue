<script setup lang="ts">
import { onMounted } from 'vue'
import { RouterView } from 'vue-router'
import RouteBar from '@/components/RouteBar.vue'
import { useTablesStore } from '@/stores/tablesStore'
import { useTeachersStore } from '@/stores/teachersStore'

const tablesStore = useTablesStore()
const teachersStore = useTeachersStore()

onMounted(() => {
  tablesStore.getTables()
  teachersStore.getTeachers()
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
