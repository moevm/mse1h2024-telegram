import type TableItem from '@/entities/TableEntity';
import type Pages from '@/entities/PagesEntity';

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

	addTableRule(table: TableItem, page: Pages) {
		const existingTable = this.data.find(existingTable => existingTable._id === table._id);
		if (existingTable) {
			existingTable.pages.unshift(page);
		}
	}

	changeTableRule(page: Pages, tableId: String) {
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
			existingTable.link = table.link;
			existingTable.provider = table.provider;
			existingTable.update_frequency = table.update_frequency
		}
	}

	removeTable(table: TableItem) {
		this.data = this.data.filter(existingTable => existingTable._id !== table._id);
	}
}