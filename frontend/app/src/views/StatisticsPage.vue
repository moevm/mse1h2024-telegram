<script setup lang="ts">
import { useStatisticsStore } from '@/stores/statisticsStore'
import { onMounted, ref, computed, type ComputedRef, type Ref } from 'vue'
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import { Pie } from 'vue-chartjs'
import type StatisticItem from '@/entities/StatisticEntity'
import socket from '@/config/websocketService'

const statisticsStore = useStatisticsStore()

const itemsPerPage: Ref<number> = ref(8)
const currentPage: Ref<number> = ref(1)
const totalPages: ComputedRef<number> = computed(() => Math.ceil(statisticsList.value.data.length / itemsPerPage.value))

onMounted(() => {
  socket.on('statistic', data => {
    data = JSON.parse(data)
    const stat: StatisticItem = {
      _id: data.id,
      status: data.status,
      table_link: data.status,
      teacher: data.teacher,
      hash: data.hash,
      table_name: data.table_name,
      created_at: data.created_at,
      updated_at: data.updated_at,
    }
    statisticsStore.statistics.addStatistic(stat)
  })
})

const counters: ComputedRef<number[]> = computed(() => {
  console.log([statisticsList.value.confirmed, statisticsList.value.sended-statisticsList.value.confirmed])
  return [statisticsList.value.confirmed, statisticsList.value.sended-statisticsList.value.confirmed]
})

const statisticsList: Ref<{ data: StatisticItem[], sended: number, confirmed: number }> = ref(statisticsStore.statistics)

const data = computed(() => {
  return {
    labels: ['Отправлены и обработаны', 'Отправлены  необработаны'],
    datasets: [
      {
        backgroundColor: ['#008000', '#FF0000'],
        data: counters.value
      }
    ]
  }
})

const options = {
  responsive: true
}

ChartJS.register(ArcElement, Tooltip, Legend)


</script>

<template>
  <v-container style="width: 80%">
    <v-row justify="start">
      <v-col cols="12" md="10" sm="6">
        <v-row style="padding: 12px">
          <v-col style='max-width: 50%' cols="12" md="10" sm="2">
            <h4>{{ `Всего отправлено уведомлений: ${statisticsList.sended}` }}</h4>
            <h4>{{ `Всего обработано уведомлений: ${statisticsList.confirmed}` }}</h4>
          </v-col>
          <Pie style="max-width: 50%; max-height: 30vh" :data="data" :options="options" />
        </v-row>
        <v-table class="table" density="compact" data-testid="teachers-table">
          <thead>
          <tr class="table-header">
            <th class="text-center" style="width: 30%">Ссылка</th>
            <th class="text-center" style="width: 60%">Преподаватель</th>
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