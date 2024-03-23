<script setup lang="ts">
import { ref } from 'vue';
import type TableItem from '@/entities/TableEntity';
import TableCreator from '@/models/TableModel';
import TablePanel from '@/views/TablesPanel.vue';
import AddTableDialog from '@/components/AddTableDialog.vue';

const tables = new TableCreator();

// Тестовая таблица
//-------------------------------------
const table1: TableItem = {
  _id: "1",
  name: "Тест таблица",
  link: "Google Sheets Link 1",
  provider: "Google",
  update_frequency: 1,
  pages: [ 
    {
      id: "1",
      name: "Лист 1",
      teacher_column: "C",
      columns: [
        "F",
        "I"
      ],
      rule: "Правило 1",
      notification_text: "Текст уведомления 1"
    }
  ]
}
const table2: TableItem = {
  _id: "2",
  name: "Тест таблица2",
  link: "Google Sheets Link 1",
  provider: "Google",
  update_frequency: 1,
  pages: [ 
    {
      id: "1",
      name: "Лист 1",
      teacher_column: "C",
      columns: [
        "F",
        "I"
      ],
      rule: "Правило 1",
      notification_text: "Текст уведомления 1"
    }
  ]
}
//-------------------------------------

tables.addTable(table1);
tables.addTable(table2)

const addTableDialog = ref(false);
</script>

<template>
  <v-container style="width: 80%" >
    <v-dialog
      v-model="addTableDialog"
      max-width="450">
      <AddTableDialog @close-dialog="addTableDialog = false" />
    </v-dialog>
    <v-row justify="start">
      <v-col cols="12" md="10" sm="6">
        <v-btn 
          class="outlined-button" 
          id="add-table-button" 
          size="35px" 
          prepend-icon="$plus" 
          variant="outlined"
          @click="addTableDialog = true">
          Добавить
        </v-btn>
        <v-expansion-panels>
          <TablePanel :tables="tables" />
        </v-expansion-panels>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
#add-table-button {
  width: 150px !important;
  color: limegreen;
  letter-spacing: 0px !important;
}
</style>