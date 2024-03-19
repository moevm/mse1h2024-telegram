<script setup lang="ts">
  import { mdiChartTree } from '@mdi/js'
  import { mdiAccountGroup } from '@mdi/js'
  import { mdiBookOpenPageVariant } from '@mdi/js'
</script>

<template>
  <div style="margin: 0; width: 20%; height: 90vh">
    <router-link to="/">
      <v-btn flat depressed style="width: 100%; height: 50px;"><v-icon style="width: 30px; height: 30px; margin-left: 0" :icon="mdiChartTree"/><p>Таблицы</p></v-btn>
    </router-link>
    <router-link to="/teachers">
      <v-btn flat depressed style="width: 100%; height: 50px;"><v-icon style="width: 30px; height: 30px" :icon="mdiAccountGroup"/>Преподаватели</v-btn>
    </router-link>
    <router-link to="/logs">
      <v-btn flat depressed style="width: 100%; height: 50px;"><v-icon style="width: 30px; height: 30px" :icon="mdiBookOpenPageVariant"/>Логи</v-btn>
    </router-link>
  </div>
</template>

<style scoped>
</style>