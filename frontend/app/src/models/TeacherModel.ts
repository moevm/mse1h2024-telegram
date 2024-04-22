import type TeacherItem from '../entities/TeacherEntity'

export default class TeacherCreator {
  data: TeacherItem[]

  constructor() {
    this.data = []
  }

  addTeacher(teacher: TeacherItem) {
    this.data.push(teacher)
  }

  changeTeacher(teacher: TeacherItem): void {
    const existingTeacher: TeacherItem | undefined = this.data.find(
        (existingTeacher) => existingTeacher._id === teacher._id
    )
    if (existingTeacher) {
      existingTeacher.names_list = teacher.names_list
      existingTeacher.telegram_login = teacher.telegram_login
    }
  }

  removeTeacher(teacherId: string): void {
    this.data = this.data.filter((existingTeacher) => existingTeacher._id != teacherId)
  }
}
