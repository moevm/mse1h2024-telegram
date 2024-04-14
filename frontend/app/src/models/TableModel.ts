import type TableItem from '@/entities/TableEntity';
import type Page from '@/entities/PageEntity';

export default class TableCreator {
  data: TableItem[];

  constructor() {
    this.data = [];
  }

  addTable(table: TableItem) {
    const exists = this.data.some(existingTable => existingTable.id === table.id);
    if (!exists) {
      this.data.unshift(table);
    }
  }

  addTableRule(table: TableItem, page: Page) {
    const existingTable = this.data.find(existingTable => existingTable.id === table.id);
    if (existingTable) {
      existingTable.pages.unshift(page);
    }
  }

  changeTableRule(page: Page, tableId: String) {
    const existingTable = this.data.find(existingTable => existingTable.id === tableId);
    if (existingTable) {
      const existingPage = existingTable.pages.find(existingPage => existingPage.id === page.id);
      if (existingPage) {
        existingPage.name = page.name;
        existingPage.teacher_column = page.teacher_column;
        existingPage.columns = page.columns;
        existingPage.rule = page.rule;
        existingPage.notification_text = page.notification_text;
      }
    }
  }

  changeTable(table: TableItem) {
    const existingTable = this.data.find(existingTable => existingTable.id === table.id);
    if (existingTable) {
      existingTable.name = table.name;
      existingTable.link = table.link;
      existingTable.provider = table.provider;
      existingTable.updateFrequency = table.updateFrequency
    }
  }

  removeTable(table: TableItem) {
    this.data = this.data.filter(existingTable => existingTable.id !== table.id);
  }
}