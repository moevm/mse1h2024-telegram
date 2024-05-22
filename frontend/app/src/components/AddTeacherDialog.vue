<script setup lang="ts">
import { ref, defineEmits, type Ref } from 'vue'
import { useTeachersStore } from '@/stores/teachersStore'
import type TeacherItem from '@/entities/TeacherEntity'
import useVuelidate, { type Validation } from '@vuelidate/core'
import TeacherValidation, { type TeacherState } from '@/validation/TeacherValidation'
import type { Rules } from '@/interfaces/ValidationRulesType'

const teachersStore = useTeachersStore()

const emit = defineEmits(['close-dialog'])

const teacherNames: Ref<string> = ref('')
const teacherLogin: Ref<string> = ref('')

const teacherValidation: TeacherValidation = new TeacherValidation()
const rules: Rules = teacherValidation.teacherRules()
const state: TeacherState = {
  teacherNames,
  teacherLogin
}

const v$: Ref<Validation<Rules, TeacherState>> = useVuelidate(rules, state)

const confirm = async (): Promise<void> => {
  const resultValidation: boolean = await v$.value.$validate()
  if (!resultValidation) {
    return
  }
  const names_list: string[] = teacherNames.value
    .split('|')
    .map((name) => name.trim())
    .filter((item) => item != '')
  console.log(names_list)
  const teacher: TeacherItem = {
    names_list: names_list,
    telegram_login: teacherLogin.value.trim().slice(1)
  }
  teachersStore.postTeacher(teacher)
  emit('close-dialog')
}
</script>

<template>
  <v-card height="280" title="Добавление преподавателя">
    <v-card-text>
      <v-text-field
        v-model="teacherNames"
        clearable
        label="Список псевдонимов через |"
        :error-messages="v$.teacherNames.$error ? v$.teacherNames.$errors[0].$message : ''"
        required
        @input="v$.teacherNames.$touch"
      ></v-text-field>
      <v-text-field
        v-model="teacherLogin"
        clearable
        label="@login"
        :error-messages="v$.teacherLogin.$error ? v$.teacherLogin.$errors[0].$message : ''"
        required
        @input="v$.teacherNames.$touch"
      ></v-text-field>
      <v-row justify="end">
        <v-col cols="auto">
          <v-btn
            class="outlined-button"
            id="cancel-button"
            size="40px"
            variant="outlined"
            @click="$emit('close-dialog')"
          >
            Отмена
          </v-btn>
        </v-col>
        <v-col cols="auto">
          <v-btn
            class="outlined-button"
            id="confirm-button"
            size="40px"
            variant="outlined"
            @click="confirm"
          >
            Подтвердить
          </v-btn>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<style scoped>
#confirm-button {
  width: 150px !important;
  color: limegreen;
  letter-spacing: 0px !important;
}
#cancel-button {
  width: 100px !important;
  color: darkred;
  letter-spacing: 0px !important;
}
</style>
