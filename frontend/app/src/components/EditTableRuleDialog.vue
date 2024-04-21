<script setup lang="ts">
import { ref, type Ref } from 'vue'
import type TablesStore from '@/interfaces/TableStoreType'
import type Page from '@/entities/PageEntity'
import { useTablesStore } from '@/stores/tablesStore'

const tablesStore: TablesStore = useTablesStore()

const emit = defineEmits<{
  (event: 'close-dialog'): void
}>()

const props = defineProps<{
  tableId: string
  page: Page
}>()

const pageName: Ref<string> = ref(props.page.name)
const teacherColumn: Ref<string> = ref(props.page.teacherColumn)
const column1: Ref<string> = ref(props.page.columns.column1)
const column2: Ref<string> = ref(props.page.columns.column2)
const operator: Ref<string> = ref(props.page.operator)
const operators: Ref<string[]> = ref(['=', '<=', '>=', '<', '>', '!='])

const confirm = (): void => {
  const changedRule: Page = {
    id: props.page.id,
    name: pageName.value,
    teacherColumn: teacherColumn.value,
    columns: {
      column1: column1.value,
      column2: column2.value
    },
    operator: operator.value,
    notification: props.page.notification
  }
  tablesStore.putTableRule(props.tableId, changedRule)
  emit('close-dialog')
}
</script>

<template>
  <v-card height="auto" title="Изменить правило">
    <v-card-text>
      <v-text-field
        v-model="pageName"
        :clearable="true"
        label="Название страницы"
        :required="true"
      ></v-text-field>
      <v-text-field
        v-model="teacherColumn"
        :clearable="true"
        label="Столбец преподавателей"
        :required="true"
      ></v-text-field>
      <v-row>
        <v-col>
          <v-text-field
            v-model="column1"
            :clearable="true"
            label="Столбец 1"
            :required="true"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-select
            v-model:="operator"
            :clearable="true"
            label="Оператор"
            :items="operators"
            item-value="icon"
            :required="true"
          ></v-select>
        </v-col>
        <v-col>
          <v-text-field
            v-model="column2"
            :clearable="true"
            label="Столбец 2"
            :required="true"
          ></v-text-field>
        </v-col>
      </v-row>
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
