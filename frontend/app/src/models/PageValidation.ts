import { helpers, required } from '@vuelidate/validators'
import type { Rules } from './TableItemValidation'
import type { Ref } from 'vue'

export type PageState = {
  pageName: Ref<string>
  teacherColumn: Ref<string>
  column1: Ref<string>
  column2: Ref<string>
  operator: Ref<string | null> 
}

export default class PageValidation {
  private isColumn: any = helpers.regex(/^[A-Z]+$/)

  pageRules = (): Rules => {
    return {
      pageName: {
        required: helpers.withMessage('Название страницы не может быть пустым', required)
      },
      teacherColumn: {
        required: helpers.withMessage('Столбец не может быть пустым', required),
        isColumn: helpers.withMessage('Столбец указывается заглавной буквой', this.isColumn)
      },
      column1: {
        required: helpers.withMessage('Столбец не может быть пустым', required),
        isColumn: helpers.withMessage('Столбец указывается заглавной буквой', this.isColumn)
      },
      column2: {
        required: helpers.withMessage('Столбец не может быть пустым', required),
        isColumn: helpers.withMessage('Столбец указывается заглавной буквой', this.isColumn)
      },
      operator: {
        required: helpers.withMessage('Нужно выбрать оператор', required)
      }
    }
  }
}
