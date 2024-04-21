import type Page from '@/entities/PageEntity'
import type TableItem from '@/entities/TableEntity'
import type TableCreator from '@/models/TableModel'

export default interface TablesStore {
  tables: TableCreator
  tablesCount: number
  getTables: () => Promise<void>
  postTable: (table: TableItem) => Promise<void>
  putTable: (table: TableItem) => Promise<void>
  deleteTable: (tableId: string) => Promise<void>
  postTableRule: (tableId: string, page: Page) => Promise<void>
  putTableRule: (tableId: string, page: Page) => Promise<void>
  deleteTableRule: (tableId: string, pageId: string) => Promise<void>
}
