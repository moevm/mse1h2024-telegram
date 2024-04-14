<script setup lang="ts">
import { ref, defineProps } from 'vue'
import TableCreator from '@/models/TableModel';
import type TableItem from '@/entities/TableEntity';
import type Page from '@/entities/PageEntity';
import DeleteTableDialog from '@/components/DeleteTableDialog.vue';
import EditTableDialog from '@/components/EditTableDialog.vue'
import AddTableRuleDialog from '@/components/AddTableRuleDialog.vue';
import EditTableRuleDialog from '@/components/EditTableRuleDialog.vue';

const props = defineProps({
  tables: {
    type: Array as () => TableItem[],
    default: () => new TableCreator()
  }
});

const activePanel = ref(0);
const deleteTableDialog = ref(false);
const editTableDialog = ref(false);
const addTableRuleDialog = ref(false);
const editTableRuleDialog = ref(false);
const currentTable = ref({} as TableItem);
const currentPage = ref({} as Page);
</script>

<template>
  <v-dialog
    v-model="editTableRuleDialog"
    max-width="450">
    <EditTableRuleDialog
      :table-id="currentTable.id"
      :page="currentPage"
      @close-dialog="editTableRuleDialog = false"/>
  </v-dialog>
  <v-dialog
    v-model="addTableRuleDialog"
    max-width="450">
    <AddTableRuleDialog 
      :table="currentTable"
      @close-dialog="addTableRuleDialog = false"/>
  </v-dialog>
  <v-dialog
    v-model="editTableDialog"
    max-width="450">
    <EditTableDialog 
      :table="currentTable"
      @close-dialog="editTableDialog = false"/>
  </v-dialog>
  <v-dialog
    v-model="deleteTableDialog"
    max-width="450">
    <DeleteTableDialog 
      :table="currentTable"
      @close-dialog="deleteTableDialog = false"/>
  </v-dialog>
  <v-expansion-panel 
    class="tables" 
    :class="{'bg-gray': i === activePanel}" 
    @click="activePanel = i"
    v-for="(table, i) in props.tables"
    :key="i">
    <v-expansion-panel-title>
      <span id="table-name">{{ table.name === '' ? `Таблица ${i + 1}` : table.name }}</span>
    </v-expansion-panel-title>
    <v-expansion-panel-text>
      <v-btn
        class="outlined-button" 
        id="add-rule-button" 
        size="35px" 
        prepend-icon="$plus" 
        variant="outlined"
        @click="addTableRuleDialog = true;
          currentTable = table;">
        Правило
      </v-btn>
      <v-table density="compact">
        <thead>
          <tr>
            <th>
              Страница
            </th>
            <th>
              Столбец преподавателей
            </th>
            <th>
              Столбец 1
            </th>
            <th>
              Столбец 2
            </th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="item in table.pages"
            :key="item.id">
            <td class="text-table">
              {{ item.name }}
            </td>
            <td class="text-table">
              {{ item.teacher_column }}
            </td>
            <td class="text-table">
              {{ item.columns[0] }}
            </td>
            <td class="text-table">
              {{ item.columns[1] }}
            </td>
            <td>
              <v-icon 
                id="edit-row-button" 
                icon="$edit" 
                @click="editTableRuleDialog = true;
                  currentTable = table;
                  currentPage = item;">
              </v-icon>
            </td>
          </tr>
        </tbody>
      </v-table>
      <v-row justify="space-between">
        <v-col cols="auto">
          <v-btn 
            class="outlined-button" 
            id="edit-table-button" 
            size="35px" 
            prepend-icon="$edit" 
            variant="outlined"
            @click="editTableDialog = true;
              currentTable = table;">
            Изменить
          </v-btn>
        </v-col>
        <v-col cols="auto">
          <v-btn 
            class="outlined-button" 
            id="delete-table-button" 
            size="35px" 
            prepend-icon="$delete" 
            variant="outlined"
            @click="deleteTableDialog = true; 
              currentTable = table;">
            Удалить
          </v-btn>
        </v-col>
      </v-row>
    </v-expansion-panel-text>
  </v-expansion-panel>
</template>

<style scoped>
th {
  text-align: center !important;
  background-color: rgb(228, 228, 228);
}
.tables {
  width: 100%;
  border: 1px solid gray;
  border-radius: 5px;
  margin-top: 20px;
  font-weight: 600;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
.bg-gray {
  background-color: rgb(228, 228, 228);
}
.text-table {
  text-align: center !important;
}
.v-table {
  border: 1px solid gray !important;
  border-collapse: separate;
  border-radius: 5px;
  overflow: hidden;
  font-size: medium;
}
#table-name {
  font-size: 20px;
  color: cornflowerblue;
}
#add-rule-button {
  margin-bottom: 20px;
  width: 135px !important;
  color: limegreen;
  letter-spacing: 0px !important;
}
#edit-row-button {
  color: rgb(238, 155, 0);
  letter-spacing: 0px !important;
}
#edit-table-button {
  margin-top: 20px;
  margin-bottom: 0px;
  width: 150px !important;
  color: rgb(238, 155, 0);
  letter-spacing: 0px !important;
}
#delete-table-button {
  margin-top: 20px;
  margin-bottom: 0px;
  width: 150px !important;
  color: darkred;
  letter-spacing: 0px !important;
}
</style>