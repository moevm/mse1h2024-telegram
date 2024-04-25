import type { Rules } from '@/interfaces/ValidationRulesType'
import { helpers, integer, minValue, required } from '@vuelidate/validators'
import type { Ref } from 'vue'

export type TableItemState = {
  tableName: Ref<string>
  tableLink: Ref<string>
  tableUpdateSeconds: Ref<number | null>
}

export default class TableItemValidation {
  private isGoogleSheetId: any = helpers.regex(/^[\w-]{44}$/)

  tableItemRules = (): Rules => {
    return {
      tableName: {
        required: helpers.withMessage('Название таблицы не может быть пустым', required)
      },
      tableLink: {
        required: helpers.withMessage('ID таблицы не может быть пустым', required),
        isGoogleSheetId: helpers.withMessage('Неправильный ID таблицы', this.isGoogleSheetId)
      },
      tableUpdateSeconds: {
        required: helpers.withMessage('Частота обновления не может быть пустой', required),
        integer: helpers.withMessage('Частота обновления должна быть целым числом', integer),
        minValue: helpers.withMessage('Частота обновления должна быть больше 0', minValue(1))
      }
    }
  }
}
