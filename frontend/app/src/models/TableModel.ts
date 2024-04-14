import type TableItem from '@/entities/TableEntity';
import type Page from '@/entities/PageEntity';

export default class TableCreator {
  data: TableItem[];

  constructor() {
    this.data = [];
  }

  addTable(table: TableItem) {
    const exists = this.data.some(existingTable => existingTable._id === table._id);
    if (!exists) {
      this.data.unshift(table);
    }
  }

  addTableRule(table: TableItem, page: Page) {
    const existingTable = this.data.find(existingTable => existingTable._id === table._id);
    if (existingTable) {
      existingTable.pages.unshift(page);
    }
  }

  changeTableRule(page: Page, tableId: String) {
    const existingTable = this.data.find(existingTable => existingTable._id === tableId);
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
    const existingTable = this.data.find(existingTable => existingTable._id === table._id);
    if (existingTable) {
      existingTable.name = table.name;
      existingTable.table_id = table.table_id;
      existingTable.update_frequency = table.update_frequency
    }
  }

  removeTable(table: TableItem) {
    this.data = this.data.filter(existingTable => existingTable._id !== table._id);
  }
}