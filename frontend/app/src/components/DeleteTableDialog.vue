<script setup lang="ts">
import { defineProps, defineEmits } from 'vue';
import type TableItem from '@/entities/TableEntity';
import { useTablesStore } from '@/stores/tablesStore';

const tablesStore = useTablesStore();

const emit = defineEmits(['close-dialog']);

const props = defineProps({
  table: {
    type: Object as () => TableItem,
    default: () => {}
  }
});

const confirm = () => {
  tablesStore.deleteTable(props.table);
  emit('close-dialog');
};
</script>

<template>
  <v-card
    height="240"
    title="Удаление таблицы">
    <v-card-text>
      Вы уверены, что хотите удалить таблицу: {{props.table.name}}?<br/>
      <strong>Данное действие не обратимо, вся информация и настройки таблицы будут удалены.</strong>
      <v-row justify="end">
        <v-col cols="auto">
          <v-btn 
            class="outlined-button"
            id="cancel-button"
            size="40px"
            variant="outlined"
            @click="$emit('close-dialog')">
            Отмена
          </v-btn>
        </v-col>
        <v-col cols="auto">
          <v-btn 
            class="outlined-button"
            id="delete-button"
            size="40px" 
            variant="outlined"
            @click="confirm">
            Удалить
          </v-btn>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<style scoped>
strong {
  color: rgb(185,34,34);
}
.v-card-text {
  text-align: left;
  font-weight: 600;
}
.v-card {
  text-align: center;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
#delete-button {
  width: 100px !important;
  color: darkred;
  letter-spacing: 0px !important;
}
#cancel-button {
  width: 100px !important;
  color: gray;
  letter-spacing: 0px !important;
}
</style>