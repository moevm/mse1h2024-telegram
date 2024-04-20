<script setup lang="ts">
import type Page from '@/entities/PageEntity'
import type TablesStore from '@/interfaces/TableStoreType'
import { useTablesStore } from '@/stores/tablesStore'

const tablesStore: TablesStore = useTablesStore()

const emit = defineEmits<{
  (event: 'close-dialog'): void
}>()

const props = defineProps<{
  tableId: string
  page: Page
}>()

const confirm = (): void => {
  tablesStore.deleteTableRule(props.tableId, props.page.id)
  emit('close-dialog')
}
</script>

<template>
  <v-card height="auto">
    <v-card-title class="card-title">
      <div>Удаление правила</div>
    </v-card-title>
    <v-card-text class="card-text">
      Вы уверены, что хотите удалить правило для данной страницы: {{ page.name }}?<br />
      <strong id="warning-text"
        >Данное действие не обратимо, вся информация о правиле будет удалена.</strong
      >
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
        id="delete-button"
        size="40px"
        variant="outlined"
        @click="confirm"
      >
        Удалить
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<style scoped>
.card-text {
  text-align: left;
  font-weight: 600;
}
#warning-text {
  color: rgb(185, 34, 34);
}
#delete-button {
  color: rgb(181, 0, 0);
}
#cancel-button {
  color: gray;
}
</style>
