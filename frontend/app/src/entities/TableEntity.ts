import type Pages from './PagesEntity';

export default interface TableItem {
	name: string;
	link: string;
	provider: string;
	update_frequency: number;
	pages: Pages[];
}