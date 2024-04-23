import type TeacherItem from '../entities/TeacherEntity'

export default class TeacherCreator {
  data: TeacherItem[]
  backup: TeacherItem[]
  piece: string

  constructor() {
    this.data = []
    this.backup = []
    this.piece = ''
  }

  addTeacher(teacher: TeacherItem): void {
    if(teacher.names_list.join(' | ').indexOf(this.piece) != -1) {
      this.data.push(teacher)
    }
    this.backup.push(teacher)
  }

  changeTeacher(teacher: TeacherItem): void {
    const existingTeacher: TeacherItem | undefined = this.data.find(
        (existingTeacher) => existingTeacher._id === teacher._id
    )
    if (existingTeacher) {
      existingTeacher.names_list = teacher.names_list
      existingTeacher.telegram_login = teacher.telegram_login
    }
    const existingTeacher2: TeacherItem | undefined = this.backup.find(
        (existingTeacher) => existingTeacher._id === teacher._id
    )
    if (existingTeacher2) {
      existingTeacher2.names_list = teacher.names_list
      existingTeacher2.telegram_login = teacher.telegram_login
    }
  }

  removeTeacher(teacherId: string): void {
    this.data = this.data.filter((existingTeacher) => existingTeacher._id != teacherId)
    this.backup = this.backup.filter((existingTeacher) => existingTeacher._id != teacherId)
  }
}
