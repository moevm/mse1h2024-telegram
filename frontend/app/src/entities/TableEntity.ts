import type Page from './PageEntity';

export default interface TableItem {
  id?: string;
  name: string;
  link: string;
  provider: string;
  updateFrequency: number;
  pages: Page[];
}