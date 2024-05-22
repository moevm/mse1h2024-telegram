<script setup lang="ts">
import { mdiChartTree } from '@mdi/js'
import { mdiAccountGroup } from '@mdi/js'
import { mdiBookOpenPageVariant } from '@mdi/js'
import { mdiChartBar } from '@mdi/js';
</script>

<template>
  <v-layout>
    <v-navigation-drawer permanent floating>
      <v-list nav>
        <v-list-item
          link
          :prepend-icon="mdiChartTree"
          title="Tables"
          data-testid="nav-admin-tables"
          to="/admin/tables"
          value="tables"
        ></v-list-item>
        <v-list-item
          link
          :prepend-icon="mdiAccountGroup"
          title="Teachers"
          data-testid="nav-admin-teachers"
          to="/admin/teachers"
          value="teachers"
        ></v-list-item>
        <v-list-item
          link
          :prepend-icon="mdiBookOpenPageVariant"
          title="Logs"
          data-testid="nav-admin-logs"
          to="/admin/logs"
          value="logs"
        ></v-list-item>
        <v-list-item
          link
          :prepend-icon="mdiChartBar"
          title="Statistics"
          data-testid="nav-admin-statistics"
          to="/admin/statistics"
          value="statistics"
        ></v-list-item>
      </v-list>
    </v-navigation-drawer>
  </v-layout>
</template>

<style scoped></style>
