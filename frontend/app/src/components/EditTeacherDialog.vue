<script setup lang="ts">
import {defineEmits, defineProps, ref, type Ref} from 'vue'
import { useTeachersStore } from '@/stores/teachersStore'
import type TeacherItem from '@/entities/TeacherEntity'

const teachersStore = useTeachersStore()

const emit = defineEmits(['close-dialog'])

const props = defineProps<{
  teacher: TeacherItem
}>()

const confirm = (): void => {
  const names_list: string[] = namesList.value.split(", ")
  const teacher: TeacherItem = {
    _id: props.teacher._id,
    names_list: names_list,
    telegram_login: telegramLogin.value,
  }
  teachersStore.putTeacher(teacher)
  emit('close-dialog')
}

const namesList: Ref<string> = ref(props.teacher.names_list.join(", "))
const telegramLogin: Ref<string> = ref(props.teacher.telegram_login)
</script>

<template>
  <v-card height="280" title="Изменение преподавателя">
    <v-card-text>
      <v-text-field v-model="namesList" clearable label="Список псевдонимов через запятую" required></v-text-field>
      <v-text-field
          v-model="telegramLogin"
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