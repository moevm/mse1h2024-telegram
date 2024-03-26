import type TableItem from '../entities/TableEntity';

export default class TableCreator {
	data: TableItem[];
	
	constructor() {
		this.data = [];
	}

	addTable(table: TableItem) {
		this.data.push(table);
	}
}