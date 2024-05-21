<script setup lang="ts">
import { useStatisticsStore } from '@/stores/statisticsStore'
import { onMounted, ref, computed, type ComputedRef, type Ref } from 'vue'
import type StatisticItem from '@/entities/StatisticEntity'
import { mdiMagnify } from '@mdi/js'
import socket from '@/config/websocketService'

const statisticsStore = useStatisticsStore()

const itemsPerPage: Ref<number> = ref(10)
const currentPage: Ref<number> = ref(1)
const totalPages: ComputedRef<number> = computed(() => Math.ceil(statisticsList.value.data.length / itemsPerPage.value))

for(let i=0; i<10; i++){
  const data: StatisticItem = {
    _id: `${i}`,
    status: "SENDED",
    table_link: "string",
    teacher: "ABOLTUS",
    hash: "string",
    table_name: "string",
    created_at: "string",
    updated_at: "string",
  }
  statisticsStore.statistics.addStatistic(data)
}

const add = () => {
  const data: StatisticItem = {
    _id: `i`,
    status: "CONFIRMED",
    table_link: "string",
    teacher: "ABOLTUS",
    hash: "string",
    table_name: "string",
    created_at: "string",
    updated_at: "string",
  }
  statisticsStore.statistics.addStatistic(data)
}

onMounted(() => {
  // socket.on('log', data => {
  //   data = JSON.parse(data)
  //   const log: LogItem = {
  //     date: data.date,
  //     level: data.level,
  //     text: data.text,
  //     _id: data.id
  //   }
  //   console.log(log)
  //   logsStore.logs.addLog(log)
  // })
})

const statisticsList: Ref<{ data: StatisticItem[], sended: number, confirmed: number }> = ref(statisticsStore.statistics)
</script>

<template>
  <v-container style="width: 80%">
    <v-row justify="start">
      <v-col cols="12" md="10" sm="6">
        <v-btn @click="add"></v-btn>
        <h4>{{ `Всего отправлено уведомлений: ${statisticsList.sended}` }}</h4>
        <h4>{{ `Всего обработано уведомлений: ${statisticsList.confirmed}` }}</h4>
        <v-table class="table" density="compact" data-testid="teachers-table">
          <thead>
          <tr class="table-header">
            <th class="text-center" style="width: 60%">Ссылка</th>
            <th class="text-center" style="width: 20%">Преподаватель</th>
            <th class="text-center" style="width: 10%">Статус</th>
          </tr>
          </thead>
          <tbody>
          <tr class="table-data"
              v-for="item in statisticsList.data.slice(
                (currentPage - 1) * itemsPerPage,
                currentPage * itemsPerPage
              )"
              :key="item._id"
          >
            <td class="text-table" >
              <a class="link" :href="'https://t.me/BeBrrick'">Перейти</a>
            </td>
            <td class="text-table" >{{item.teacher}}</td>
            <td class="text-table">{{item.status}}</td>
          </tr>
          </tbody>
        </v-table>
        <v-pagination v-model="currentPage" :length="totalPages"></v-pagination>
      </v-col>
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
.link {
  color: dodgerblue;
  text-decoration: none;
}
</style>