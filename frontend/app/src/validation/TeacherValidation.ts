import { helpers, required } from '@vuelidate/validators'
import type { Rules } from '@/interfaces/ValidationRulesType'
import type { Ref } from 'vue'

export type TeacherState = {
  teacherNames: Ref<string>
  teacherLogin: Ref<string>
}

export default class TeacherValidation {
  private isNameList: any = helpers.regex(/^(\s*[^|\s]\s*)+(\|\s*[^|]+\s*)*$/)
  private isLogin: any = helpers.regex(/^@\w+$/)

  teacherRules = (): Rules => {
    return {
      teacherNames: {
        required: helpers.withMessage('Псевдоним не может быть пустым', required),
        isNameList: helpers.withMessage('Неправильно задан список', this.isNameList)
      },
      teacherLogin: {
        required: helpers.withMessage('Логин не может быть пустым', required),
        isLogin: helpers.withMessage('Неправильно задан логин', this.isLogin)
      }
    }
  }
}
