<script setup lang="ts">
import {defineEmits, defineProps} from 'vue'
import { useTeachersStore } from '@/stores/teachersStore'
import type TeacherItem from '@/entities/TeacherEntity'

const teachersStore = useTeachersStore()

const emit = defineEmits(['close-dialog'])

const props = defineProps<{
  teacher: TeacherItem
}>()

const confirm = (): void => {
  teachersStore.deleteTeacher(props.teacher._id)
  emit('close-dialog')
}
</script>

<template>
  <v-card height="230" title="Удаление преподавателя">
    <v-card-text>
      Вы уверены, что хотите удалить преподавателя: {{ props.teacher.telegram_login }}?<br />
      <strong
        >Данное действие необратимо, вся информация о преподавателе будет удалена.</strong
      >
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
              id="delete-button"
              size="40px"
              variant="outlined"
              @click="confirm"
          >
            Удалить
          </v-btn>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<style scoped>
strong {
  color: rgb(185, 34, 34);
}
#delete-button {
  width: 100px !important;
  color: darkred;
  letter-spacing: 0px !important;
  margin-top: 10px;
}
#cancel-button {
  width: 100px !important;
  color: gray;
  letter-spacing: 0px !important;
  margin-top: 10px;
}
</style>