import type Pages from './PagesEntity';

export default interface TableItem {
	_id?: string;
	name: string;
	link: string;
	provider: string;
	update_frequency: number;
	pages: Pages[];
}