<script setup lang="ts">
import { ref, defineProps, defineEmits, type Ref } from "vue";
import type Page from "@/entities/PageEntity";
import { useTablesStore } from "@/stores/tablesStore";

const tablesStore = useTablesStore();

const emit = defineEmits(["close-dialog"]);

const props = defineProps({
  tableId: {
    type: String,
    default: ""
  },
  page: {
    type: Object as () => Page,
    default: () => {}
  }
});

//- Данные ----------------------------------------
const pageName: Ref<string> = ref(props.page.name);
const teacherColumn: Ref<string> = ref(props.page.teacherColumn);
const column1: Ref<string> = ref(props.page.columns.column1);
const column2: Ref<string> = ref(props.page.columns.column2);
const operator: Ref<string> = ref(props.page.operator);
const operators: Ref<string[]> = ref(["=", "<=", ">=", "<", ">", "!="]);
//-------------------------------------------------

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
  tablesStore.putTableRule(props.tableId, changedRule);
  emit("close-dialog");
};
</script>

<template>
  <v-card
    height="380"
    title="Изменить правило">
    <v-card-text>
      <v-text-field
        v-model="pageName"
        clearable
        label="Название страницы"
        required></v-text-field>
      <v-text-field
        v-model="teacherColumn"
        clearable
        label="Столбец преподавателей"
        required></v-text-field>
      <v-row>
        <v-col>
          <v-text-field
            v-model="column1"
            clearable
            label="Столбец 1"
            required></v-text-field>
        </v-col>        
        <v-col>
          <v-select
            v-model:="operator"
            clearable
            label="Оператор"
            :items="operators"
            item-value="icon"
            required></v-select>
        </v-col>
        <v-col>
          <v-text-field
            v-model="column2"
            clearable
            label="Столбец 2"
            required></v-text-field>
        </v-col>
      </v-row>
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
            id="confirm-button"
            size="40px" 
            variant="outlined"
            @click="confirm">
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
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
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