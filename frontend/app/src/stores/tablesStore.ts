import { computed, ref } from 'vue';
import { defineStore } from 'pinia';
import axios from '@/config/defaultAxios';
import TableCreator from '@/models/TableModel';
import type TableItem from '@/entities/TableEntity';

export const useTablesStore = defineStore('tables', () => {
  const tables = ref(new TableCreator())
  const tablesCount = computed(() => tables.value.data.length)

  const getTables = async () => {
    const response = await axios.get('/tables');
    response.data.forEach((table: TableItem) => {
      tables.value.addTable(table);
    });
  }

  const setTable = async (table: TableItem) => {
    await axios.post('/tables', table);
    tables.value.addTable(table);
  }

  return { tables, tablesCount, getTables, setTable }
})