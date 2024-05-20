<script setup lang="ts">
import { ref, type Ref } from 'vue'
import { mdiPlus, mdiPencil, mdiMinusCircleOutline, mdiOpenInNew } from '@mdi/js'
import type TableItem from '@/entities/TableEntity'
import type Page from '@/entities/PageEntity'
import DeleteTableDialog from '@/components/DeleteTableDialog.vue'
import DeleteTableRuleDialog from '@/components/DeleteTableRuleDialog.vue'
import EditTableDialog from '@/components/EditTableDialog.vue'
import EditTableRuleDialog from '@/components/EditTableRuleDialog.vue'
import AddTableRuleDialog from '@/components/AddTableRuleDialog.vue'

const props = defineProps<{
  tables: TableItem[]
}>()

const activePanel: Ref<number> = ref(-1)
const deleteTableDialog: Ref<boolean> = ref(false)
const deleteTableRuleDialog: Ref<boolean> = ref(false)
const editTableDialog: Ref<boolean> = ref(false)
const editTableRuleDialog: Ref<boolean> = ref(false)
const addTableRuleDialog: Ref<boolean> = ref(false)
const currentTable: Ref<TableItem> = ref({} as TableItem)
const currentPage: Ref<Page> = ref({} as Page)
</script>

<template>
  <!-- Delete Table Rule -->
  <v-dialog v-model="deleteTableRuleDialog" max-width="450">
    <DeleteTableRuleDialog
      :table-id="currentTable.id!"
      :page="currentPage"
      @close-dialog="deleteTableRuleDialog = false"
    />
  </v-dialog>
  <!-- Edit Table Rule -->
  <v-dialog v-model="editTableRuleDialog" max-width="600">
    <EditTableRuleDialog
      :table-id="currentTable.id!"
      :page="currentPage"
      @close-dialog="editTableRuleDialog = false"
    />
  </v-dialog>
  <!-- Add Table Rule -->
  <v-dialog v-model="addTableRuleDialog" max-width="600">
    <AddTableRuleDialog :table-id="currentTable.id!" @close-dialog="addTableRuleDialog = false" />
  </v-dialog>
  <!-- Edit Table -->
  <v-dialog v-model="editTableDialog" max-width="450">
    <EditTableDialog :table="currentTable" @close-dialog="editTableDialog = false" />
  </v-dialog>
  <!-- Delete Table -->
  <v-dialog v-model="deleteTableDialog" max-width="450">
    <DeleteTableDialog :table="currentTable" @close-dialog="deleteTableDialog = false" />
  </v-dialog>
  <v-expansion-panel
    class="tables"
    :class="{ 'bg-gray': i === activePanel }"
    @click="activePanel = i"
    v-for="(table, i) in props.tables"
    :key="i"
  >
    <v-expansion-panel-title>
      <span id="table-name">{{ table.name }}</span>
      <v-btn
        id="link-button"
        :icon="mdiOpenInNew"
        variant="plain"
        density="compact"
        :href="'https://docs.google.com/spreadsheets/d/' + table.link"
        @mousedown.prevent="$event.stopPropagation()"
      ></v-btn>
    </v-expansion-panel-title>
    <v-expansion-panel-text>
      <v-btn
        class="outlined-button"
        id="add-button"
        data-testid="add-rule-button"
        size="35px"
        :prepend-icon="mdiPlus"
        variant="outlined"
        @click="
          addTableRuleDialog = true;
          currentTable = table;
        "
      >
        Правило
      </v-btn>
      <v-table class="table" density="compact">
        <thead>
          <tr class="table-header">
            <th>Страница</th>
            <th>Столбец преподавателей</th>
            <th>Столбец 1</th>
            <th>Оператор</th>
            <th>Столбец 2</th>
            <th></th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr class="table-data" v-for="item in table.pages" :key="item.id">
            <td>
              {{ item.name }}
            </td>
            <td>
              {{ item.teacherColumn }}
            </td>
            <td>
              {{ item.columns.column1 }}
            </td>
            <td>
              {{ item.operator }}
            </td>
            <td>
              {{ item.columns.column2 }}
            </td>
            <td>
              <v-icon
                id="edit-button"
                :icon="mdiPencil"
                @click="
                  editTableRuleDialog = true;
                  currentTable = table;
                  currentPage = item;
                "
              >
              </v-icon>
            </td>
            <td>
              <v-icon
                id="delete-button"
                :icon="mdiMinusCircleOutline"
                @click="
                  deleteTableRuleDialog = true;
                  currentTable = table;
                  currentPage = item;
                "
              >
              </v-icon>
            </td>
          </tr>
        </tbody>
      </v-table>
      <v-row justify="space-between">
        <v-col cols="auto">
          <v-btn
            class="outlined-button"
            id="edit-button"
            size="35px"
            :prepend-icon="mdiPencil"
            variant="outlined"
            @click="
              editTableDialog = true;
              currentTable = table;
            "
          >
            Изменить
          </v-btn>
        </v-col>
        <v-col cols="auto">
          <v-btn
            class="outlined-button"
            id="delete-button"
            size="35px"
            :prepend-icon="mdiMinusCircleOutline"
            variant="outlined"
            @click="
              deleteTableDialog = true;
              currentTable = table;
            "
          >
            Удалить
          </v-btn>
        </v-col>
      </v-row>
    </v-expansion-panel-text>
  </v-expansion-panel>
</template>

<style scoped>
.tables {
  border: 1px solid gray;
  margin-top: 20px;
  font-weight: 600;
}
.bg-gray {
  background-color: rgb(228, 228, 228);
}
#link-button {
  color: cornflowerblue;
}
#table-name {
  font-size: 20px;
  color: cornflowerblue;
}
#add-button {
  color: limegreen;
}
#delete-button {
  color: rgb(181, 0, 0);
}
#edit-button {
  color: rgb(238, 155, 0);
}
</style>
