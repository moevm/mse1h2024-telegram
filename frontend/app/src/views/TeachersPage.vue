<script setup lang="ts">
import { ref, computed } from 'vue';
import type TeacherItem from "@/entities/TeacherEntity";
import TeacherCreator from "@/models/TeacherModel";
import { mdiMagnify } from '@mdi/js';

const teachers = new TeacherCreator();

const itemsPerPage = ref(12);
const currentPage = ref(1);
const totalPages = computed(() => Math.ceil(teachersList.value.length / itemsPerPage.value));

const filterList = (searchable: string) => {
  if(searchable != '') {
    console.log(teachersData.value.filter((item) => item.aliases.indexOf(searchable) != -1));
    teachersList.value = teachersData.value.filter((item) => item.aliases.indexOf(searchable) != -1);
    currentPage.value = 1
  }
  else{
    console.log(teachersData.value)
    teachersList.value = teachersData.value;
  }
}

const teacher1: TeacherItem = {
  _id: 1,
  username: '@testusername1',
  aliases: 'Иванов Дмитрий Владимирович'
}

const teacher2: TeacherItem = {
  _id: 2,
  username: '@testusername2',
  aliases: 'Заславский Марк Маркович'
}

teachers.addTeacher(teacher1)
teachers.addTeacher(teacher2)

const teachersData = ref(teachers.data)
const teachersList = ref(teachers.data)

const items = ['Иванов Дмитрий Владимирович', 'Заславский Марк Маркович']
</script>

<template>
  <v-container style="width: 80%">
    <v-row justify="start">
      <v-col cols="12" md="10" sm="6">
        <v-autocomplete
            :items="items"
            :prepend-inner-icon="mdiMagnify"
            class="mx-auto"
            density="comfortable"
            menu-icon=""
            placeholder="Поиск преподавателей"
            style="max-width: 350px;"
            theme="light"
            variant="solo"
            auto-select-first
            item-props
            @update:search="filterList"
        ></v-autocomplete>
        <v-table density="compact">
          <thead>
          <tr>
            <th class="text-center">
              ФИО
            </th>
            <th class="text-center">
              Имя пользователя
            </th>
          </tr>
          </thead>
          <tbody>
          <tr
              v-for="item in teachersList.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage)"
              :key="item.username"
          >
            <td class="text-table">{{ item.aliases }}</td>
            <td class="text-table">{{ item.username }}</td>
          </tr>
          </tbody>
        </v-table>
        <v-pagination
            v-model="currentPage"
            :length="totalPages"
        ></v-pagination>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
.text-table {
  text-align: center !important;
  border: 1px solid lightgray !important;
}
.v-table {
  border: 1px solid gray !important;
  border-radius: 5px;
  overflow: hidden;
  font-size: medium;
  font-weight: 600;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
th {
  background-color: rgb(228, 228, 228);
  border: 1px solid lightgray !important;
}
</style>