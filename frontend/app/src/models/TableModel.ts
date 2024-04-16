import type TableItem from "@/entities/TableEntity";
import type Page from "@/entities/PageEntity";

export default class TableCreator {
  data: TableItem[];

  constructor() {
    this.data = [];
  }

  addTable(table: TableItem): void {
    const exists: boolean = this.data.some(existingTable => existingTable.id === table.id);
    if (!exists) {
      this.data.unshift(table);
    }
  }

  changeTable(table: TableItem): void {
    const existingTable: TableItem | undefined = this.data.find(existingTable => existingTable.id === table.id);
    if (existingTable) {
      existingTable.name = table.name;
      existingTable.link = table.link;
      existingTable.provider = table.provider;
      existingTable.updateFrequency = table.updateFrequency
    }
  }

  addTableRule(tableId: string, page: Page): void {
    const existingTable: TableItem | undefined = this.data.find(existingTable => existingTable.id === tableId);
    if (existingTable) {
      existingTable.pages.unshift(page);
    }
  }

  changeTableRule(tableId: string, page: Page): void {
    const existingTable: TableItem | undefined = this.data.find(existingTable => existingTable.id === tableId);
    if (existingTable) {
      const existingPage: Page | undefined = existingTable.pages.find(existingPage => existingPage.id === page.id);
      if (existingPage) {
        existingPage.name = page.name;
        existingPage.teacherColumn = page.teacherColumn;
        existingPage.columns = page.columns;
        existingPage.operator = page.operator;
        existingPage.notification = page.notification;
      }
    }
  }

  removeTableRule(tableId: string, pageId: string): void {
    const existingTable: TableItem | undefined = this.data.find(existingTable => existingTable.id === tableId);
    if (existingTable) {
      existingTable.pages = existingTable.pages.filter(existingPage => existingPage.id !== pageId);
    }
  }

  removeTable(tableId: string): void {
    this.data = this.data.filter(existingTable => existingTable.id !== tableId);
  }
}