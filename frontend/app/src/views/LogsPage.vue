<script setup lang="ts">
import { useLogsStore } from '@/stores/logsStore'
import { onMounted, ref, computed, type ComputedRef, type Ref } from 'vue'
import type LogItem from '@/entities/LogEntity'
import { mdiMagnify } from '@mdi/js'
import socket from '@/config/websocketService'

const logsStore = useLogsStore()

const itemsPerPage: Ref<number> = ref(10)
const currentPage: Ref<number> = ref(1)
const totalPages: ComputedRef<number> = computed(() => Math.ceil(logsList.value.data.length / itemsPerPage.value))

const items: string[] = ['INFO', 'ERROR']

onMounted(() => {
  socket.on('log', data => {
    data = JSON.parse(data)
    const log: LogItem = {
      date: data.date,
      level: data.level,
      text: data.text,
      _id: data.id
    }
    console.log(log)
    logsStore.logs.addLog(log)
  })
})

const logsList: Ref<{ data: LogItem[], backup: LogItem[], piece: string, level: string }> = ref(logsStore.logs)
logsStore.logs.reset()

const selected: Ref<string> = ref('')
const searchable: Ref<string> = ref('')
const filterList = () => {
  console.log(selected.value)
  if (selected.value == null) {
    selected.value = ''
  }
  if (searchable.value == null) {
    searchable.value = ''
  }
  if (selected.value != '' || searchable.value != '') {
    logsList.value.data = logsList.value.backup.filter(
      (item) =>
        item.level.indexOf(selected.value) != -1 && item.text.indexOf(searchable.value) != -1
    )
    currentPage.value = 1
  } else {
    logsList.value.data = logsList.value.backup
  }
  logsList.value.piece = searchable.value
  logsList.value.level = selected.value
}
</script>

<template>
  <v-container>
    <v-row justify="start">
      <v-col cols="12" md="10" sm="6">
        <v-row style="padding: 12px">
          <v-text-field
            v-model="searchable"
            :prepend-inner-icon="mdiMagnify"
            data-testid="search-logs"
            class="mx-auto"
            density="comfortable"
            clearable
            label="Поиск по тексту лога"
            style="max-width: 350px"
            theme="light"
            variant="solo"
            @update:modelValue="filterList"
          ></v-text-field>
          <v-select
            :items="items"
            data-testid="logs-filter-options"
            v-model="selected"
            density="comfortable"
            class="mx-auto"
            label="Фильтры"
            style="max-width: 200px"
            theme="light"
            variant="solo"
            clearable
            @update:modelValue="filterList"
          ></v-select>
        </v-row>
        <v-table density="compact" data-testid="logs-table">
          <thead>
            <tr>
              <th class="text-center">Дата и время</th>
              <th class="text-center">Уровень</th>
              <th class="text-center">Текст лога</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="item in logsList.data.slice(
                (currentPage - 1) * itemsPerPage,
                currentPage * itemsPerPage
              )"
              :key="item._id"
            >
              <td class="text-table">{{ `${item.date}` }}</td>
              <td class="text-table">{{ `${item.level}` }}</td>
              <td class="text-table">{{ `${item.text}` }}</td>
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
</style>
