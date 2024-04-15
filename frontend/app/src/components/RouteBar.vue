<script setup lang="ts">
  import { mdiChartTree } from "@mdi/js"
  import { mdiAccountGroup } from "@mdi/js"
  import { mdiBookOpenPageVariant } from "@mdi/js"
</script>

<template>
  <div id="route-bar">
    <v-layout>
      <v-navigation-drawer permanent floating>
        <v-list nav>
          <v-list-item link :prepend-icon="mdiChartTree" title="Tables" to="/admin/tables" value="tables"></v-list-item>
          <v-list-item link :prepend-icon="mdiAccountGroup" title="Teachers" to="/admin/teachers" value="teachers"></v-list-item>
          <v-list-item link :prepend-icon="mdiBookOpenPageVariant" title="Logs" to="/admin/logs" value="logs"></v-list-item>
        </v-list>
      </v-navigation-drawer>
    </v-layout>
  </div>
</template>

<style scoped>
#route-bar{
  margin: 0;
  width: 20%;
  height: 90vh;
}
</style>