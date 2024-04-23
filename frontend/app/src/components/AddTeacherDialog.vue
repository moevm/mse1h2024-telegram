<script setup lang="ts">
import { ref, defineEmits, type Ref } from 'vue'
import { useTeachersStore } from '@/stores/teachersStore'
import type TeacherItem from '@/entities/TeacherEntity'

const teachersStore = useTeachersStore()

const emit = defineEmits(['close-dialog'])

//- Данные ------------------------------------------------------
const teacherNames: Ref<string> = ref('')
const teacherLogin: Ref<string> = ref('')
//---------------------------------------------------------------

const confirm = (): void => {
  const names_list: string[] = teacherNames.value.split("|").map(name => name.trim()).filter((item) => item != '')
  console.log(names_list)
  const teacher: TeacherItem = {
    names_list: names_list,
    telegram_login: teacherLogin.value.trim(),
  }
  teachersStore.postTeacher(teacher)
  emit('close-dialog')
}
</script>

<template>
  <v-card height="280" title="Добавление преподавателя">
    <v-card-text>
      <v-text-field v-model="teacherNames" clearable label="Список псевдонимов через |" required></v-text-field>
      <v-text-field
        v-model="teacherLogin"
        clearable
        label="@login"
        required
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
