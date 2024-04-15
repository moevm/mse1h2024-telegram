<<<<<<< HEAD
import type TeacherItem from "../entities/TeacherEntity";
=======
import type TeacherItem from '../entities/TeacherEntity';
>>>>>>> 0b583128bfe77ebe54a88a7a44e614543cc2985a

export default class TeacherCreator {
  data: TeacherItem[];

  constructor() {
    this.data = [];
  }

  addTeacher(teacher: TeacherItem) {
    this.data.push(teacher);
  }
}