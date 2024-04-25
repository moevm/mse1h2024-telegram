import type { Rules } from '@/interfaces/ValidationRulesType'
import { helpers, required } from '@vuelidate/validators'
import type { Ref } from 'vue'

export type PageState = {
  pageName: Ref<string>
  teacherColumn: Ref<string>
  column1: Ref<string>
  column2: Ref<string>
  operator: Ref<string | null>
}

export default class PageValidation {
  private isColumn: any = helpers.regex(/^[A-Z\u0410-\u042F\u0401]+$/)
  private isCorrectLength: any = helpers.regex(/^[\w\u0400-\u04FF]{1,3}$/)

  pageRules = (): Rules => {
    return {
      pageName: {
        required: helpers.withMessage('Название страницы не может быть пустым', required)
      },
      teacherColumn: {
        required: helpers.withMessage('Столбец не может быть пустым', required),
        isColumn: helpers.withMessage('Столбец указывается заглавной буквой', this.isColumn),
        isCorrectLength: helpers.withMessage(
          'Столбец должен быть длиной не более 3-х символов',
          this.isCorrectLength
        )
      },
      column1: {
        required: helpers.withMessage('Столбец не может быть пустым', required),
        isColumn: helpers.withMessage('Столбец указывается заглавной буквой', this.isColumn),
        isCorrectLength: helpers.withMessage(
          'Столбец должен быть длиной не более 3-х символов',
          this.isCorrectLength
        )
      },
      column2: {
        required: helpers.withMessage('Столбец не может быть пустым', required),
        isColumn: helpers.withMessage('Столбец указывается заглавной буквой', this.isColumn),
        isCorrectLength: helpers.withMessage(
          'Столбец должен быть длиной не более 3-х символов',
          this.isCorrectLength
        )
      },
      operator: {
        required: helpers.withMessage('Нужно выбрать оператор', required)
      }
    }
  }
}
