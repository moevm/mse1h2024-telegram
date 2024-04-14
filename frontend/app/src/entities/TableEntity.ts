import type Page from './PageEntity';

export default interface TableItem {
  _id?: string;
  name: string;
  table_id: string;
  update_frequency: number;
  pages: Page[];
}