import type LogItem from '../entities/LogEntity'

export default class LogCreator {
  data: LogItem[]
  backup: LogItem[]
  piece: string
  level: string

  constructor() {
    this.data = []
    this.backup = []
    this.piece = ''
    this.level = ''
  }

  reset(): void {
    this.data = this.backup.slice()
    this.piece = ''
    this.level = ''
  }

  addLog(log: LogItem): void {
    if(log.text.indexOf(this.piece) != -1 && log.level.indexOf(this.level) != -1) {
      this.data.unshift(log)
    }
    this.backup.unshift(log)
  }
}
