<script setup lang="ts">
import { ref, computed, type Ref, type ComputedRef } from 'vue'
import { useTablesStore } from '@/stores/tablesStore'
import { mdiPlus } from '@mdi/js'
import TablePanel from '@/views/TablesPanel.vue'
import AddTableDialog from '@/components/AddTableDialog.vue'
import type TableItem from '@/entities/TableEntity'

const tablesStore = useTablesStore()
const tables: Ref<{ data: TableItem[] }> = ref(tablesStore.tables)
const itemsPerPage: Ref<number> = ref(5)
const currentPage: Ref<number> = ref(1)
const totalPages: ComputedRef<number> = computed(() =>
  Math.ceil(tables.value.data.length / itemsPerPage.value)
)
const addTableDialog: Ref<boolean> = ref(false)
</script>

<template>
  <v-container>
    <v-dialog v-model="addTableDialog" max-width="450">
      <AddTableDialog @close-dialog="addTableDialog = false" />
    </v-dialog>
    <v-row justify="start">
      <v-col cols="12" md="10" sm="6">
        <v-btn
          class="outlined-button"
          id="add-button"
          data-testid="add-table-button"
          size="35px"
          :prepend-icon="mdiPlus"
          variant="outlined"
          @click="addTableDialog = true"
        >
          Добавить
        </v-btn>
        <v-expansion-panels>
          <TablePanel
            :tables="
              tables.data.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage)
            "
          />
        </v-expansion-panels>
        <v-pagination v-model="currentPage" :length="totalPages"></v-pagination>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
#add-button {
  color: limegreen;
}
</style>
