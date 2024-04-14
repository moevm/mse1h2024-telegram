import type Pages from './PagesEntity';

export default interface TableItem {
  _id?: string;
  name: string;
  table_id: string;
  update_frequency: number;
  pages: Pages[];
}