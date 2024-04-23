<script setup lang="ts">
import { ref, type Ref } from 'vue'
import type TablesStore from '@/interfaces/TableStoreType'
import type TableItem from '@/entities/TableEntity'
import { useTablesStore } from '@/stores/tablesStore'
import useVuelidate, { type Validation } from '@vuelidate/core'
import TableItemValidation, {
  type Rules,
  type TableItemState
} from '@/models/TableItemValidation'

const tablesStore: TablesStore = useTablesStore()

const emit = defineEmits<{
  (event: 'close-dialog'): void
}>()

const props = defineProps<{
  table: TableItem
}>()

const tableName: Ref<string> = ref(props.table.name)
const tableLink: Ref<string> = ref(props.table.link)
const tableUpdateSeconds: Ref<number> = ref(props.table.updateFrequency)

const tableItemValidation: TableItemValidation = new TableItemValidation()
const rules: Rules = tableItemValidation.tableItemRules()
const state: TableItemState = {
  tableName,
  tableLink,
  tableUpdateSeconds
}

const v$: Ref<Validation<Rules, TableItemState>> = useVuelidate(rules, state)

const confirm = async (): Promise<void> => {
  const resultValidation: boolean = await v$.value.$validate()
  if (!resultValidation) {
    return
  }
  const changedTable: TableItem = {
    id: props.table.id,
    name: tableName.value,
    link: tableLink.value,
    provider: 'GOOGLE', // Provider is hardcoded for now
    updateFrequency: tableUpdateSeconds.value,
    pages: props.table.pages
  }
  tablesStore.putTable(changedTable)
  emit('close-dialog')
}
</script>

<template>
  <v-card height="auto">
    <v-card-title class="card-title">
      <div>Изменение таблицы</div>
    </v-card-title>
    <v-card-text>
      <v-text-field
        v-model="tableName"
        :clearable="true"
        label="Название таблицы в системе"
        :error-messages="v$.tableName.$error ? v$.tableName.$errors[0].$message : ''"
        :required="true"
        @input="v$.tableName.$touch"
      ></v-text-field>
      <v-text-field
        v-model="tableLink"
        :clearable="true"
        label="ID таблицы"
        :error-messages="v$.tableLink.$error ? v$.tableLink.$errors[0].$message : ''"
        :required="true"
        @input="v$.tableLink.$touch"
      ></v-text-field>
      <v-text-field
        v-model="tableUpdateSeconds"
        :clearable="true"
        label="Частота обновления в секундах"
        :error-messages="
          v$.tableUpdateSeconds.$error ? v$.tableUpdateSeconds.$errors[0].$message : ''
        "
        :required="true"
        @input="v$.tableUpdateSeconds.$touch"
      ></v-text-field>
    </v-card-text>
    <v-card-actions class="card-actions">
      <v-btn
        class="outlined-button"
        id="cancel-button"
        size="40px"
        variant="outlined"
        @click="$emit('close-dialog')"
      >
        Отмена
      </v-btn>
      <v-btn
        class="outlined-button"
        id="confirm-button"
        size="40px"
        variant="outlined"
        @click="confirm"
      >
        Подтвердить
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<style scoped>
#confirm-button {
  color: limegreen;
}
#cancel-button {
  color: rgb(181, 0, 0);
}
</style>
