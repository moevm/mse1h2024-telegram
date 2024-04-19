import type Page from './PageEntity'

export default interface TableItem {
  readonly id?: string
  name: string
  link: string
  provider: string
  updateFrequency: number
  pages: Page[]
}
