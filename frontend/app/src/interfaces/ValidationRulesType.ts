import type { ValidationRuleWithParams } from "@vuelidate/core"

export type ValidationRules = {
  [key: string]: ValidationRuleWithParams<object, any>
}

export type Rules = {
  [key: string]: ValidationRules
}