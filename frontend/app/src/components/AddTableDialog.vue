<script setup lang="ts">
import { ref, type Ref } from 'vue'
import type TableItem from '@/entities/TableEntity'
import type TablesStore from '@/interfaces/TableStoreType'
import { useTablesStore } from '@/stores/tablesStore'

const tablesStore: TablesStore = useTablesStore()

const emit = defineEmits<{
  (event: 'close-dialog'): void
}>()

const tableName: Ref<string> = ref('')
const tableLink: Ref<string> = ref('')
const tableUpdateSeconds: Ref<string> = ref('')

const confirm = (): void => {
  const table: TableItem = {
    name: tableName.value,
    link: tableLink.value,
    provider: 'GOOGLE', // Provider is hardcoded for now
    updateFrequency: Number(tableUpdateSeconds.value), // import vuelidate in future
    pages: []
  }
  tablesStore.postTable(table)
  emit('close-dialog')
}
</script>

<template>
  <v-card height="auto">
    <v-card-title class="card-title">
      <div>Добавление таблицы</div>
    </v-card-title>
    <v-card-text>
      <v-text-field
        v-model="tableName"
        :clearable="true"
        label="Название таблицы в системе"
        :required="true"
      ></v-text-field>
      <v-text-field
        v-model="tableLink"
        :clearable="true"
        label="ID таблицы"
        :required="true"
      ></v-text-field>
      <v-text-field
        v-model="tableUpdateSeconds"
        :clearable="true"
        label="Частота обновления в секундах"
        :required="true"
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
