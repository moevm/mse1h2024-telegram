<script setup lang="ts">
import { ref, defineEmits, type Ref } from 'vue'
import { useTeachersStore } from '@/stores/teachersStore'
import type TeacherItem from '@/entities/TeacherEntity'

const teachersStore = useTeachersStore()

const emit = defineEmits(['close-dialog'])

//- Данные ------------------------------------------------------
const teacherName: Ref<string> = ref('')
const teacherPatronymic: Ref<string> = ref('')
const teacherSurname: Ref<string> = ref('')
const teacherLogin: Ref<string> = ref('')
const teacherRole: Ref<string> = ref('')
const roles: Ref<string[]> = ref(['ADMIN', 'TEACHER'])
//---------------------------------------------------------------

const confirm = (): void => {
  const teacher: TeacherItem = {
    name: teacherName.value,
    patronymic: teacherPatronymic.value,
    surname: teacherSurname.value,
    telegram_login: teacherLogin.value,
    role: teacherRole.value
  }
  teachersStore.putTeacher(teacher)
  emit('close-dialog')
}
</script>

<template>
  <v-card height="510" title="Добавление таблицы">
    <v-card-text>
      <v-text-field v-model="teacherName" clearable label="Имя" required></v-text-field>
      <v-text-field v-model="teacherPatronymic" clearable label="Отчество" required></v-text-field>
      <v-text-field v-model="teacherSurname" clearable label="Фамилия" required></v-text-field>
      <v-text-field
        v-model="teacherLogin"
        clearable
        label="Логин преподавателя в телеграме"
        required
      ></v-text-field>
      <v-select v-model="teacherRole" clearable label="Роль" :items="roles" required></v-select>
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
.v-card {
  text-align: center;
  font-family:
    system-ui,
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    Oxygen,
    Ubuntu,
    Cantarell,
    'Open Sans',
    'Helvetica Neue',
    sans-serif;
}
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
