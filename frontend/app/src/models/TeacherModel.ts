import type TeacherItem from '../entities/TeacherEntity'

export default class TeacherCreator {
  data: TeacherItem[]

  constructor() {
    this.data = []
  }

  addTeacher(teacher: TeacherItem) {
    this.data.push(teacher)
  }
}
