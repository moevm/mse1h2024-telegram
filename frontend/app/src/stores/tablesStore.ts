import { computed, ref } from 'vue';
import { defineStore } from 'pinia';
import axios from '@/config/defaultAxios';
import TableCreator from '@/models/TableModel';
import type TableItem from '@/entities/TableEntity';
import type Page from '@/entities/PageEntity';

export const useTablesStore = defineStore('tables', () => {
  const tables = ref(new TableCreator())

  const tablesCount = computed(() => tables.value.data.length)

  const getTables = async () => {
    axios.get('/tables').then((response) => {
      response.data.forEach((data: any) => {
        const table: TableItem = {
          id: data._id,
          name: data.name,
          link: data.table_id,
          provider: data.provider,
          updateFrequency: data.update_frequency,
          pages: data.pages
        }
        tables.value.addTable(table);
      });
    });
  }

  const postTable = async (table: TableItem) => {
    const body = {
      name: table.name,
      table_id: table.link,
      provider: table.provider,
      update_frequency: table.updateFrequency,
      pages: table.pages
    }
    axios.post('/tables', body).then((response) => {
      table.id = response.data._id;
      tables.value.addTable(table);
    });
  }

  const putTable = async (table: TableItem) => {
    axios.put(`/tables/${table.id}`, {
      params: {
        table_id: table.link,
        id: table.id,
        name: table.name,
        provider: table.provider,
        timer: table.updateFrequency
      }
    }).then((response) => {
      tables.value.changeTable(table);
    });
  }

  const deleteTable = async (table: TableItem) => {
    axios.delete(`/tables/${table.id}`, { 
      params: { 
        id: table.id 
      } 
    }).then((response) => {
      tables.value.removeTable(table);
    });
  }

  const setTableRule = async (table: TableItem, page: Page) => {
    axios.post(`/tables/${table.id}`, page, {
      params: {
        id: table.id
      }
    }).then((response) => {
      tables.value.addTableRule(table, page);
    });
  }

  const editTableRule = async (page: Page, tableId: String) => {
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

  return { 
    tables, 
    tablesCount, 
    getTables, 
    postTable, 
    putTable,
    deleteTable, 
    setTableRule, 
    editTableRule
  }
})