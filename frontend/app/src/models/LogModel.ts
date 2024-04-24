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

  addLog(log: LogItem): void {
    if(log.text.indexOf(this.piece) != -1 && log.level == this.level) {
      this.data.push(log)
    }
    this.backup.push(log)
  }
}
