<script setup lang="ts">
import { ref, defineProps } from 'vue'

const props = defineProps({
  tables: {
    type: Array,
    default: () => [[]],
    validator: (tables: any[]) => {
      return tables.every(table => 
        table.every(item => 
          typeof item === 'object' &&
          'page' in item &&
          'teachersColumn' in item &&
          'column1' in item &&
          'column2' in item
        )
      );
    }
  }
});
const activePanel = ref(0);
</script>

<template>
	<v-expansion-panel class="tables" :class="{'bg-gray': i == activePanel}" @click="activePanel = i"
		v-for="(table, i) in props.tables"
		:key="i">
	<v-expansion-panel-title>
			Таблица {{i + 1}}
	</v-expansion-panel-title>
	<v-expansion-panel-text>
			<v-btn class="outlined-button" id="add-rule-button" size="35px" prepend-icon="$plus" variant="outlined">
			Правило
			</v-btn>
			<v-table density="compact">
			<thead>
					<tr>
					<th>
							Страница
					</th>
					<th>
							Столбец преподавателей
					</th>
					<th>
							Столбец преподавателей
					</th>
					<th>
							Столбец преподавателей
					</th>
					<th></th>
					</tr>
			</thead>
			<tbody>
					<tr
					v-for="item in table"
					:key="item.page"
					>
					<td class="text-table">Страница {{ item.page }}</td>
					<td class="text-table">{{ item.teachersColumn }}</td>
					<td class="text-table">{{ item.column1 }}</td>
					<td class="text-table">{{ item.column2 }}</td>
					<td>
							<v-icon id="edit-row-button" icon="$edit" @click=""></v-icon>
					</td>
					</tr>
			</tbody>
			</v-table>
			<v-row justify="space-between">
			<v-col cols="auto">
					<v-btn class="outlined-button" id="edit-table-button" size="35px" prepend-icon="$edit" variant="outlined">
					Изменить
					</v-btn>
			</v-col>
			<v-col cols="auto">
					<v-btn class="outlined-button" id="delete-table-button" size="35px" prepend-icon="$delete" variant="outlined">
					Удалить
					</v-btn>
			</v-col>
			</v-row>
	</v-expansion-panel-text>
	</v-expansion-panel>
</template>

<style scoped>
th {
  text-align: center !important;
  background-color: rgb(228, 228, 228);
}
.tables {
  width: 100%;
  border: 1px solid gray;
  border-radius: 5px;
  margin-top: 20px;
  color:cornflowerblue;
  font-size: large;
  font-weight: 600;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
.bg-gray {
  background-color: rgb(228, 228, 228);
}
.text-table {
  text-align: center !important;
}
.v-table {
  border: 1px solid gray !important;
  border-collapse: separate;
  border-radius: 5px;
  overflow: hidden;
}
#add-rule-button {
  margin-bottom: 20px;
  width: 135px !important;
  color: limegreen;
}
#edit-row-button {
  color: rgb(238, 155, 0);
}
#edit-table-button {
  margin-top: 20px;
  margin-bottom: 0px;
  width: 150px !important;
  color: rgb(238, 155, 0);
}
#delete-table-button {
  margin-top: 20px;
  margin-bottom: 0px;
  width: 150px !important;
  color: darkred;
}
</style>