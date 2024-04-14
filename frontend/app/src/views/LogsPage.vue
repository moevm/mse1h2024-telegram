<script setup lang="ts">
import {useLogsStore} from "@/stores/logsStore";
import { ref, computed } from 'vue';
import type LogItem from "@/entities/LogEntity";

const logsStore = useLogsStore();
const logs = ref(logsStore.logs.data)

const itemsPerPage = ref(10);
const currentPage = ref(1);
const totalPages = computed(() => Math.ceil(logsList.value.length / itemsPerPage.value));

for(let i=0; i<30; i++)
{
  const log: LogItem = {
    date: '22.02.2024 04:22',
    level: 'INFO',
    text: 'test log log test log test log test log test log test log ',
    _id: `${i}`,
  }
  logsStore.logs.addLog(log)
}

const logsList = ref(logsStore.logs.data)
</script>

<template>
  <v-container style="width: 80%">
    <v-row justify="start">
      <v-col cols="12" md="10" sm="6">
        <v-table density="compact">
          <thead>
          <tr>
            <th class="text-center">
              Дата и время
            </th>
            <th class="text-center">
              Уровень
            </th>
            <th class="text-center">
              Текст лога
            </th>
          </tr>
          </thead>
          <tbody>
          <tr
              v-for="item in logs.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage)"
              :key="item._id"
          >
            <td class="text-table">{{ `${item.date}` }}</td>
            <td class="text-table">{{ `${item.level}` }}</td>
            <td class="text-table">{{ `${item.text}` }}</td>
          </tr>
          </tbody>
        </v-table>
        <v-pagination
            v-model="currentPage"
            :length="totalPages"
        ></v-pagination>
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
</style>