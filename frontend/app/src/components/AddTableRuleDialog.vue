<script setup lang="ts">
import { ref, type Ref } from 'vue'
import type Page from '@/entities/PageEntity'
import type TablesStore from '@/interfaces/TableStoreType'
import { v4 as uuidv4 } from 'uuid'
import { useTablesStore } from '@/stores/tablesStore'
import useVuelidate, { type Validation } from '@vuelidate/core'
import PageValidation, { type PageState } from '@/validation/PageValidation'
import type { Rules } from '@/interfaces/ValidationRulesType'

const tablesStore: TablesStore = useTablesStore()

const emit = defineEmits<{
  (event: 'close-dialog'): void
}>()

const props = defineProps<{
  tableId: string
}>()

const pageName: Ref<string> = ref('')
const teacherColumn: Ref<string> = ref('')
const column1: Ref<string> = ref('')
const column2: Ref<string> = ref('')
const operator: Ref<string | null> = ref(null)
const operators: Ref<string[]> = ref(['=', '<=', '>=', '<', '>', '!='])

const pageValidation: PageValidation = new PageValidation()
const rules: Rules = pageValidation.pageRules()
const state: PageState = {
  pageName,
  teacherColumn,
  column1,
  column2,
  operator
}

const v$: Ref<Validation<Rules, PageState>> = useVuelidate(rules, state)

const confirm = async (): Promise<void> => {
  const resultValidation: boolean = await v$.value.$validate()
  if (!resultValidation) {
    return
  }
  const rule: Page = {
    id: uuidv4(),
    name: pageName.value.trim().replace(/\s+/g, ' '),
    teacherColumn: teacherColumn.value.trim(),
    columns: {
      column1: column1.value.trim(),
      column2: column2.value.trim()
    },
    operator: operator.value!
  }
  tablesStore.postTableRule(props.tableId, rule)
  emit('close-dialog')
}
</script>

<template>
  <v-card height="auto">
    <v-card-title class="card-title">
      <div>Добавление правила</div>
    </v-card-title>
    <v-card-text>
      <v-text-field
        v-model:="pageName"
        :clearable="true"
        label="Название страницы"
        :error-messages="v$.pageName.$error ? v$.pageName.$errors[0].$message : ''"
        :required="true"
      ></v-text-field>
      <v-text-field
        v-model:="teacherColumn"
        :clearable="true"
        label="Столбец преподавателей"
        :error-messages="v$.teacherColumn.$error ? v$.teacherColumn.$errors[0].$message : ''"
        :required="true"
      ></v-text-field>
      <v-row>
        <v-col>
          <v-text-field
            v-model:="column1"
            :clearable="true"
            label="Столбец 1"
            :error-messages="v$.column1.$error ? v$.column1.$errors[0].$message : ''"
            :required="true"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-select
            v-model:="operator"
            :clearable="true"
            label="Оператор"
            :error-messages="v$.operator.$error ? v$.operator.$errors[0].$message : ''"
            :items="operators"
            :required="true"
          ></v-select>
        </v-col>
        <v-col>
          <v-text-field
            v-model:="column2"
            :clearable="true"
            label="Столбец 2"
            :error-messages="v$.column2.$error ? v$.column2.$errors[0].$message : ''"
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
