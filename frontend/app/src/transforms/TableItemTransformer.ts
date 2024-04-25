import type Page from "@/entities/PageEntity"
import type TableItem from "@/entities/TableEntity"

export type DataTable = {
  _id?: string
  name: string
  table_id: string
  provider: string
  update_frequency: number
  pages: DataPage[]
}

export type DataPage = {
  id: string
  name: string
  teacher_column: string
  column1: string
  column2: string
  comparison_operator: string
  notification_text: string
}

export type TableResponseArray = {
  data: DataTable[]
}

export type TableResponse = {
  data: DataTable
}

export default class TableItemTransformer {
  convertDataPageToPage = (page: DataPage): Page => {
    return {
      id: page.id,
      name: page.name,
      teacherColumn: page.teacher_column,
      columns: {
        column1: page.column1,
        column2: page.column2
      },
      operator: page.comparison_operator,
      notification: page.notification_text === undefined ? '' : page.notification_text
    }
  }

  convertToPage = (data: DataPage[] | DataPage): Page[] | Page => {
    if (Array.isArray(data)) {
      return data.map(this.convertDataPageToPage)
    } else {
      return this.convertDataPageToPage(data)
    }
  }

  convertToTableItem = (data: DataTable): TableItem => {
    const page: any = this.convertToPage(data.pages)
    return {
      id: data._id,
      name: data.name,
      link: data.table_id,
      provider: data.provider,
      updateFrequency: data.update_frequency,
      pages: Array.isArray(page) ? page : [page]
    }
  }

  convertPageToDataPage = (page: Page): DataPage => {
    return {
      id: page.id,
      name: page.name,
      teacher_column: page.teacherColumn,
      column1: page.columns.column1,
      column2: page.columns.column2,
      comparison_operator: page.operator,
      notification_text: page.notification === undefined ? '' : page.notification
    }
  }

  convertToDataPage = (data: Page[] | Page): DataPage[] | DataPage => {
    if (Array.isArray(data)) {
      return data.map(this.convertPageToDataPage)
    } else {
      return this.convertPageToDataPage(data)
    }
  }

  convertToDataTable = (data: TableItem): DataTable => {
    const pages: any = this.convertToDataPage(data.pages)
    return {
      name: data.name,
      table_id: data.link,
      provider: data.provider,
      update_frequency: data.updateFrequency,
      pages: Array.isArray(pages) ? pages : [pages]
    }
  }
}
