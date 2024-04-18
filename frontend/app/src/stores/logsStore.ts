import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from '@/config/defaultAxios'
import type LogItem from '@/entities/LogEntity'
import LogCreator from '@/models/LogModel'

export const useLogsStore = defineStore('logs', () => {
  const logs = ref(new LogCreator())

  const getLogs = async () => {
    axios.get('/logs').then((response) => {
      response.data.forEach((log: LogItem) => {
        logs.value.addLog(log)
      })
    })
  }

  return {
    logs,
    getLogs
  }
})
