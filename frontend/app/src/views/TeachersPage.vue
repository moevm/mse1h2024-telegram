<script setup lang="ts">
import {ref, computed, type Ref, type ComputedRef} from 'vue'
import { mdiMagnify } from '@mdi/js'
import { useTeachersStore } from '@/stores/teachersStore'
import AddTeacherDialog from '@/components/AddTeacherDialog.vue'
import DeleteTeacherDialog from '@/components/DeleteTeacherDialog.vue'
import EditTeacherDialog from "@/components/EditTeacherDialog.vue";
import type TeacherItem from "@/entities/TeacherEntity";

const teachersStore = useTeachersStore()

const itemsPerPage: Ref<number> = ref(11)
const currentPage: Ref<number> = ref(1)
const totalPages: ComputedRef<number> = computed(() => Math.ceil(teachersList.value.data.length / itemsPerPage.value))
const addTeacherDialog: Ref<boolean> = ref(false)
const deleteTeacherDialog: Ref<boolean> = ref(false)
const editTeacherDialog: Ref<boolean> = ref(false)
const currentTeacher: Ref<TeacherItem> = ref({} as TeacherItem)
const searchable: Ref<string> = ref('')

const filterList = () => {
  if (searchable.value != ('' || null)) {
    teachersList.value.piece = searchable.value
    teachersList.value.data = teachersList.value.backup.filter(
      (item) => item.names_list.join(" | ").indexOf(searchable.value) != -1
    )
    currentPage.value = 1
  } else {
    teachersList.value.piece = ''
    teachersList.value.data = teachersList.value.backup
  }
}

const teachersList: Ref<{ data: TeacherItem[], backup: TeacherItem[], piece: string }> = ref(teachersStore.teachers)
teachersStore.teachers.reset()
</script>

<template>
  <v-container style="width: 80%">
    <v-row justify="start">
      <v-col cols="12" md="10" sm="6">
        <v-dialog v-model="addTeacherDialog" max-width="450">
          <AddTeacherDialog @close-dialog="addTeacherDialog = false" />
        </v-dialog>
        <v-dialog v-model="editTeacherDialog" max-width="450">
          <EditTeacherDialog :teacher="currentTeacher" @close-dialog="editTeacherDialog = false" />
        </v-dialog>
        <v-dialog v-model="deleteTeacherDialog" max-width="450">
          <DeleteTeacherDialog :teacher="currentTeacher" @close-dialog="deleteTeacherDialog = false" />
        </v-dialog>
        <v-btn
          class="outlined-button"
          id="add-teacher-button"
          data-testid="add-teacher-button"
          size="35px"
          prepend-icon="$plus"
          variant="outlined"
          @click="addTeacherDialog = true"
        >
          Добавить
        </v-btn>
        <v-text-field
            v-model="searchable"
            :prepend-inner-icon="mdiMagnify"
            data-testid="search-teachers"
            class="mx-auto"
            density="comfortable"
            clearable
            label="Поиск преподавателей"
            style="max-width: 350px"
            theme="light"
            variant="solo"
            @update:modelValue="filterList"
        ></v-text-field>
        <v-table class="table" density="compact" data-testid="teachers-table">
          <thead>
            <tr class="table-header">
              <th class="text-center" style="width: 60%">Псевдонимы</th>
              <th class="text-center" style="width: 20%">Имя пользователя</th>
              <th class="text-center" style="width: 10%">Изменение</th>
              <th class="text-center" style="width: 10%">Удаление</th>
            </tr>
          </thead>
          <tbody>
            <tr class="table-data"
              v-for="item in teachersList.data.slice(
                (currentPage - 1) * itemsPerPage,
                currentPage * itemsPerPage
              )"
              :key="item._id"
            >
              <td class="text-table" >{{ `${item.names_list.join(" | ")}` }}</td>
              <td class="text-table" >
                <a class="link" :href="`https://t.me/${item.telegram_login}`">{{
                  item.telegram_login
                }}</a>
              </td>
              <td class="text-table">
                <v-icon
                    id="edit-teacher-button"
                    icon="$edit"
                    @click="
                  editTeacherDialog = true;
                  currentTeacher = item;
                "
                >
                </v-icon>
              </td>
              <td class="text-table">
                <v-icon
                    id="delete-teacher-button"
                    icon="$delete"
                    @click="
                  deleteTeacherDialog = true;
                  currentTeacher = item;
                "
                >
                </v-icon>
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
#edit-teacher-button {
  color: rgb(238, 155, 0);
  letter-spacing: 0px !important;
}
#delete-teacher-button {
  color: darkred;
}
.link {
  color: dodgerblue;
  text-decoration: none;
}
</style>
