export default interface Page {
  readonly id: string
  name: string
  teacherColumn: string
  columns: {
    column1: string
    column2: string
  }
  operator: string
  notification?: string
}
