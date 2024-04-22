<script setup lang="ts">
import { ref, computed } from 'vue'
import { mdiMagnify } from '@mdi/js'
import { useTeachersStore } from '@/stores/teachersStore'
import AddTeacherDialog from '@/components/AddTeacherDialog.vue'

const teachersStore = useTeachersStore()
const teachers = ref(teachersStore.teachers.data)

const itemsPerPage = ref(11)
const currentPage = ref(1)
const totalPages = computed(() => Math.ceil(teachersList.value.length / itemsPerPage.value))
const addTeacherDialog = ref(false)

const filterList = (searchable: string) => {
  if (searchable != ('' || null)) {
    teachersList.value = teachers.value.filter(
      (item) => item.names_list.join(" | ").indexOf(searchable) != -1
    )
    currentPage.value = 1
  } else {
    teachersList.value = teachers.value
  }
}

const teachersList = ref(teachersStore.teachers.data)

</script>

<template>
  <v-container style="width: 80%">
    <v-row justify="start">
      <v-col cols="12" md="10" sm="6">
        <v-dialog v-model="addTeacherDialog" max-width="450">
          <AddTeacherDialog @close-dialog="addTeacherDialog = false" />
        </v-dialog>
        <v-btn
          class="outlined-button"
          id="add-teacher-button"
          size="35px"
          prepend-icon="$plus"
          variant="outlined"
          @click="addTeacherDialog = true"
        >
          Добавить
        </v-btn>
        <v-text-field
            :prepend-inner-icon="mdiMagnify"
            class="mx-auto"
            density="comfortable"
            clearable
            label="Поиск преподавателей"
            style="max-width: 350px"
            theme="light"
            variant="solo"
            @update:modelValue="filterList"
        ></v-text-field>
        <v-table density="compact">
          <thead>
            <tr>
              <th class="text-center">ФИО</th>
              <th class="text-center">Имя пользователя</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="item in teachersList.slice(
                (currentPage - 1) * itemsPerPage,
                currentPage * itemsPerPage
              )"
              :key="item._id"
            >
              <td class="text-table" style="width: 70%">{{ `${item.names_list.join(" | ")}` }}</td>
              <td class="text-table" style="width: 30%">
                <a class="link" :href="`https://t.me/${item.telegram_login}`">{{
                  item.telegram_login
                }}</a>
              </td>
            </tr>
          </tbody>
        </v-table>
        <v-pagination v-model="currentPage" :length="totalPages"></v-pagination>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
.text-table {
  text-align: center !important;
  border: 1px solid lightgray !important;
}
th {
  background-color: rgb(228, 228, 228);
  border: 1px solid lightgray !important;
}
#add-teacher-button {
  width: 150px !important;
  color: limegreen;
  letter-spacing: 0px !important;
}
.link {
  color: dodgerblue;
  text-decoration: none;
}
</style>
