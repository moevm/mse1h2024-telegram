<script setup lang="ts">
import { ref, computed } from 'vue';
import type TeacherItem from "@/entities/TeacherEntity";
import TeacherCreator from "@/models/TeacherModel";
import TableCreator from "@/models/TableModel";

const teachers = new TeacherCreator();

const itemsPerPage = ref(10);
const currentPage = ref(1);
const totalPages = computed(() => Math.ceil(teachers.data.length / itemsPerPage.value));

const teacher1: TeacherItem = {
  username: '@testusername1',
  aliases: 'Иванов Дмитрий Владимирович'
}

const teacher2: TeacherItem = {
  username: '@testusername2',
  aliases: 'Заславский Марк Маркович'
}

teachers.addTeacher(teacher1)
teachers.addTeacher(teacher2)
</script>

<template>
  <v-container style="width: 80%">
    <v-row justify="start">
      <v-col cols="12" md="10" sm="6">
        <v-table density="compact">
          <thead>
          <tr>
            <th class="text-center">
              Username
            </th>
            <th class="text-center">
              Aliases
            </th>
          </tr>
          </thead>
          <tbody>
          <tr
              v-for="item in teachers.data"
              :key="item.username"
          >
            <td class="text-table">{{ item.username }}</td>
            <td class="text-table">{{ item.aliases }}</td>
          </tr>
          </tbody>
        </v-table>
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