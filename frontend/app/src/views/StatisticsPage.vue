<script setup lang="ts">
import { useStatisticsStore } from '@/stores/statisticsStore'
import { onMounted, ref, computed, type ComputedRef, type Ref } from 'vue'
import type StatisticItem from '@/entities/StatisticEntity'
import { mdiMagnify } from '@mdi/js'
import socket from '@/config/websocketService'
</script>

<template>
  <v-container style="width: 80%">
    <v-row justify="start">
      <p>STATISTICS</p>
    </v-row>
  </v-container>
</template>

<style scoped>
.text-table {
  text-align: center !important;
  border: 1px solid lightgray !important;
}
th {
  background-color: rgb(228, 228, 228);
  border: 1px solid lightgray !important;
}
</style>