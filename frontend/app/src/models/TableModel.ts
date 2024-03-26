import type TableItem from '../entities/TableEntity';

export default class TableCreator {
	data: TableItem[];
	
	constructor() {
		this.data = [];
	}

	addTable(table: TableItem) {
		const exists = this.data.some(existingTable => existingTable._id === table._id);
		if (!exists) {
			this.data.push(table);
		}
	}
}