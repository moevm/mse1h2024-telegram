<script setup lang="ts">
import { ref, defineProps, defineEmits, type Ref } from "vue";
import type Page from "@/entities/PageEntity";
import { v4 as uuidv4 } from "uuid";
import { useTablesStore } from "@/stores/tablesStore";

const tablesStore = useTablesStore();

const emit = defineEmits(["close-dialog"]);

const props = defineProps({
  tableId: {
    type: String,
    default: ""
  }
});

//- Данные ------------------------------------------------
const pageName: Ref<string> = ref("");
const teacherColumn: Ref<string> = ref("");
const column1: Ref<string> = ref("");
const column2: Ref<string> = ref("");
const operator: Ref<string> = ref("");
const operators: Ref<string[]> = ref(["=", "<=", ">=", "<", ">", "!="]);
//---------------------------------------------------------

const confirm = (): void => {
  const rule: Page = {
    id: uuidv4(),
    name: pageName.value,
    teacherColumn: teacherColumn.value,
    columns: {
      column1: column1.value,
      column2: column2.value
    },
    operator: operator.value
  }
  tablesStore.postTableRule(props.tableId, rule);
  emit("close-dialog");
};
</script>

<template>
  <v-card
    height="380"
    title="Добавление правила">
    <v-card-text>
      <v-text-field
        v-model:="pageName"
        clearable
        label="Название страницы"
        required></v-text-field>
      <v-text-field
        v-model:="teacherColumn"
        clearable
        label="Столбец преподавателей"
        required></v-text-field>
      <v-row>
        <v-col>
          <v-text-field
            v-model:="column1"
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
            required></v-select>
        </v-col>
        <v-col>
          <v-text-field
            v-model:="column2"
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