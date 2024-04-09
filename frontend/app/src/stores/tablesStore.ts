import { computed, ref } from 'vue';
import { defineStore } from 'pinia';
import axios from '@/config/defaultAxios';
import TableCreator from '@/models/TableModel';
import type TableItem from '@/entities/TableEntity';
import type Pages from '@/entities/PagesEntity';

export const useTablesStore = defineStore('tables', () => {
  const tables = ref(new TableCreator())

  const tablesCount = computed(() => tables.value.data.length)

  const getTables = async () => {
    axios.get('/tables').then((response) => {
      response.data.forEach((table: TableItem) => {
        tables.value.addTable(table);
      });
    });
  }

  const setTable = async (table: TableItem) => {
    axios.post('/tables', table).then((response) => {
      table._id = response.data._id;
    });
    tables.value.addTable(table);
  }

  const deleteTable = async (table: TableItem) => {
    axios.delete(`/tables/${table._id}`, { 
      params: { 
        id: table._id 
      } 
    }).then((response) => {
      tables.value.removeTable(table);
    });
  }

  const setTableRule = async (table: TableItem, page: Pages) => {
    axios.post(`/tables/${table._id}`, page, {
      params: {
        id: table._id
      }
    }).then((response) => {
      tables.value.addTableRule(table, page);
    });
  }

  const editTableRule = async (page: Pages, tableId: String) => {
    axios.put(`/table/${tableId}/${page.id}`, page.columns, {
      params: {
        t_id: tableId,
        p_id: page.id,
        new_name: page.name,
        t_col: page.teacher_column,
        rule: page.rule,
        text: page.notification_text
      }
    }).then((response) => {
      tables.value.changeTableRule(page, tableId);
    });
  }

  const editTable = async (table: TableItem) => {
    axios.put(`/tables/${table._id}`, {
      params: {
        id: table._id,
        name: table.name,
        table_id: table.table_id,
        provider: table.provider,
        timer: table.update_frequency
      }
    }).then((response) => {
      tables.value.changeTable(table);
    });
  }

  return { 
    tables, 
    tablesCount, 
    getTables, 
    setTable, 
    deleteTable, 
    setTableRule, 
    editTableRule,
    editTable
  }
})