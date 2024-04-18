<script setup lang="ts">
import { ref, defineProps, defineEmits, type Ref } from 'vue'
import { useTablesStore } from '@/stores/tablesStore'
import type TableItem from '@/entities/TableEntity'

const tablesStore = useTablesStore()

const emit = defineEmits(['close-dialog'])

const props = defineProps({
  table: {
    type: Object as () => TableItem,
    default: () => {}
  }
})

//- Данные ------------------------------------------------------
const tableName: Ref<string> = ref(props.table.name)
const tableLink: Ref<string> = ref(props.table.link)
const tableUpdateSeconds: Ref<number> = ref(props.table.updateFrequency)
//---------------------------------------------------------------

const confirm = (): void => {
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
  <v-card height="360" title="Изменение таблицы">
    <v-card-text>
      <v-text-field
        v-model="tableName"
        clearable
        label="Название таблицы в системе"
        required
      ></v-text-field>
      <v-text-field v-model="tableLink" clearable label="Ссылка" required></v-text-field>
      <v-text-field
        v-model="tableUpdateSeconds"
        clearable
        label="Частота обновления в секундах"
        required
      ></v-text-field>
      <v-row justify="end">
        <v-col cols="auto">
          <v-btn
            class="outlined-button"
            id="cancel-button"
            size="40px"
            variant="outlined"
            @click="$emit('close-dialog')"
          >
            Отмена
          </v-btn>
        </v-col>
        <v-col cols="auto">
          <v-btn
            class="outlined-button"
            id="confirm-button"
            size="40px"
            variant="outlined"
            @click="confirm"
          >
            Подтвердить
          </v-btn>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<style scoped>
.v-card {
  text-align: center;
  font-family:
    system-ui,
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    Oxygen,
    Ubuntu,
    Cantarell,
    'Open Sans',
    'Helvetica Neue',
    sans-serif;
}
#confirm-button {
  width: 150px !important;
  color: limegreen;
  letter-spacing: 0px !important;
}
#cancel-button {
  width: 100px !important;
  color: darkred;
  letter-spacing: 0px !important;
}
</style>
