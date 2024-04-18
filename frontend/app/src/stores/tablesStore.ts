import { computed, ref, type ComputedRef, type Ref } from 'vue'
import { defineStore } from 'pinia'
import axios from '@/config/defaultAxios'
import TableCreator from '@/models/TableModel'
import type TableItem from '@/entities/TableEntity'
import type Page from '@/entities/PageEntity'

export const useTablesStore = defineStore('tables', () => {
  const tables: Ref<TableCreator> = ref(new TableCreator())

  const tablesCount: ComputedRef<number> = computed(() => tables.value.data.length)

  // GET /tables
  const getTables = async (): Promise<void> => {
    axios.get('/tables').then((response) => {
      response.data.forEach((data: any) => {
        const responsePages: Page[] = data.pages.reduceRight((pages: Page[], page: any) => {
          pages.push({
            id: page.id,
            name: page.name,
            teacherColumn: page.teacher_column,
            columns: {
              column1: page.column1,
              column2: page.column2
            },
            operator: page.comparison_operator,
            notification: page.notification_text
          })
          return pages
        }, [])
        const responseTable: TableItem = {
          id: data._id,
          name: data.name,
          link: data.table_id,
          provider: data.provider,
          updateFrequency: data.update_frequency,
          pages: responsePages
        }
        tables.value.addTable(responseTable)
      })
    })
  }

  // POST /tables
  const postTable = async (table: TableItem): Promise<void> => {
    const body: object = {
      name: table.name,
      table_id: table.link,
      provider: table.provider,
      update_frequency: table.updateFrequency,
      pages: table.pages
    }
    axios.post('/tables', body).then((response) => {
      const createdTable: TableItem = {
        id: response.data._id,
        name: response.data.name,
        link: response.data.table_id,
        provider: response.data.provider,
        updateFrequency: response.data.update_frequency,
        pages: response.data.pages
      }
      tables.value.addTable(createdTable)
    })
  }

  // PUT /tables/:id
  const putTable = async (table: TableItem): Promise<void> => {
    const requestPages: object[] = table.pages.reduce((pages: object[], page: Page) => {
      pages.push({
        id: page.id,
        name: page.name,
        teacher_column: page.teacherColumn,
        column1: page.columns.column1,
        column2: page.columns.column2,
        comparison_operator: page.operator,
        notification_text: page.notification
      })
      return pages
    }, [])
    const body: object = {
      _id: table.id,
      name: table.name,
      table_id: table.link,
      provider: table.provider,
      update_frequency: table.updateFrequency,
      pages: requestPages
    }
    axios.put(`/tables/${table.id}`, body).then((response) => {
      const changedTable: TableItem = {
        id: response.data._id,
        name: response.data.name,
        link: response.data.table_id,
        provider: response.data.provider,
        updateFrequency: response.data.update_frequency,
        pages: response.data.pages
      }
      tables.value.changeTable(changedTable)
    })
  }

  // DELETE /tables/:id
  const deleteTable = async (tableId: string): Promise<void> => {
    console.log(tableId)
    axios.delete(`/tables/${tableId}`).then((response) => {
      const responseTableId: string = response.data._id
      tables.value.removeTable(responseTableId)
    })
  }

  // POST /tables/:id
  const postTableRule = async (tableId: string, page: Page): Promise<void> => {
    const body: object = {
      id: page.id,
      name: page.name,
      teacher_column: page.teacherColumn,
      column1: page.columns.column1,
      column2: page.columns.column2,
      comparison_operator: page.operator,
      notification_text: page.notification === undefined ? '' : page.notification
    }
    axios.post(`/tables/${tableId}`, body).then((response) => {
      const lastPage: any = response.data.pages[response.data.pages.length - 1]
      const responsePage: Page = {
        id: lastPage.id,
        name: lastPage.name,
        teacherColumn: lastPage.teacher_column,
        columns: {
          column1: lastPage.column1,
          column2: lastPage.column2
        },
        operator: lastPage.comparison_operator,
        notification: lastPage.notification_text
      }
      const responseTableId: string = response.data._id
      tables.value.addTableRule(responseTableId, responsePage)
    })
  }

  // PUT /table/:id/:pageId
  const putTableRule = async (tableId: string, page: Page): Promise<void> => {
    const body: object = {
      id: page.id,
      name: page.name,
      teacher_column: page.teacherColumn,
      column1: page.columns.column1,
      column2: page.columns.column2,
      comparison_operator: page.operator,
      notification_text: page.notification === undefined ? '' : page.notification
    }
    axios.put(`/table/${tableId}/${page.id}`, body).then((response) => {
      const responsePage: any = response.data.pages.find(
        (iterationPage: any) => iterationPage.id === page.id
      )
      const changedPage: Page = {
        id: responsePage.id,
        name: responsePage.name,
        teacherColumn: responsePage.teacher_column,
        columns: {
          column1: responsePage.column1,
          column2: responsePage.column2
        },
        operator: responsePage.comparison_operator,
        notification: responsePage.notification_text
      }
      const responseTableId: string = response.data._id
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
