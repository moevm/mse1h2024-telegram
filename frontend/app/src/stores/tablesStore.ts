import { computed, ref, type ComputedRef, type Ref } from 'vue'
import { defineStore } from 'pinia'
import type TableItem from '@/entities/TableEntity'
import type Page from '@/entities/PageEntity'
import type TablesStore from '@/interfaces/TableStoreType'
import type { DataTable, DataPage, TableResponseArray, TableResponse } from '@/transforms/TableItemTransformer'
import axios from '@/config/defaultAxios'
import TableCreator from '@/models/TableModel'
import TableItemTransformer from '@/transforms/TableItemTransformer'

const transform: TableItemTransformer = new TableItemTransformer()

export const useTablesStore: () => TablesStore = defineStore('tables', () => {
  const tables: Ref<TableCreator> = ref(new TableCreator())

  const tablesCount: ComputedRef<number> = computed(() => tables.value.data.length)

  // GET /tables
  const getTables = async (): Promise<void> => {
    axios.get('/tables').then((response: TableResponseArray) => {
      response.data.forEach((data: DataTable) => {
        const responseTable: TableItem = transform.convertToTableItem(data)
        tables.value.addTable(responseTable)
      })
    })
  }

  // POST /tables
  const postTable = async (table: TableItem): Promise<void> => {
    const body: DataTable = transform.convertToDataTable(table)
    axios.post('/tables', body).then((response: TableResponse) => {
      const responseTable: TableItem = transform.convertToTableItem(response.data)
      tables.value.addTable(responseTable)
    })
  }

  // PUT /tables/:id
  const putTable = async (table: TableItem): Promise<void> => {
    const body: DataTable = transform.convertToDataTable(table)
    axios.put(`/tables/${table.id}`, body).then((response: TableResponse) => {
      const responseTable: TableItem = transform.convertToTableItem(response.data)
      tables.value.changeTable(responseTable)
    })
  }

  // DELETE /tables/:id
  const deleteTable = async (tableId: string): Promise<void> => {
    axios.delete(`/tables/${tableId}`).then((response: TableResponse) => {
      const responseTableId: string = response.data._id!
      tables.value.removeTable(responseTableId)
    })
  }

  // POST /tables/:id
  const postTableRule = async (tableId: string, page: Page): Promise<void> => {
    const body: DataPage = transform.convertPageToDataPage(page)
    axios.post(`/tables/${tableId}`, body).then((response: TableResponse) => {
      const lastPage: DataPage = response.data.pages[response.data.pages.length - 1]
      const responsePage: Page = transform.convertDataPageToPage(lastPage)
      const responseTableId: string = response.data._id!
      tables.value.addTableRule(responseTableId, responsePage)
    })
  }

  // PUT /table/:id/:pageId
  const putTableRule = async (tableId: string, page: Page): Promise<void> => {
    const body: DataPage = transform.convertPageToDataPage(page)
    axios.put(`/table/${tableId}/${page.id}`, body).then((response: TableResponse) => {
      const responsePage: DataPage | undefined = response.data.pages.find(
        (iterationPage: DataPage) => iterationPage.id === page.id
      )
      const changedPage: Page = transform.convertDataPageToPage(responsePage!)
      const responseTableId: string = response.data._id!
      tables.value.changeTableRule(responseTableId, changedPage)
    })
  }

  // DELETE /table/:id/:pageId
  const deleteTableRule = async (tableId: string, pageId: string): Promise<void> => {
    axios.delete(`/tables/${tableId}/${pageId}`).then((response) => {
      // Response don't have deleted page id, so we need to pass it manually
      // ;)
      const responseTableId: string = response.data._id
      tables.value.removeTableRule(responseTableId, pageId)
    })
  }

  return {
    tables,
    tablesCount,
    getTables,
    postTable,
    putTable,
    deleteTable,
    postTableRule,
    putTableRule,
    deleteTableRule
  }
})
